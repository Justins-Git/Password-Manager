import sys
from PyQt5.QtWidgets import QApplication
from PasswordManager import PasswordManager 
from PasswordManagerApp import PasswordManagerApp  

if __name__ == '__main__':
    app = QApplication(sys.argv)
    password_manager = PasswordManager()
    pm_app = PasswordManagerApp(password_manager)
    pm_app.show()
    sys.exit(app.exec_())
