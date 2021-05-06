#GUI Слово -перевод
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow
from time import sleep
from PyQt5.QtCore import Qt

from GUI.TableExample import Ui_MainWindow  # importing our generated file
from DictTable import DictTableItem
import sys


class MyWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.fillTable)
        self.ui.ClearButton.clicked.connect(self.clearTable)
        self.dict_table_item = DictTableItem()

    def clearTable(self):
        for i in range(self.ui.tableWidget.rowCount(), -1, -1):
            self.ui.tableWidget.removeRow(i)

    def fillTable(self):
        self.clearTable()
        for r in self.dict_table_item.get_data():
            if r.Word == r.Stem:
                print(f"{r.Word} - {r.Translate}")
            else:
                print(f"{r.Word}({r.Stem}) - {r.Translate}")
            row_position = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(row_position)
            self.ui.tableWidget.setItem(row_position, 0, QtWidgets.QTableWidgetItem(r.Word))
            self.ui.tableWidget.setItem(row_position, 1, QtWidgets.QTableWidgetItem(r.Translate))


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = MyWindow()
    application.show()
    sys.exit(app.exec())
