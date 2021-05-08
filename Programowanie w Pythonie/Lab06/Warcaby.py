from IPython.external.qt_for_kernel import QtCore
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QMessageBox
import sys


class kwadrat(QLabel):
    def __init__(self, parent, row, column, color):
        super().__init__(parent)
        self.row = row;
        self.column = column;
        self.color = color
        self.setGeometry(column * 100, row * 100, 100, 100)
        self.setStyleSheet(f"background-color: {color}")
        self.show()


class pionek(QLabel):
    def __init__(self, parent, row, column, color):
        super().__init__(parent)
        self.parent = parent
        self.row = row;
        self.column = column;
        self.color = color
        self.setGeometry(column * 100 + 10, row * 100 + 10, 80, 80)
        self.setStyleSheet(f"background-color: {color};border-radius:40px")
        self.show()

    def position(self, row, column):
        self.setGeometry(column * 100 + 10, row * 100 + 10, 80, 80)
        self.row = row
        self.column = column

    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            pos = event.windowPos()
            x = pos.x()
            y = pos.y()
            self.move(x - 40, y - 40)

    def mouseReleaseEvent(self, event: QtGui.QMouseEvent) -> None:
        pos = event.windowPos()
        x = pos.x()
        y = pos.y()
        x = int(x // 100)
        y = int(y // 100)
        table = self.parent.tablica
        deltay = self.row - y
        deltax = self.column - x
        d = abs(deltax) == abs(deltay)
        ruch_o_jeden = abs(deltax) == 1
        ruch_o_dwa = abs(deltax) == 2

        if self.color == "red" and not self.parent.gracz and x < 8 and x > -1 and y < 8 and y > -1:
            if table[y][x].color == "black" and self.parent.pionki[y][x] == None and d and ruch_o_jeden and deltay < 0:
                self.parent.pionki[y][x] = self.parent.pionki[self.row][self.column]
                self.parent.pionki[self.row][self.column] = None
                self.position(y, x)
                self.row = y
                self.column = x
                self.parent.setWindowTitle("Tura Niebieska")
                self.parent.gracz = True
            elif table[y][x].color == "black" and self.parent.pionki[y][x] == None and d and ruch_o_dwa and \
                    self.parent.pionki[int(y + deltay / 2)][int(x + deltax / 2)] != None and \
                    self.parent.pionki[int(y + deltay / 2)][int(x + deltax / 2)].color != self.color:
                self.parent.pionki[y][x] = self.parent.pionki[self.row][self.column]
                self.parent.pionki[int(y + deltay / 2)][int(x + deltax / 2)].hide()
                self.parent.pionki[int(y + deltay / 2)][int(x + deltax / 2)] = None
                self.parent.pionki[self.row][self.column] = None
                self.position(y, x)
                self.row = y
                self.column = x
                self.parent.setWindowTitle("Tura Niebieska")
                self.parent.gracz = True
            else:
                self.position(self.row, self.column)
        elif self.color == "blue" and self.parent.gracz and x < 8 and x > -1 and y < 8 and y > -1:
            if table[y][x].color == "black" and self.parent.pionki[y][x] == None and d and ruch_o_jeden and deltay > 0:
                self.parent.pionki[y][x] = self.parent.pionki[self.row][self.column]
                self.parent.pionki[self.row][self.column] = None
                self.position(y, x)
                self.row = y
                self.column = x
                self.parent.setWindowTitle("Tura Czerwony")
                self.parent.gracz = False
            elif table[y][x].color == "black" and self.parent.pionki[y][x] == None and d and ruch_o_dwa and \
                    self.parent.pionki[int(y + deltay / 2)][int(x + deltax / 2)] != None and \
                    self.parent.pionki[int(y + deltay / 2)][int(x + deltax / 2)].color != self.color:
                self.parent.pionki[y][x] = self.parent.pionki[self.row][self.column]
                self.parent.pionki[int(y + deltay / 2)][int(x + deltax / 2)].hide()
                self.parent.pionki[int(y + deltay / 2)][int(x + deltax / 2)] = None
                self.parent.pionki[self.row][self.column] = None
                self.position(y, x)
                self.row = y
                self.column = x
                self.parent.setWindowTitle("Tura Czerwony")
                self.parent.gracz = False
            else:
                self.position(self.row, self.column)
        else:
            self.position(self.row, self.column)
        czerwony_win = False
        niebieski_win = False
        for i in range(len(self.parent.pionki)):
            for j in range(len(self.parent.pionki)):
                if self.parent.pionki[i][j] == None:
                    pass
                elif self.parent.pionki[i][j].color == "red":
                    czerwony_win = True
                    break
            if czerwony_win:
                break

        for i in range(len(self.parent.pionki)):
            for j in range(len(self.parent.pionki)):
                if self.parent.pionki[i][j] == None:
                    pass
                elif self.parent.pionki[i][j].color == "blue":
                    niebieski_win = True
                    break
            if niebieski_win:
                break

        if not czerwony_win:
            QMessageBox.warning(self.parent, "Wygrany", "Niebieski gracz wygral", QMessageBox.Ok)
        if not niebieski_win:
            QMessageBox.warning(self.parent, "Wygrany", "Czerwony gracz wygral", QMessageBox.Ok)


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.gracz = True
        self.title = "Tura Niebieski"
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
                    tab2.append(kwadrat(self, row, column, "black"))
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
                    tab2.append(pionek(self, row, column, "red"))
                elif row > 4 and self.tablica[row][column].color == "black":
                    tab2.append(pionek(self, row, column, "blue"))
                else:
                    tab2.append(None)
            tab.append(tab2)
        self.pionki = tab


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    window2 = Window()
    sys.exit(App.exec())
