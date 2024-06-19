import sys
from PyQt5.QtWidgets import QApplication
from PasswordManager import PasswordManager 
from WindowManager import WindowManager  

def main():
    app = QApplication(sys.argv)
    password_manager = PasswordManager()
    pm_app = WindowManager(password_manager)
    pm_app.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()