from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

class GUI(QObject):
    def __init__(self):
        super(GUI, self).__init__()
        self.layout = QVBoxLayout()
        self.initGUI()

    def getLayout(self):
        return self.layout

    def initGUI(self):
        self.listWidget = QListWidget()
        self.listWidget.addItem(QListWidgetItem('item1'))
        self.listWidget.addItem(QListWidgetItem('item2'))
        self.listWidget.itemClicked.connect(self.listwidgetclicked)
        self.layout.addWidget(self.listWidget)

    def listwidgetclicked(self, dupa):
        print('click -> {}'.format(dupa.text()))

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.imagelabel = QLabel()
        layout = QVBoxLayout()
        self.imagelabel.setLayout(layout)
        self.setCentralWidget(self.imagelabel)

        label1 = QLabel('hello, world')
        layout.addWidget(label1)


        self.listWidget = GUI()                        # <--- + self.
        layout.addLayout(self.listWidget.getLayout())  # <--- + self.


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()