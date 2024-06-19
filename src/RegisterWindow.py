# RegisterWindow.py
import json
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox

class RegisterWindow(QWidget):
    def __init__(self, switch_to_login):
        super().__init__()
        self.switch_to_login = switch_to_login
        self.setupUI()
        
    def setupUI(self):
        self.setWindowTitle('Register')
        
        layout = QVBoxLayout()

        self.username = QLineEdit(self)
        self.username.setPlaceholderText("Username")
        self.password = QLineEdit(self)
        self.password.setPlaceholderText("Password")
        self.password.setEchoMode(QLineEdit.Password)
        self.confirm_password = QLineEdit(self)
        self.confirm_password.setPlaceholderText("Confirm Password")
        self.confirm_password.setEchoMode(QLineEdit.Password)

        self.register_button = QPushButton("Register", self)
        self.register_button.clicked.connect(self.register)

        layout.addWidget(QLabel("Register"))
        layout.addWidget(self.username)
        layout.addWidget(self.password)
        layout.addWidget(self.confirm_password)
        layout.addWidget(self.register_button)

        self.setLayout(layout)
            
    def register(self):
        username = self.username.text()
        password = self.password.text()
        confirm_password = self.confirm_password.text()

        if password != confirm_password:
            QMessageBox.critical(self, "Error", "Passwords do not match")
            return

        try:
            with open('master.json', 'r') as file:
                users = json.load(file)
        except FileNotFoundError:
            users = {}

        if username in users:
            QMessageBox.critical(self, "Error", "Username already exists")
            return

        users[username] = password

        with open('master.json', 'w') as file:
            json.dump(users, file)

        QMessageBox.information(self, "Success", "Registration successful")
        self.switch_to_login()
