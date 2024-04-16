import os
import zipfile
import sys
import shutil

class FolderZipper:
    def __init__(self, subfolder_name):
        self.subfolder_name = '/Volumes/SSD2/Bank Statements/' + subfolder_name
        self.zip_filename = f"{subfolder_name}.zip"

    def zip_subfolder(self):
        # Check if the subfolder exists
        if not os.path.isdir(self.subfolder_name):
            print(f"Error: The directory '{self.subfolder_name}' does not exist.")
            sys.exit(1)

        # Create a zip file and add the subfolder with its contents
        with zipfile.ZipFile(self.zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(self.subfolder_name):
                for file in files:
                    # Create the file path
                    file_path = os.path.join(root, file)
                    # Add file to the zip file
                    zipf.write(file_path, os.path.relpath(file_path, os.path.dirname(self.subfolder_name)))

        print(f"Created zip file: {self.zip_filename}")

    def delete_folder(self):
        shutil.rmtree(self.subfolder_name)
        print(f"Deleted {self.subfolder_name} folder.")

