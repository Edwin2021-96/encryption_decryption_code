import os
import zipfile
import shutil

class Unzipper_YF:
    def __init__(self, base_dir='/Volumes/SSD2/Bank Statements/'):
        self.base_dir = base_dir

    def unzip_files(self):
        """ Unzip all zip files in the base directory. """
        zip_files = [f for f in os.listdir(self.base_dir) if f.endswith('.zip')]
        for zip_file in zip_files:
            zip_path = os.path.join(self.base_dir, zip_file)
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(self.base_dir)
            os.remove(zip_path)

    def organize_files_by_year(self):
        """ Organize PDF files into folders based on the year extracted from their filenames. """
        for root, dirs, files in os.walk(self.base_dir):
            for file in files:
                if file.lower().endswith('.pdf'):
                    file_path = os.path.join(root, file)
                    file_year = file[:4]  # Assuming the format is YYYYMMDD
                    year_dir = os.path.join(self.base_dir, file_year)
                    if not os.path.exists(year_dir):
                        os.makedirs(year_dir)
                    shutil.move(file_path, os.path.join(year_dir, file))
                    # Clean up empty directories
                    if not os.listdir(root):
                        shutil.rmtree(root)

    def unzip_and_organize(self):
        """ Unzip all zip files and organize the contents. """
        self.unzip_files()
        self.organize_files_by_year()

