from IPython.external.qt_for_kernel import QtCore
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QMessageBox, QPushButton, QLineEdit
import sys
from socket import *


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.gracz = True
        self.title = "Register"
        self.top = 100
        self.left = 100
        self.width = 200
        self.height = 200
        self.InitWindow()


    def InitWindow(self):
        self.kolorowy_kwadracik = QLabel("",self)
        self.kolorowy_kwadracik.setStyleSheet("background-color:pink")
        self.login = QLabel("Login",self)
        self.password = QLabel("Password",self)
        self.in_login = QLineEdit(self)
        self.in_password = QLineEdit(self)
        self.check_pass = QPushButton("Login",self)
        self.check_pass.clicked.connect(self.Check_Login)
        self.register = QPushButton("Register",self)
        self.register.clicked.connect(self.Register)

        self.kolorowy_kwadracik.setGeometry(0,0,200,200)
        self.login.setGeometry(85,25,100,25)
        self.password.setGeometry(80, 75, 100, 25)
        self.in_login.setGeometry(50,50,100,25)
        self.in_password.setGeometry(50, 100, 100, 25)
        self.check_pass.setGeometry(0, 150, 100, 50)
        self.register.setGeometry(100,150,100,50)

        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()

    def Check_Login(self):
        s = socket(AF_INET, SOCK_STREAM)
        s.connect(("localhost", 8888))
        s.send(str(["log", self.in_login.text(), self.in_password.text()]).encode())
        data = s.recv(1024)
        if (data.decode() == "OK"):
            # s.close()
            print("login")
            self.close()
        else:
            self.in_login.setText("")
            self.in_password.setText("")
            QMessageBox.warning(self, "Error", "Zly login lub haslo", QMessageBox.Ok)
    def Register(self):
        pass
if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())