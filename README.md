# Encryption/Decryption Code
Made an encryption/decryption (and other stuff) program. Need help with making a GUI out of it though so if you have any suggestions or anything I can improve, then let me know :)

Disclaimer: the text mentions financial information but the code holds no financial information about me. Hope this clears things up :)

Scripts

filename_transformer.py:

The 'FilenameTransformer' class in the provided Python script manages the transformation and organization of bank statement files based on their filenames. It expects filenames in the format "Statement_ddMonyyyy" and transforms them to a "yyyymmdd" format, also handling the renaming and sorting of files into directories based on the year extracted from the filename. The class automatically creates a new directory for each year if it doesn't already exist. During processing, each file's name is transformed, and the file is moved to the appropriate directory. Messages are printed to indicate successful file processing or if no target files are found.

zipper_for_year_folders.py:

The 'YearFolderZipper' class automates the archiving of folders named by year in a specified base directory by zipping their contents. It creates a separate directory for storing these zips if it doesn't already exist. Each year's folder is compressed into a zip file, which is then moved to the zipped files directory. The original year folder is deleted after its contents have been zipped. This process helps in managing space and organizing files by keeping archived data compact and removing original uncompressed data. ​

zipper_for_main_folder.py:

The 'FolderZipper' class is used to manage the zipping and optional deletion of a specified subfolder within a fixed base directory. It ensures that the subfolder exists before proceeding to zip its contents into a file named after the subfolder. Each file within the subfolder is added to the zip file, retaining its relative path for organization. After zipping, the original subfolder can be completely deleted to free up space. The process is designed to efficiently archive and clean up directory contents while confirming each major action to the user.

encryptor.py:

The 'FileEncryptor' class in Python provides a solution for encrypting files with the Fernet symmetric encryption method. It generates a unique encryption key for each file and allows encrypted data to be saved with a '.enc' extension. The class also includes functionality to delete the original unencrypted file for security purposes. Additionally, it can store the encryption key in a Word document, maintaining a clear structure for easy retrieval. This script offers a secure way to handle sensitive data by encrypting it and effectively managing the encryption keys.

decryptor.py:

The 'FileDecryptor' class in Python is designed to handle the decryption of files encrypted with the Fernet symmetric encryption method. It initializes with the path to an encrypted file and prepares a path for the output of the decrypted content. Users must manually input the encryption key, which the class uses to set up the decryption cypher suite. After decryption, the class can write the decrypted data to a new file and optionally delete the original encrypted file. This script facilitates secure data handling by allowing users to easily decrypt and manage encrypted files.

unzipper_for_main_folder.py:

The 'Unzipper_MF' class facilitates the unzipping of files into a specified directory within a main folder and the subsequent management of these files. It ensures the creation of necessary directories, extracts all contents of a zip file, and securely deletes the zip file post-extraction. Additionally, the class includes functionality to reorganize files by moving them up one directory level and cleaning up any empty directories. This process helps maintain an organized file system within the main directory, ensuring easy access and management of files. Error handling is built into the methods to ensure robust operations even in case of invalid zip files or other filesystem issues. ​

unzipper_for_year_folders.py:

The 'Unzipper_YF' class automates the unzipping of files and the subsequent organization of PDF documents into year-based folders within a specified base directory. It searches for zip files, extracts their contents directly into the base directory, and removes the zip files post-extraction. The class then sorts PDF files into folders named for the year presumed to lead each file's name. Empty directories are cleaned up to maintain organizational efficiency. This systematic approach facilitates the management of archived documents by making them easily accessible based on the year they correspond to.

encrypt_decrypt.py:

The 'encrypt_decrypt.py' script orchestrates complex tasks involving the encryption and decryption of bank statements. It utilizes separate classes for each major step: transforming filenames, zipping, encrypting, decrypting, and finally organizing files. The encryption process includes saving an encryption key in a document for security. After decryption, the script ensures that files are correctly unzipped and organized by year within specified directories. This script provides a comprehensive solution for the secure management and retrieval of sensitive financial documents.

program_runner.py:

The 'program_runner.py' script acts as a launcher for managing bank statements through encryption and decryption tasks. It imports and initializes the 'BankStatementManager' from the 'encrypt_decrypt' module, which encapsulates all the functionality related to the management of bank statements. The script directly invokes the run method of this manager, which is designed to interact with the user through a command-line interface. This setup is ideal for users who need a simple way to execute complex processes without directly interacting with the underlying code. It ensures a user-friendly approach to securely managing sensitive financial data.
