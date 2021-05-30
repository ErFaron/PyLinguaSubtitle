from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import Qt, QRegExp
from PyQt5.QtGui import QTextCharFormat, QSyntaxHighlighter
from PyQt5.QtSql import QSqlTableModel, QSqlDatabase, QSqlQuery
from PyQt5.QtWidgets import QFileDialog, QTableWidgetItem, QTableView, QMessageBox
from Srt_Item import SRTItem

from GUI.fr_QtableView import Ui_MainWindow  # importing our generated file
from Highlighter import Highlighter
import sys
import pysrt


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.open_subtitle_btn.clicked.connect(self.openSubtitle)
        self.highlighter = Highlighter(self.ui.textBrowser.document())
        self.model = QSqlTableModel()

    def openSubtitle(self):
        file_name, _ = QFileDialog.getOpenFileName(filter='Subrip files (*.srt);;All files(*.*)')
        if file_name is None:
            pass
        else:
            self.srtitem = SRTItem(file_name)
            self.ui.textBrowser.setText(self.srtitem.generate_text())
            self.initializeModel()

    # def clear_table(self):
    #     for i in range(self.ui.TranslationTable.rowCount(), -1, -1):
    #         self.ui.TranslationTable.removeRow(i)

    def initializeModel(self):
        self.model.setTable('Stems')
        self.model.setEditStrategy(QSqlTableModel.OnManualSubmit)
        self.model.select()
        query = QSqlQuery()
        for r in self.srtitem.get_actual_table():
            str_to_make = (f'insert into Stems values('
                           f'"{r.Word}",'
                           f'"{r.Stem}",'
                           f'"{r.Translate}",'
                           f'{r.Meeting},'
                           f'{r.Known},'
                           f'{r.Amount})')
            query.exec_(str_to_make)
        #query.exec_('SELECT * from Stems')
        self.ui.TranslationTable.setModel(self.model)


def createConnection():
    con = QSqlDatabase.addDatabase('QSQLITE')
    con.setDatabaseName(':memory:')
    if not con.open():
        QMessageBox.critical(None, "Cannot open database",
                             "Unable to establish a database connection.\n"
                             "This example needs SQLite support. Please read the Qt SQL "
                             "driver documentation for information how to build it.\n\n"
                             "Click Cancel to exit.",
                             QMessageBox.Cancel)
        return False
    query = QSqlQuery()
    query.exec_(
        "CREATE TABLE Stems ("
        "Word VARCHAR NOT NULL,"
        "Stem VARCHAR NOT NULL,"
        "Translate VARCHAR,"
        "Meeting INTEGER NOT NULL DEFAULT 0,"
        "Known INTEGER NOT NULL DEFAULT 0,"
        "Amount INTEGER NOT NULL DEFAULT 0,"
        "PRIMARY KEY(Stem) )")
    return True


if __name__ == '__main__':
    if not createConnection():
        sys.exit(1)
    app = QtWidgets.QApplication([])
    application = MyWindow()
    application.show()
    sys.exit(app.exec())
