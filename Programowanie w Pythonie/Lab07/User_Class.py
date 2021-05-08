from datetime import datetime
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QWidget, \
    QListWidgetItem, QScrollBar, QListWidget, QLineEdit
import sys
from socket import *


def Get_Server_Time():
    return datetime.now().strftime("%H:%M:%S")


class Wiadomosc(QListWidgetItem):
    def __init__(self,parent,user_name,date,messenge):
        if user_name == parent.user:
            super().__init__("Ja:\n\t"+messenge + "\n")
            self.setBackground(Qt.cyan)
        else:
            super().__init__(user_name + ":\n\t" + messenge + "\n")
        self.user_name = user_name
        self.date = date
        self.messenge = messenge

class Window(QWidget):
    def __init__(self,chat_name,user_name):
        super().__init__()
        self.setMouseTracking(True)
        self.title = chat_name
        self.user = user_name
        self.top = 100
        self.left = 100
        self.width = 1000
        self.height = 800
        self.Init_Window()
        self.Init_rest()
    def Init_Window(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)

    def Init_rest(self):
        self.list_widget = QListWidget(self)
        self.list_widget.setGeometry(25, 25, 950, 650)
        self.list_widget.itemClicked.connect(self.Show_Date)

        scroll_bar = QScrollBar(self)
        scroll_bar.setStyleSheet("background : Grey;")
        self.list_widget.setVerticalScrollBar(scroll_bar)
        self.label = QLabel("Data wyslania: ",self)
        self.label.setGeometry(850,660,200,50)
        self.wejscie = QLineEdit(self)
        self.wejscie.setGeometry(200,685,600,50)
        wyslij = QPushButton("Wyslij", self)
        wyslij.clicked.connect(self.siema)
        wyslij.setGeometry(400, 740, 200, 50)
        self.show()
    def Show_Date(self,item):
        self.label.setText("Data wyslania: "+item.date)
    def siema(self):
        if self.wejscie.text():
            try:
                s = socket(AF_INET, SOCK_STREAM)
                s.connect(("localhost", 8888))
                s.send(str(["SND",self.user,self.wejscie.text(),Get_Server_Time()]).encode())
                data = s.recv(1024)
                # item = Wiadomosc(self, self.user, Get_Server_Time(), self.wejscie.text())
                # self.list_widget.addItem(item)
            except(error):
                print(error)
    def Recive_Messenge(self):
        pass
if __name__ == "__main__":
    App = QApplication(sys.argv)
    win = Window("siema","siema2")
    sys.exit(App.exec())
