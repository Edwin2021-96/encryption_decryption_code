import os
import re
import shutil

class FilenameTransformer:
    def __init__(self, directory='/Volumes/SSD2/Bank Statements/'):
        self.directory = directory
        self.month_map = {
            "Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04",
            "May": "05", "Jun": "06", "Jul": "07", "Aug": "08",
            "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"
        }

    def parse_filename(self, filename):
        """Parse the original filename to extract date components."""
        pattern = r"Statement_(\d{2})([A-Za-z]{3})(\d{4})"
        match = re.match(pattern, filename)
        if not match:
            return None
        
        day, mon, year = match.groups()
        return day, mon, year

    def ensure_year_directory(self, year):
        """Ensure that a directory for the year exists, create if not."""
        dir_path = os.path.join(self.directory, year)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        return dir_path

    def transform_filename(self, filename):
        """Transforms the given filename from 'Statement_ddMonyyyy' to 'yyyymmdd' and manages directory."""
        parsed = self.parse_filename(filename)
        if not parsed:
            return None
        
        day, mon, year = parsed
        original_ext = os.path.splitext(filename)[1]  # Capture the file extension
        new_filename = f"{year}{self.month_map[mon]}{day}{original_ext}"
        directory = self.ensure_year_directory(year)
        new_path = os.path.join(directory, new_filename)
        return new_path

    def process_directory(self):
        """Process all files in the specified directory."""
        files_processed = 0
        for filename in os.listdir(self.directory):
            full_path = os.path.join(self.directory, filename)
            if os.path.isfile(full_path):
                new_path = self.transform_filename(filename)
                if new_path:
                    shutil.move(full_path, new_path)
                    print(f"File {filename} transformed and moved to {new_path}")
                    files_processed += 1
        
        if files_processed == 0:
            print("No target files found in the directory.")

