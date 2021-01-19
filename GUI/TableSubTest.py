from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QCheckBox, QHBoxLayout, QTableWidgetItem
from PyQt5.QtCore import Qt

from GUI.TableSub import Ui_MainWindow  # importing our generated file
from SRTReader import SRT_Table_item
from sqlalchemy import select
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
        srt_table_item = SRT_Table_item('Carter.srt')
        srt_table = srt_table_item.srt_table
        stmt = select([srt_table]).select_from(srt_table).order_by(srt_table.c.word)
        result = srt_table_item.engine.execute(stmt).fetchall()
        for r in result:
            print(f"{r.word}-{r.amount}")
            rowPosition = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(rowPosition)
            self.ui.tableWidget.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(r.word))
            self.ui.tableWidget.setItem(rowPosition, 2, QtWidgets.QTableWidgetItem(r.stem))
            self.ui.tableWidget.setItem(rowPosition, 3, QtWidgets.QTableWidgetItem(r.word))
            #int correct sort
            item = QTableWidgetItem()
            item.setData(Qt.EditRole, r.amount)
            self.ui.tableWidget.setItem(rowPosition, 4, item)

        # print(self.ui.tableWidget.rowCount())

        for row in range(self.ui.tableWidget.rowCount()):
            widget = QWidget()
            checkbox = QCheckBox()
            checkbox.setCheckState(Qt.Unchecked)
            layoutH = QHBoxLayout(widget)
            layoutH.addWidget(checkbox)
            layoutH.setAlignment(Qt.AlignCenter)
            layoutH.setContentsMargins(0, 0, 0, 0)
            # self.ui.tableWidget.setCellWidget(row, 0, widget)
            self.ui.tableWidget.setCellWidget(row, 0, widget)

        for i in range(1,3):
            self.ui.tableWidget.item(0, i).setBackground(QtGui.QColor('lightgrey'))
        self.ui.tableWidget.cellWidget(0, 0).setStyleSheet('background-color: lightgrey')

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
