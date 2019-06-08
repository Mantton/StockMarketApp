from PyQt5.QtWidgets import *
import sys
from PyQt5 import QtGui
from PyQt5.QtCore import QRect
from PyQt5 import QtCore


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        title = "PYQT Events and Signals "
        left = 500
        top = 200
        width = 300
        height = 250
        iconname = "icon.jpg"

        self.setWindowTitle(title)
        self.setWindowIcon(QtGui.QIcon(iconname))
        self.setGeometry(left, top, width, height)
        self.CreateButton()


        self.show()
    def CreateButton(self):
        button = QPushButton("Close App", self)
        button.move(50, 50)
        button.setGeometry(QRect(100, 100, 120, 40))
        button.setIcon(QtGui.QIcon('button1.jpg'))
        button.setIconSize(QtCore.QSize(60, 60))
        button.setToolTip("Click to close the app")
        # button.setToolTipDuration(2000)
        button.clicked.connect(self.buttonclick) # this function is not defined but works

    def buttonclick(self):
        sys.exit()





if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
