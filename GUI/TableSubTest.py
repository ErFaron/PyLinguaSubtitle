from PySide2 import QtGui, QtWidgets
from PySide2.QtWidgets import QMainWindow, QWidget, QCheckBox, QHBoxLayout, QTableWidgetItem, QFileDialog
from PySide2.QtCore import Qt

from GUI.TableSub import Ui_MainWindow  # importing our generated file
from Srt_Item import SRTItem
from sqlalchemy import select
import sys


class MyWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.fill_table)
        self.ui.ClearButton.clicked.connect(self.clear_table)

    def clear_table(self):
        for i in range(self.ui.tableWidget.rowCount(), -1, -1):
            self.ui.tableWidget.removeRow(i)

    def fill_table(self):
        file_name, _ = QFileDialog.getOpenFileName(filter='Subrip files (*.srt);;All files(*.*)')
        if file_name:
            self.clear_table()
            srt_table_item = SRTItem(file_name)
            for r in srt_table_item.get_actual_table():
                # print(f"{r.Word}-{r.Amount}")
                rowPosition = self.ui.tableWidget.rowCount()
                self.ui.tableWidget.insertRow(rowPosition)
                self.ui.tableWidget.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(r.Word))
                self.ui.tableWidget.setItem(rowPosition, 2, QtWidgets.QTableWidgetItem(r.Stem))
                self.ui.tableWidget.setItem(rowPosition, 3, QtWidgets.QTableWidgetItem(r.Translate))
                item = QTableWidgetItem()
                item.setData(Qt.EditRole, r.Amount)
                self.ui.tableWidget.setItem(rowPosition, 4, item)
                item = QTableWidgetItem()
                item.setData(Qt.EditRole, r.Meeting)
                self.ui.tableWidget.setItem(rowPosition, 5, item)
                item = QTableWidgetItem()
                item.setData(Qt.EditRole, r.Known)
                self.ui.tableWidget.setItem(rowPosition, 0, item)

                if r.Known==1:
                    for i in range(0, 6):
                        self.ui.tableWidget.item(rowPosition, i).setBackground(QtGui.QColor('lightgrey'))
                        #self.ui.tableWidget.cellWidget(0, 0).setStyleSheet('background-color: lightgrey')

                #             for row in range(self.ui.tableWidget.rowCount()):
                # widget = QWidget()
                #     checkbox = QCheckBox()
                #     checkbox.setCheckState(Qt.Unchecked)
                #     layoutH = QHBoxLayout(widget)
                #     layoutH.addWidget(checkbox)
                #     layoutH.setAlignment(Qt.AlignCenter)
                #     layoutH.setContentsMargins(0, 0, 0, 0)
                # self.ui.tableWidget.setCellWidget(rowPosition, 0, widget)

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = MyWindow()
    application.show()
    sys.exit(app.exec_())
