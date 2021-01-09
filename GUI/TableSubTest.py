from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QCheckBox, QHBoxLayout, QTableWidgetItem
from time import sleep
from PyQt5.QtCore import Qt

from GUI.TableSub import Ui_MainWindow  # importing our generated file
from DB_SQLAlchemy import getData
import sys


class MyWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.fillTable)
        self.ui.ClearButton.clicked.connect(self.clearTable)

    def clearTable(self):
        for i in range(self.ui.tableWidget.rowCount(), -1, -1):
            self.ui.tableWidget.removeRow(i)

    def fillTable(self):
        self.clearTable()
        for r in getData('..\Vocabulary.db'):
            rowPosition = self.ui.tableWidget.rowCount()

            self.ui.tableWidget.insertRow(rowPosition)
            # self.ui.tableWidget.setCellWidget(rowPosition, 0, widget)
            self.ui.tableWidget.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(r.Word))
            self.ui.tableWidget.setItem(rowPosition, 2, QtWidgets.QTableWidgetItem(r.Translate))

        # print(self.ui.tableWidget.rowCount())

        for row in range(self.ui.tableWidget.rowCount()):
            widget = QWidget()
            checkbox = QCheckBox()
            checkbox.setCheckState(Qt.Unchecked)
            layoutH = QHBoxLayout(widget)
            layoutH.addWidget(checkbox)
            layoutH.setAlignment(Qt.AlignCenter)
            layoutH.setContentsMargins(0, 0, 0, 0)
            #self.ui.tableWidget.setCellWidget(row, 0, widget)
            self.ui.tableWidget.setCellWidget(row, 0, widget)

    # Копипаст из примера. Подсчёт установленных чекбоксов
    def ButtonClicked(self):
        checked_list = []
        for i in range(self.table.rowCount()):
            if self.table.cellWidget(i, 0).findChild(type(QCheckBox())).isChecked():
                checked_list.append(self.table.item(i, 1).text())
        print(checked_list)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = MyWindow()
    application.show()
    sys.exit(app.exec())
