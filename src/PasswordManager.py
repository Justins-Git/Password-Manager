import os
import json
from cryptography.fernet import Fernet
import pyperclip

# Class for back-end part of the password manager
class PasswordManager:
    # Initializes all the important local variables in the PasswordManager class
    def __init__(self, key_file='key.key', data_file='passwords.json'):
        self.key_file = key_file
        self.data_file = data_file
        self.key = self.load_key()
        self.cipher = Fernet(self.key)
        self.passwords = self.load_passwords()

    # Creates an unique key to you if there is not one already and opens it
    def load_key(self):
        # If the key file exists, open it and read the key
        if os.path.exists(self.key_file):
            with open(self.key_file, 'rb') as file:
                key = file.read()
        # If the key file does not exist, create a new key and save it
        else:
            key = Fernet.generate_key()
            with open(self.key_file, 'wb') as file:
                file.write(key)
        return key
    
    # Loads the passwords from the data file
    def load_passwords(self):
        # If the data file exists, open it and read the encrypted data
        if os.path.exists(self.data_file):
            with open(self.data_file, 'rb') as file:
                encrypted_data = file.read()
            decrypted_data = self.cipher.decrypt(encrypted_data)
            # Return the decrypted data
            return json.loads(decrypted_data)
        else:
            return {}
        
    # Saves the passwords to the data file
    def save_passwords(self):
        encrypted_data = self.cipher.encrypt(json.dumps(self.passwords).encode())
        with open(self.data_file, 'wb') as file:
            file.write(encrypted_data)
            
    # Adds a password to the password manager
    def add_password(self, site, username, password):
        self.passwords[site] = {'username': username, 'password': password}
        self.save_passwords()
        
    # Removes a password from the password manager
    def get_password(self, site):
        # If the site exists in the passwords, copy the password to the clipboard
        pyperclip.copy(self.passwords.get(site, None)['password'])
        return self.passwords.get(site, None)
    
    
        
