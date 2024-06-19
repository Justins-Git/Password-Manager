import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QLineEdit, QPushButton, QInputDialog, QMessageBox
from PasswordManager import PasswordManager  # Correctly import the PasswordManager class

class PasswordManagerApp(QMainWindow):
    def __init__(self, password_manager):
        super().__init__()
        self.password_manager = password_manager
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Password Manager')

        widget = QWidget()
        layout = QVBoxLayout()

        self.add_button = QPushButton('Add New Password')
        self.add_button.clicked.connect(self.register_password)

        self.retrieve_button = QPushButton('Retrieve Password')
        self.retrieve_button.clicked.connect(self.retrieve_password)

        layout.addWidget(self.add_button)
        layout.addWidget(self.retrieve_button)

        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def add_password(self):
        site = self.site_input.text()
        username = self.username_input.text()
        password = self.password_input.text()
        if site and username and password:
            self.password_manager.add_password(site, username, password)
            QMessageBox.information(self, 'Success', 'Password added successfully.')
            self.site_input.clear()
            self.username_input.clear()
            self.password_input.clear()
            self.initUI()
        else:
            QMessageBox.warning(self, 'Error', 'All fields are required.')

    def retrieve_password(self):
        site, ok = QInputDialog.getText(self, 'Retrieve Password', 'Enter site:')
        if ok and site:
            credentials = self.password_manager.get_password(site)
            if credentials:
                QMessageBox.information(self, 'Credentials', f"Username: {credentials['username']}\nPassword: {credentials['password']}")
            else:
                QMessageBox.warning(self, 'Error', 'No credentials found for this site.')

    def register_password(self):
        self.setWindowTitle('Password Manager')

        widget = QWidget()
        layout = QVBoxLayout()
        
        self.site_label = QLabel('Site:')
        self.site_input = QLineEdit()
        self.username_label = QLabel('Username:')
        self.username_input = QLineEdit()
        self.password_label = QLabel('Password:')
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        
        self.submit_button = QPushButton('Submit')
        self.submit_button.clicked.connect(self.add_password)
        
        layout.addWidget(self.site_label)
        layout.addWidget(self.site_input)
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.submit_button)
        
        widget.setLayout(layout)
        self.setCentralWidget(widget)