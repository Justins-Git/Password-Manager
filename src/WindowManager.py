import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLabel, QLineEdit, QMessageBox, QInputDialog, QStackedWidget, QComboBox
from PyQt5.QtCore import Qt
from PasswordManager import PasswordManager
from LoginWindow import LoginWindow
from RegisterWindow import RegisterWindow

class WindowManager(QMainWindow):
    def __init__(self, password_manager):
        super().__init__()
        self.password_manager = password_manager
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('Account Access')
        self.setGeometry(100, 100, 300, 200)
        
        self.stack = QStackedWidget(self)
        
        self.login_window = LoginWindow(self.show_register, self.show_password_manager)
        self.register_window = RegisterWindow(self.show_login)
        
        self.stack.addWidget(self.login_window)
        self.stack.addWidget(self.register_window)
        
        self.setCentralWidget(self.stack)

    def show_login(self):
        self.stack.setCurrentWidget(self.login_window)

    def show_register(self):
        self.stack.setCurrentWidget(self.register_window)
    
    def show_password_manager(self):
        widget = QWidget()
        layout = QVBoxLayout()

        self.site_combobox = QComboBox()
        self.site_combobox.view().setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.site_combobox.addItems(self.password_manager.load_passwords().keys())
        self.site_combobox.currentIndexChanged.connect(self.on_site_selected)
        layout.addWidget(self.site_combobox)

        self.retrieve_button = QPushButton('Retrieve Password')
        self.retrieve_button.clicked.connect(self.retrieve_password)
        layout.addWidget(self.retrieve_button)
        
        self.add_button = QPushButton('Add New Password')
        self.add_button.clicked.connect(self.register_password)
        layout.addWidget(self.add_button)

        widget.setLayout(layout)
        self.stack.addWidget(widget)
        self.stack.setCurrentWidget(widget)

    def on_site_selected(self, index):
        self.selected_site = self.site_combobox.currentText()

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
            self.show_password_manager()
        else:
            QMessageBox.warning(self, 'Error', 'All fields are required.')

    def retrieve_password(self):
        site = self.selected_site
        credentials = self.password_manager.get_password(site)
        QMessageBox.information(self, 'Credentials', f"Username: {credentials['username']}\nPassword: {credentials['password']}")
                
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
        self.stack.addWidget(widget)
        self.stack.setCurrentWidget(widget)