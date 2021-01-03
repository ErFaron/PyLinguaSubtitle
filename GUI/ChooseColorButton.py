import sys
from pprint import pprint
from PyQt5.QtWidgets import (QWidget, QPushButton, QFrame, QColorDialog, QApplication)
from PyQt5.QtGui import QColor
from time import sleep


class QColorPickButton(QWidget):
    bwidth = 70
    bheight = 25

    def __init__(self, parent=None):
        super().__init__(parent)
        selected_color = QColor(0, 0, 255)
        self.b1 = QPushButton(self)
        self.b1.clicked.connect(self.showColorDialog)
        self.b1.setStyleSheet("QWidget { background-color: %s}" % selected_color.name())
        self.setSize(self.bwidth, self.bheight)

    def showColorDialog(self):
        selected_color = QColorDialog.getColor()
        if selected_color.isValid():
            self.b1.setStyleSheet("QWidget { background-color: %s}" % selected_color.name())
            print(selected_color.name())

    def setPosition(self, x, y):
        self.setGeometry(x, y, x + self.bwidth, y + self.bheight)

    def setSize(self, x, y):
        self.b1.setGeometry(0, 0, x, y)

if __name__ == '__main__':
    class TutorialWindow(QWidget):
        def __init__(self):
            super().__init__()
            self.tw = QColorPickButton(self)
            self.tw.setPosition(0, 0)
            self.tw2 = QColorPickButton(self)
            self.tw2.setPosition(50, 25)
            self.tw3 = QColorPickButton(self)
            self.tw3.setPosition(0, 50)
            self.setGeometry(0, 0, 100, 75)
    app = QApplication(sys.argv)
    pprint("input parameters = " + str(sys.argv))
    tutorial_window = TutorialWindow()
    tutorial_window.show()
    sys.exit(app.exec_())
