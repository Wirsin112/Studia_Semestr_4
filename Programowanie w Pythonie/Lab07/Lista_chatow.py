from _thread import *
import threading
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QWidget, \
    QListWidgetItem, QScrollBar, QListWidget, QLineEdit
import sys
from socket import *
from User_Class import Window, Wiadomosc


def Wait_For_Call(parent):
    s = socket(AF_INET, SOCK_STREAM)
    s.connect(("localhost", 8888))
    answer = str(["CON"])
    s.send(answer.encode())
    while 1:
        try:
            data = s.recv(1024)
            if data.decode():
                if eval(data.decode())[0] == "CAT":
                    print(data.decode())
                    item = Przemiot_Dyskusji(parent, eval(data.decode())[1])
                    parent.list_widget.addItem(item)
                if eval(data.decode())[0] == "MES":
                    for i in parent.lista_chatow:
                        if i.title == eval(data.decode())[4]:
                            print(data.decode())
                            item = Wiadomosc(i, eval(data.decode())[1], eval(data.decode())[3], eval(data.decode())[2])
                            i.list_widget.addItem(item)
        except():
            pass
    s.close()


class Przemiot_Dyskusji(QListWidgetItem):
    def __init__(self, parent, title):
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
        self.Init_Chat_Names()
        x = threading.Thread(target=Wait_For_Call, args=(self,))
        x.start()
        print("out")

    def Wait_Thread(self):
        pass

    def Init_Window(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)

    def Init_rest(self):
        self.list_widget = QListWidget(self)
        self.list_widget.setGeometry(25, 25, 250, 250)
        self.list_widget.itemDoubleClicked.connect(self.Open_Chat_Window)
        scroll_bar = QScrollBar(self)
        scroll_bar.setStyleSheet("background : Grey;")
        self.list_widget.setVerticalScrollBar(scroll_bar)
        self.wejscie = QLineEdit(self)
        self.wejscie.setGeometry(25, 300, 250, 50)
        wyslij = QPushButton("Dodaj chat", self)
        wyslij.clicked.connect(self.siema)
        wyslij.setGeometry(25, 375, 250, 50)
        self.show()

    def Init_Chat_Names(self):
        s = socket(AF_INET, SOCK_STREAM)
        s.connect(("localhost", 8888))
        s.send(str(["GCL", self.title]).encode())
        data = s.recv(1024)
        s.close()
        for i in eval(data.decode()):
            item = Przemiot_Dyskusji(self, i)
            self.list_widget.addItem(item)

    def Open_Chat_Window(self, item):
        item = Window(item.title, self.user)
        self.lista_chatow.append(item)
        print(self.lista_chatow)

    def siema(self):
        if self.wejscie.text() != "":
            print("1")
            s = socket(AF_INET, SOCK_STREAM)
            s.connect(("localhost", 8888))
            s.send(str(["NTA", self.wejscie.text()]).encode())
            s.close()
            self.wejscie.setText("")


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Chat_List("Fan Legi")
    sys.exit(App.exec())
