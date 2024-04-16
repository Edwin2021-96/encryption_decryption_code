import os
import zipfile
import shutil

class Unzipper_MF:
    def __init__(self, main_folder='/Volumes/SSD2/Bank Statements/'):
        self.main_folder = main_folder

    def unzip_file(self, zip_path='Zipped Files.zip', output_dir='Zipped Files'):
        """
        Unzip a ZIP file to a specified directory and then delete the ZIP file.
        
        Args:
        zip_path (str): The path to the ZIP file.
        output_dir (str): The directory to extract the files to.
        
        Returns:
        str: Success message indicating that files have been extracted and the original zip deleted.
        """
        # Ensure the output directory exists
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        try:
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(output_dir)
            os.remove(zip_path)
            return f"Files extracted and zip file deleted successfully at {output_dir}"
        except zipfile.BadZipFile:
            return "Error: The file is not a valid zip file"
        except FileNotFoundError:
            return "Error: The zip file does not exist"
        except Exception as e:
            return f"An error occurred: {str(e)}"

    def move_files_up_one_level_and_delete_if_empty(self, subfolder):
        subfolder = os.path.abspath(subfolder)
        items = os.listdir(subfolder)
        files = [f for f in items if os.path.isfile(os.path.join(subfolder, f))]
        other_items = [f for f in items if not os.path.isfile(os.path.join(subfolder, f))]

        moved_files = 0
        for file in files:
            src_path = os.path.join(subfolder, file)
            dest_path = os.path.join(self.main_folder, file)

            if os.path.exists(dest_path):
                continue

            shutil.move(src_path, dest_path)
            moved_files += 1

        if not os.listdir(subfolder):
            try:
                os.rmdir(subfolder)
            except Exception as e:
                pass
        return moved_files

