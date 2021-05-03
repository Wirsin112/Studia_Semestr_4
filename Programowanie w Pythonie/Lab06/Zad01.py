import sys

from PyQt5 import Qt
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QGridLayout, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtWidgets import *


class Main(QWidget):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setup()

    def setup(self):
        self.etykieta = QLabel("Witaj w menu", self)
        self.wejscie = QLineEdit()
        self.wynik = QLineEdit()
        self.wynik.readonly = True
        self.wynik.setToolTip("Tu wynik")
        self.button1 = QPushButton("Gracz vs Gracz", self)
        self.button1.clicked.connect(self.GraczVsGracz)
        self.button2 = QPushButton("Komputer vs Gracz")
        self.button2.clicked.connect(self.GraczVsKomputer)
        self.uklad = QVBoxLayout()
        self.uklad.setAlignment(self.button1, Qt.AlignTop)
        self.uklad.setAlignment(self.button2, Qt.AlignTop)
        self.uklad.setAlignment(self.etykieta, Qt.AlignTop)
        self.uklad.addWidget(self.etykieta, 0, 0)
        # uklad.addWidget(self.wejscie,3,0)
        # uklad.addWidget(self.wynik,1,0,1,2)
        self.uklad.addWidget(self.button1, 1, 0, 1, 3)
        self.uklad.addWidget(self.button2, 2, 0, 1, 3)

        self.setLayout(self.uklad)
        self.setGeometry(20, 20, 300, 100)
        self.setWindowTitle("Menu")
        self.show()

    def GraczVsGracz(self):
        self.uklad.removeWidget(self.button1)
        self.button1.deleteLater()
        del self.button1
        self.uklad.removeWidget(self.etykieta)
        self.etykieta.deleteLater()
        del self.etykieta
        self.uklad.removeWidget(self.button2)
        self.button2.deleteLater()
        del self.button2

        # b1.setStyleSheet("background-image : url(czerwona_bierka.png); border: none;")
        # tab = [[],[],[],[],[],[],[],[]]
        # for i in range(8):
        #     for j in range(8):
        #         tab[i].append(QPushButton("1", self))
        #         print(1)
        #         # if(i < 4 and j % 2 == 0):
        #         #     tab[i][j].setStyleSheet("background-image : url(white.png); border: none;")

        b1 = QPushButton("1", self)
        b2 = QPushButton("2", self)
        b2.clicked.connect(self.akcja)
        b3 = QPushButton("3", self)
        b4 = QPushButton("4", self)
        self.uklad.setColumnMinimumWidth(0,40)
        self.uklad.setRowMinimumHeight(0,40)
        self.uklad.addWidget(b1, 0, 0)
        self.uklad.addWidget(b2, 1,1)
        self.uklad.addWidget(b3, 2,2)
        self.uklad.addWidget(b4, 3,3)
        self.setLayout(self.uklad)
        self.setGeometry(200, 200, 300, 100)
        self.setWindowTitle("GraczVsGracz")
        self.show()

    def GraczVsKomputer(self):
        self.setLayout(self.uklad)
        self.setGeometry(200, 200, 300, 100)
        self.setWindowTitle("GraczVsKomputer")
        self.show()

    def akcja(self):
        print(1)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    okno = Main()
    sys.exit(app.exec_())
