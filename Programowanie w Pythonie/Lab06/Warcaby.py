from IPython.external.qt_for_kernel import QtCore
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout,QLabel
from PyQt5.QtGui import QPainter, QBrush, QPen
from PyQt5.QtCore import Qt
import sys
class kwadrat(QLabel):
    def __init__(self,parent,row,column,color):
        super().__init__(parent)
        self.row = row;
        self.column = column;
        self.color = color
        self.setGeometry(column*100,row*100,100,100)
        self.setStyleSheet(f"background-color: {color}")
        self.show()


class pionek(QLabel):
    def __init__(self,parent,row,column,color):
        super().__init__(parent)
        self.parent = parent
        self.row = row;
        self.column = column;
        self.color = color
        self.setGeometry(column * 100 + 10, row * 100 + 10, 80, 80)
        self.setStyleSheet(f"background-color: {color};border-radius:40px")
        self.show()
    def position(self,row,column):
        self.setGeometry(column * 100 + 10, row * 100 + 10, 80, 80)
        self.row = row
        self.column = column
    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            pos = event.windowPos()
            x = pos.x()
            y = pos.y()
            self.move(x-40,y-40)

    def mouseReleaseEvent(self, event: QtGui.QMouseEvent) -> None:
        pos = event.windowPos()
        x = pos.x()
        y = pos.y()
        x = int(x//100)
        y = int(y//100)
        table = self.parent.tablica
        deltay = self.row - y
        deltax = self.column - x
        d = abs(deltax) == abs(deltay)
        ruch_o_jeden = abs(deltax) == 1
        ruch_o_dwa = abs(deltax) == 2
        if table[y][x].color == "black" and self.parent.pionki[y][x] == None and d and ruch_o_jeden:
            self.parent.pionki[y][x] = self.parent.pionki[self.row][self.column]
            self.parent.pionki[self.row][self.column] = None
            self.position(y,x)
            self.row = y
            self.column = x
        elif table[y][x].color == "black" and self.parent.pionki[y][x] == None and d and ruch_o_dwa and self.parent.pionki[int(y+deltay/2)][int(x+deltax/2)] != None and self.parent.pionki[int(y+deltay/2)][int(x+deltax/2)].color != self.color:
            self.parent.pionki[y][x] = self.parent.pionki[self.row][self.column]
            self.parent.pionki[int(y + deltay / 2)][int(x + deltax / 2)].hide()
            self.parent.pionki[int(y + deltay / 2)][int(x + deltax / 2)] = None
            self.parent.pionki[self.row][self.column] = None
            self.position(y, x)
            self.row = y
            self.column = x
        else:
            self.position(self.row, self.column)


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Drawing Rectangle"
        self.top = 100
        self.left = 100
        self.width = 800
        self.height = 800
        self.InitWindow()
        self.tablica()
        self.pionki()


    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()


    def tablica(self):
        tab = []
        black = False
        for row in range(8):
            tab2 = []
            for column in range(8):
                if black:
                    tab2.append(kwadrat(self,row,column,"black"))
                    black = not black
                else:
                    tab2.append(kwadrat(self, row, column, "white"))
                    black = not black
            black = not black
            tab.append(tab2)
        self.tablica = tab


    def pionki(self):
        tab = []
        for row in range(8):
            tab2 = []
            for column in range(8):
                if row < 3 and self.tablica[row][column].color == "black":
                    tab2.append(pionek(self,row,column,"red"))
                elif row > 4 and self.tablica[row][column].color == "black":
                    tab2.append(pionek(self, row, column, "blue"))
                else:
                    tab2.append(None)
            tab.append(tab2)
        self.pionki = tab
App = QApplication(sys.argv)
window = Window()

sys.exit(App.exec())