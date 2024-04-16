from cryptography.fernet import Fernet
import getpass
import os

class FileDecryptor:
    def __init__(self, encrypted_file_path='/Volumes/SSD2/Bank Statements/Zipped Files.zip.enc'):
        """
        Initialize the FileDecryptor with the path to the encrypted file.
        """
        self.encrypted_file_path = encrypted_file_path
        self.decrypted_file_path = self.encrypted_file_path.replace('.enc', '')
        self.cipher_suite = None
    
    def set_key_from_input(self):
        """
        Prompt the user to enter the encryption key and setup the cipher suite.
        """
        key_input = getpass.getpass(prompt='Please enter the encryption key: ')
        key = key_input.encode()  # Convert the key to bytes
        self.cipher_suite = Fernet(key)
    
    def decrypt_file(self):
        """
        Read the encrypted file, decrypt it and return the decrypted data.
        """
        with open(self.encrypted_file_path, 'rb') as encrypted_file:
            encrypted_data = encrypted_file.read()
        decrypted_data = self.cipher_suite.decrypt(encrypted_data)
        return decrypted_data
    
    def write_decrypted_file(self, data):
        """
        Write the decrypted data to a file.
        """
        with open(self.decrypted_file_path, 'wb') as decrypted_file:
            decrypted_file.write(data)
        print(f'Decrypted file written to: {self.decrypted_file_path}')
    
    def remove_encrypted_file(self):
        """
        Remove the encrypted file if it exists.
        """
        if os.path.exists(self.encrypted_file_path):
            os.remove(self.encrypted_file_path)
            print(f"Deleted {self.encrypted_file_path}.")
        else:
            print(f"File '{self.encrypted_file_path}' not found.")

