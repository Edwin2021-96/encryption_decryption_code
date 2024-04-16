import os
import zipfile
import shutil
from datetime import datetime

class YearFolderZipper:
    def __init__(self, base_path='/Volumes/SSD2/Bank Statements/'):
        self.base_path = base_path
        self.zipped_folder_path = os.path.join(self.base_path, 'Zipped Files')
        self.current_year = datetime.now().year

    def prepare_zipped_directory(self):
        """Create a directory for storing zipped files if it does not exist."""
        if not os.path.exists(self.zipped_folder_path):
            os.makedirs(self.zipped_folder_path)
            print(f"Created folder: {self.zipped_folder_path}")

    def zip_directory(self, item):
        """Zip the specified directory."""
        item_path = os.path.join(self.base_path, item)
        zip_file_name = f"{item}.zip"
        zip_file_path = os.path.join(self.base_path, zip_file_name)

        with zipfile.ZipFile(zip_file_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(item_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, start=item_path)
                    zipf.write(file_path, arcname)

        print(f"Created zip for {item}: {zip_file_name}")
        self.move_and_cleanup(zip_file_path, zip_file_name, item_path, item)

    def move_and_cleanup(self, zip_file_path, zip_file_name, item_path, item):
        """Move the zip file to the zipped files folder and delete the original directory."""
        shutil.move(zip_file_path, self.zipped_folder_path)
        print(f"Moved {zip_file_name} to {self.zipped_folder_path}")
        shutil.rmtree(item_path)
        print(f"Deleted original folder: {item}")

    def process_year_folders(self):
        """Process all year folders in the base directory by zipping them."""
        self.prepare_zipped_directory()
        for item in os.listdir(self.base_path):
            item_path = os.path.join(self.base_path, item)
            if os.path.isdir(item_path) and item.isdigit() and int(item) <= self.current_year:
                self.zip_directory(item)

