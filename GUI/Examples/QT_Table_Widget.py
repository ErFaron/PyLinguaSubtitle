import sys

from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QTableWidget, QVBoxLayout
from PyQt5.QtCore import Qt


class Widget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.widget_layout = QVBoxLayout()
        self.table_widget = QTableWidget(101, 1)
        self.table_widget.setSortingEnabled(True)

        self.widget_layout.addWidget(self.table_widget)
        self.setLayout(self.widget_layout)

        for num in range(101):
            item = QTableWidgetItem()
            item.setData(Qt.EditRole, num)
            self.table_widget.setItem(num, 0, item)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec_())
