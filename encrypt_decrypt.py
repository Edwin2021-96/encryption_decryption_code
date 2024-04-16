# Encryption:
class Encrypting_Bank_Statements:
    def __init__(self, file_path='/Volumes/SSD2/Bank Statements/', zip_folder_name='Zipped Files', encryption_key_path='/Users/aidanpayne/Documents/Important stuff/Letters/Bank Statements/Bank Statements Encryption Key.docx'):
        """
        Initialize the processor with the necessary paths.
        
        :param file_path: str - path to the directory containing the files to process
        :param zip_folder_name: str - name of the folder to store zipped files
        :param encryption_key_path: str - path to save the encryption key
        """
        self.file_path = file_path
        self.zip_folder_name = zip_folder_name
        self.encryption_key_path = encryption_key_path

    def transform_filenames(self):
        """
        Transform the filenames within the directory.
        """
        from filename_transformer import FilenameTransformer
        transformer = FilenameTransformer(self.file_path)
        transformer.process_directory()

    def zip_year_folders(self):
        """
        Zip the folders organized by year.
        """
        from zipper_for_year_folders import YearFolderZipper
        zipper = YearFolderZipper(self.file_path)
        zipper.process_year_folders()

    def zip_main_folder(self):
        """
        Zip the main folder and delete it after zipping.
        """
        from zipper_for_main_folder import FolderZipper
        fz = FolderZipper(self.zip_folder_name)
        fz.zip_subfolder()
        fz.delete_folder()

    def encrypt_files(self):
        """
        Encrypt the files and manage the encryption keys.
        """
        from encryptor import FileEncryptor
        encryptor = FileEncryptor(f"{self.zip_folder_name}.zip")
        encryptor.encrypt_file()
        encryptor.delete_original_file()
        encryptor.save_key_to_docx(self.encryption_key_path)

    def encrypt_bank_statements(self):
        """
        Process the bank statements by performing a series of operations:
        filename transformation, zipping, and encryption.
        """
        self.transform_filenames()
        self.zip_year_folders()
        self.zip_main_folder()
        self.encrypt_files()

# Decryption:
class Decrypting_Bank_Statements:
    def __init__(self):
        from decryptor import FileDecryptor
        from unzipper_for_main_folder import Unzipper_MF
        from unzipper_for_year_folders import Unzipper_YF
        
        self.decryptor = FileDecryptor()
        self.mf_unzip = Unzipper_MF()
        self.yf_unzip = Unzipper_YF()

    def decrypt_bank_statements(self):
        """ Decrypts, unzips, and organizes files. """
        # Step 1: Decrypt the file
        self.decryptor.set_key_from_input()
        decrypted_data = self.decryptor.decrypt_file()
        self.decryptor.write_decrypted_file(decrypted_data)
        self.decryptor.remove_encrypted_file()

        # Step 2: Unzip files in the main folder
        self.mf_unzip.unzip_file()

        # Step 3: Move files up one level and delete empty subfolders
        subfolders = [
            '/Volumes/SSD2/Bank Statements/Zipped Files/Zipped Files/',
            '/Volumes/SSD2/Bank Statements/Zipped Files/'
        ]
        for subfolder in subfolders:
            self.mf_unzip.move_files_up_one_level_and_delete_if_empty(subfolder)

        # Step 4: Unzip and organize files in year folders
        self.yf_unzip.unzip_and_organize()

class BankStatementManager:
    def __init__(self):
        self.encryptor = Encrypting_Bank_Statements()
        self.decryptor = Decrypting_Bank_Statements()

    def run(self):
        print('Choose an option:')
        print('E - Encrypt')
        print('D - Decrypt')
        print('Q - Quit')

        # Display a simple command-line menu
        while True:
            choice = input("Enter your choice: ").strip().upper()
            if choice == 'E':
                print("Starting the encryption process...")
                self.encryptor.encrypt_bank_statements()
                print("Encryption completed successfully.")
            elif choice == 'D':
                print("Starting the decryption process...")
                self.decryptor.decrypt_bank_statements()
                print("Decryption completed successfully.")
            elif choice == 'Q':
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please try again.")