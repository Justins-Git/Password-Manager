import json
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QLineEdit, QPushButton, QInputDialog, QMessageBox
from PasswordManager import PasswordManager 

class PasswordManagerApp(QMainWindow):
    # Initializes all the important local variables in the PasswordManagerApp class
    def __init__(self, password_manager):
        super().__init__()
        self.password_manager = password_manager
        self.startUI()
        
    def startUI(self):
        self.setWindowTitle('Account Access')
        
        widget = QWidget()
        layout = QVBoxLayout()
        
        self.register_button = QPushButton('Register Account')
        self.register_button.clicked.connect(self.registerUI)

        self.login_button = QPushButton('Login Account')
        self.login_button.clicked.connect(self.loginUI)
        
        layout.addWidget(self.register_button)
        layout.addWidget(self.login_button)

        widget.setLayout(layout)
        self.setCentralWidget(widget)
    
    def registerUI(self):
        widget = QWidget()
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

        widget.setLayout(layout)
        self.setCentralWidget(widget)
    
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
        self.loginUI()
        
    def loginUI(self):      
        widget = QWidget()
        layout = QVBoxLayout()

        self.username = QLineEdit(self)
        self.username.setPlaceholderText("Username")
        self.password = QLineEdit(self)
        self.password.setPlaceholderText("Password")
        self.password.setEchoMode(QLineEdit.Password)

        self.login_button = QPushButton("Login", self)
        self.login_button.clicked.connect(self.login)

        self.register_button = QPushButton("Register", self)
        self.register_button.clicked.connect(self.registerUI)

        layout.addWidget(QLabel("Login"))
        layout.addWidget(self.username)
        layout.addWidget(self.password)
        layout.addWidget(self.login_button)
        layout.addWidget(self.register_button)

        widget.setLayout(layout)
        self.setCentralWidget(widget)
    
    def login(self):
        username = self.username.text()
        password = self.password.text()

        with open('master.json', 'r') as file:
            users = json.load(file)

        if username in users and users[username] == password:
            QMessageBox.information(self, "Success", "Login successful")
            self.initUI()
        else:
            QMessageBox.critical(self, "Error", "Invalid username or password")
            
        
    # Add the initUI method to the PasswordManagerApp class
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
        
    # Add the add_password method to the PasswordManagerApp class
    def add_password(self):
        # Retrieve the site, username, and password from the user
        site = self.site_input.text()
        username = self.username_input.text()
        password = self.password_input.text()
        # If all fields are filled out
        if site and username and password:
            self.password_manager.add_password(site, username, password)
            QMessageBox.information(self, 'Success', 'Password added successfully.')
            self.site_input.clear()
            self.username_input.clear()
            self.password_input.clear()
            self.initUI()
        else:
            QMessageBox.warning(self, 'Error', 'All fields are required.')
            
    # Add the retrieve_password method to the PasswordManagerApp class
    def retrieve_password(self):
        # Retrieve the site from the user
        site, ok = QInputDialog.getText(self, 'Retrieve Password', 'Enter site:')
        # If the user clicked OK and the site is not empty
        if ok and site:
            # Retrieve the credentials for the site
            credentials = self.password_manager.get_password(site)
            # If credentials were found, show them to the user
            if credentials:
                QMessageBox.information(self, 'Credentials', f"Username: {credentials['username']}\nPassword: {credentials['password']}")
            else:
                QMessageBox.warning(self, 'Error', 'No credentials found for this site.')
                
    # Add the register_password method to the PasswordManagerApp class
    def register_password(self):
        # Create a new instance of the RegisterPasswordDialog class
        self.setWindowTitle('Password Manager')
        #  Show the dialog
        widget = QWidget()
        layout = QVBoxLayout()
        # Create the input fields and submit button
        self.site_label = QLabel('Site:')
        self.site_input = QLineEdit()
        self.username_label = QLabel('Username:')
        self.username_input = QLineEdit()
        self.password_label = QLabel('Password:')
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        
        self.submit_button = QPushButton('Submit')
        self.submit_button.clicked.connect(self.add_password)
        
        # Add the widgets to the layout
        layout.addWidget(self.site_label)
        layout.addWidget(self.site_input)
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.submit_button)
        
        widget.setLayout(layout)
        self.setCentralWidget(widget)