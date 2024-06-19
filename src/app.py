import sys
from PyQt5.QtWidgets import QApplication
from PasswordManager import PasswordManager 
from PasswordManagerApp import PasswordManagerApp  

def main():
    app = QApplication(sys.argv)
    password_manager = PasswordManager()
    pm_app = PasswordManagerApp(password_manager)
    pm_app.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()