import sys
from PyQt5.QtWidgets import QApplication
from interface.login_interface import LoginWindow
from interface.main_interface import MainInterface
from interface.login_interface import LoginWindow


if __name__ == "__main__": 
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show() 
    
    sys.exit(app.exec_())