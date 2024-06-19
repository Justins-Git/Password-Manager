# LoginWindow.py
import json
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox

class LoginWindow(QWidget):
    def __init__(self, switch_to_register, switch_to_password_manager):
        super().__init__()
        self.switch_to_register = switch_to_register
        self.switch_to_password_manager = switch_to_password_manager
        self.setupUI()
        
    def setupUI(self):
        layout = QVBoxLayout()
        
        self.username = QLineEdit(self)
        self.username.setPlaceholderText("Username")
        self.password = QLineEdit(self)
        self.password.setPlaceholderText("Password")
        self.password.setEchoMode(QLineEdit.Password)

        self.login_button = QPushButton("Login", self)
        self.login_button.clicked.connect(self.login)

        self.register_button = QPushButton("Register", self)
        self.register_button.clicked.connect(self.switch_to_register)

        layout.addWidget(QLabel("Login"))
        layout.addWidget(self.username)
        layout.addWidget(self.password)
        layout.addWidget(self.login_button)
        layout.addWidget(self.register_button)

        self.setLayout(layout)
    
    def login(self):
        username = self.username.text()
        password = self.password.text()

        try:
            with open('master.json', 'r') as file:
                users = json.load(file)
        except FileNotFoundError:
            users = {}

        if username in users and users[username] == password:
            QMessageBox.information(self, "Success", "Login successful")
            self.switch_to_password_manager()
        else:
            QMessageBox.critical(self, "Error", "Invalid username or password")
