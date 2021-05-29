from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import Qt, QRegExp
from PyQt5.QtGui import QTextCharFormat, QSyntaxHighlighter
from PyQt5.QtWidgets import QFileDialog, QTableWidgetItem
from Srt_Item import SRTItem

from GUI.fr import Ui_MainWindow  # importing our generated file
from Highlighter import Highlighter
import sys
import pysrt


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # Модификация таблицы перевода
        self.ui.TranslationTable.setColumnWidth(0, 45)
        self.ui.TranslationTable.setColumnWidth(1, 250)
        self.ui.TranslationTable.setColumnWidth(2, 250)
        self.ui.TranslationTable.setColumnWidth(3, 60)
        self.ui.TranslationTable.setColumnWidth(4, 45)
        # self.ui.TranslationTable.horizontalHeaderItem(5).setTextAlignment(Qt.AlignLeft)
        self.ui.open_subtitle_btn.clicked.connect(self.openSubtitle)
        self.highlighter = Highlighter(self.ui.textBrowser.document())

    def openSubtitle(self):
        file_name, _ = QFileDialog.getOpenFileName(filter='Subrip files (*.srt);;All files(*.*)')
        if file_name is None:
            pass
        else:
            self.srtitem = SRTItem(file_name)
            self.ui.textBrowser.setText(self.srtitem.generate_text())
            self.fill_table()

    def clear_table(self):
        for i in range(self.ui.TranslationTable.rowCount(), -1, -1):
            self.ui.TranslationTable.removeRow(i)

    def fill_table(self):
        self.clear_table()
        for r in self.srtitem.get_actual_table():
            # print(f"{r.Word}-{r.Amount}")
            rowPosition = self.ui.TranslationTable.rowCount()
            self.ui.TranslationTable.insertRow(rowPosition)
            self.ui.TranslationTable.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(r.Word))
            # self.ui.TranslationTable.setItem(rowPosition, 2, QtWidgets.QTableWidgetItem(r.Stem))
            self.ui.TranslationTable.setItem(rowPosition, 2, QtWidgets.QTableWidgetItem(r.Translate))
            item = QTableWidgetItem()
            item.setData(Qt.EditRole, r.Amount)
            self.ui.TranslationTable.setItem(rowPosition, 3, item)
            item = QTableWidgetItem()
            item.setData(Qt.EditRole, r.Meeting)
            self.ui.TranslationTable.setItem(rowPosition, 4, item)
            #
            item = QTableWidgetItem()
            item.setData(Qt.EditRole, r.Known)
            self.ui.TranslationTable.setItem(rowPosition, 0, item)
            if r.Known == 1:
                for i in range(0, 5):
                    self.ui.TranslationTable.item(rowPosition, i).setBackground(QtGui.QColor('lightgrey'))


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = MyWindow()
    application.show()
    sys.exit(app.exec())
