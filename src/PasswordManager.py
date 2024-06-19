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
        if os.path.exists(self.key_file):
            with open(self.key_file, 'rb') as file:
                key = file.read()
        else:
            key = Fernet.generate_key()
            with open(self.key_file, 'wb') as file:
                file.write(key)
        return key

    def load_passwords(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, 'rb') as file:
                encrypted_data = file.read()
            decrypted_data = self.cipher.decrypt(encrypted_data)
            return json.loads(decrypted_data)
        else:
            return {}

    def save_passwords(self):
        encrypted_data = self.cipher.encrypt(json.dumps(self.passwords).encode())
        with open(self.data_file, 'wb') as file:
            file.write(encrypted_data)

    def add_password(self, site, username, password):
        self.passwords[site] = {'username': username, 'password': password}
        self.save_passwords()

    def get_password(self, site):
        pyperclip.copy(self.passwords.get(site, None)['password'])
        return self.passwords.get(site, None)
