from datetime import datetime
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QWidget, \
    QListWidgetItem, QScrollBar, QListWidget, QLineEdit
import sys
from socket import *
from User_Class import Window


def Wait_For_Call():
    s = socket(AF_INET, SOCK_STREAM)
    s.connect(("localhost", 8888))
    while 1:
        if s.recv(1024):
            data = s.recv(1024)
    s.close()


class Przemiot_Dyskusji(QListWidgetItem):
    def __init__(self,parent,title):
        super().__init__(title)
        self.title = title
        self.parent = parent
        self.setFont(QFont('Arial', 25))

class Chat_List(QWidget):
    def __init__(self, user_name):
        super().__init__()
        self.title = "Wybor Chatu"
        self.setMouseTracking(True)
        self.user = user_name
        self.top = 100
        self.left = 100
        self.width = 300
        self.height = 450
        self.Init_Window()
        self.Init_rest()
        self.lista_chatow = []

    def Wait_Thread(self):
        pass
    def Init_Window(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)

    def Init_rest(self):
        self.list_widget = QListWidget(self)
        self.list_widget.setGeometry(25, 25, 250, 250)
        self.list_widget.itemDoubleClicked.connect(self.Open_Chat_Window)
        for i in range(3):
            if i == 1 or i == 2:
                item = Przemiot_Dyskusji(self,"Jan_zamoj")
                self.list_widget.addItem(item)
            item = Przemiot_Dyskusji(self, "Bob")
            self.list_widget.addItem(item)

        scroll_bar = QScrollBar(self)
        scroll_bar.setStyleSheet("background : Grey;")
        self.list_widget.setVerticalScrollBar(scroll_bar)
        self.wejscie = QLineEdit(self)
        self.wejscie.setGeometry(25,300,250,50)
        wyslij = QPushButton("Dodaj chat", self)
        wyslij.clicked.connect(self.siema)
        wyslij.setGeometry(25, 375, 250, 50)
        self.show()
    def Open_Chat_Window(self,item):
        item = Window(item.title,self.user)
        self.lista_chatow.append(item)
        print(self.lista_chatow)
    def siema(self):
        item = Przemiot_Dyskusji(self,self.wejscie.text())
        self.list_widget.addItem(item)
        self.wejscie.setText("")
        if self.lista_chatow[0].isHidden():
            print("hidden")
if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Chat_List("Fan Legi")
    sys.exit(App.exec())



