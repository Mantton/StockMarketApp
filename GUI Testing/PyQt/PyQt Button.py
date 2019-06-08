from PyQt5.QtWidgets import *
import sys
from PyQt5 import QtGui
from PyQt5.QtCore import QRect
from PyQt5 import QtCore


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        title = " PYQT 5 "
        left = 500
        top = 200
        width = 300
        height = 250
        iconname = "icon.jpg"

        self.setWindowTitle(title)
        self.setWindowIcon(QtGui.QIcon(iconname))
        self.setGeometry(left, top, width, height)
        self.UiComponents()
        self.show()

    def UiComponents(self):
        button = QPushButton("Click Me ", self)
        button.move(50, 50)
        button.setGeometry(QRect(100, 100, 111, 40))
        button.setIcon(QtGui.QIcon('icon.jpg'))
        button.setIconSize(QtCore.QSize(40, 40))
        button.setToolTip("Click if you love rosie")
        # button.setToolTipDuration(2000)


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
