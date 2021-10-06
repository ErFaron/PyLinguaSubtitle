from PySide2.QtCore import Qt
from PySide2.QtSql import QSqlTableModel, QSqlDatabase, QSqlQuery
from PySide2.QtWidgets import QFileDialog, QMessageBox, QMainWindow, QApplication, QHeaderView, QTableWidgetItem, \
    QItemDelegate
from PySide2.QtGui import QTextCursor

from Srt_Item import SRTItem
from GUI.MainWindow import Ui_MainWindow  # importing our generated file
from Highlighter import Highlighter
import sys
import os
from CheckBoxDelegate import CheckBoxDelegate
from timeit import timeit


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.open_subtitle_btn.clicked.connect(self.run_open_file_dialog)
        self.ui.HideKnown_Chekbox.clicked.connect(self.filter)
        self.ui.HideTranslated_Chekbox.clicked.connect(self.filter)
        self.model = QSqlTableModel()
        self.highlighter = Highlighter(self.ui.textBrowser.document())
        self.info = dict((k, dict.fromkeys(['All', 'Unknown', 'Known', 'New'], 0)) for k in ['Unique', 'Total'])

    def initialize_model(self):
        self.model.setTable('Stems')
        self.model.setEditStrategy(QSqlTableModel.OnFieldChange)
        self.model.select()
        query = QSqlQuery()
        query.exec_(f'DELETE FROM Stems')
        for r in self.srt_item.get_actual_table():
            str_to_make = (f'insert into Stems values('
                           f'{r.Known},'
                           f'"{r.Word}",'
                           f'"{r.Stem}",'
                           f'"{r.Translate}",'
                           f'{r.Amount},'
                           f'{r.Meeting})')
            query.exec_(str_to_make)
        self.ui.TranslationTable.setModel(self.model)
        self.fill_tables()

    def run_open_file_dialog(self):
        file_name, _ = QFileDialog.getOpenFileName(filter='Subrip files (*.srt);;All files(*.*)')
        self.open_subtitle(file_name)
        self.setWindowTitle(f"PyLinguaSubtitle - {os.path.basename(file_name)}")

    def open_subtitle(self, file_name):
        if file_name != '':
            self.srt_item = SRTItem(file_name)
            self.initialize_model()
            self.ui.textBrowser.setText(self.srt_item.subs_text_full)

    def update_info(self):
        q = QSqlQuery()

        def get_info(string):
            q.exec_(string)
            q.first()
            result = q.value(0)
            return result

        self.info['Unique']['All'] = get_info('SELECT COUNT(*) FROM Stems')
        self.info['Total']['All'] = get_info('SELECT SUM(Amount) FROM Stems')
        self.info['Unique']['Known'] = get_info('SELECT COUNT(*) FROM Stems WHERE Known=1')
        self.info['Total']['Known'] = get_info('SELECT SUM(Amount) FROM Stems WHERE Known=1')
        self.info['Unique']['Unknown'] = get_info('SELECT COUNT(*) FROM Stems WHERE Known=0')
        self.info['Total']['Unknown'] = get_info('SELECT SUM(Amount) FROM Stems WHERE Known=0')
        self.info['Unique']['New'] = get_info('SELECT COUNT(*) FROM Stems WHERE Meeting=0')
        self.info['Total']['New'] = get_info('SELECT SUM(Amount) FROM Stems WHERE Meeting=0')

    def update_info_table(self):
        self.update_info()

        self.ui.infoTable.item(0, 1).setData(Qt.EditRole, self.info['Unique']['All'])
        self.ui.infoTable.item(0, 2).setData(Qt.EditRole, self.info['Total']['All'])

        self.ui.infoTable.item(1, 1).setData(Qt.EditRole, self.info['Unique']['Unknown'])
        self.ui.infoTable.item(1, 2).setData(Qt.EditRole, self.info['Total']['Unknown'])

        self.ui.infoTable.item(2, 1).setData(Qt.EditRole, self.info['Unique']['Known'])
        self.ui.infoTable.item(2, 2).setData(Qt.EditRole, self.info['Total']['Known'])

        self.ui.infoTable.item(3, 1).setData(Qt.EditRole, self.info['Unique']['New'])
        self.ui.infoTable.item(3, 2).setData(Qt.EditRole, self.info['Total']['New'])

    def fill_tables(self):
        # fill Translationtable
        self.model.setHeaderData(self.model.fieldIndex('Meeting'), Qt.Horizontal, "Mentioned before")
        for i in range(0, 5):
            self.ui.TranslationTable.horizontalHeader().setSectionResizeMode(i, QHeaderView.ResizeToContents)
        self.ui.TranslationTable.horizontalHeader().setSectionResizeMode(3, QHeaderView.Stretch)
        self.ui.TranslationTable.horizontalHeader().setSectionResizeMode(5, QHeaderView.Fixed)
        self.ui.TranslationTable.horizontalHeader().setMinimumSectionSize(50)
        self.ui.TranslationTable.sortByColumn(1, Qt.AscendingOrder)

        self.ui.TranslationTable.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ui.TranslationTable.customContextMenuRequested.connect(self.on_right_click)

        # fill infoTable
        self.update_info()
        for i in range(4):
            for j in range(1, 3):
                self.ui.infoTable.setItem(i, j, QTableWidgetItem())
        self.update_info_table()

        # self.ui.TranslationTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.TranslationTable.setItemDelegate(CustomItemDelegate(self))
        self.ui.TranslationTable.setItemDelegateForColumn(0, CheckBoxDelegate(self))

    def filter(self):
        if self.ui.HideKnown_Chekbox.isChecked():
            if self.ui.HideTranslated_Chekbox.isChecked():
                self.model.setFilter('Known=0 AND Translate=""')
            else:
                self.model.setFilter('Known=0')
        else:
            if self.ui.HideTranslated_Chekbox.isChecked():
                self.model.setFilter('Translate=""')
            else:
                self.model.setFilter('')

    def on_right_click(self, q_point):
        index = self.ui.TranslationTable.indexAt(q_point)
        stem = (self.ui.TranslationTable.model().index(index.row(), 2).data())
        self.highlighter.change_highlighting_rules(self.srt_item.stem_index[stem])
        self.ui.textBrowser.setText(self.srt_item.get_text())
        index = self.srt_item.get_first_index(stem)
        # setTextCursor is too slow
        self.ui.textBrowser.setTextCursor(QTextCursor(self.ui.textBrowser.document().findBlockByLineNumber(index)))


class CustomItemDelegate(QItemDelegate):

    def __init__(self, parent=None):
        QItemDelegate.__init__(self, parent)

    def createEditor(self, parent, option, index):
        if index.column() == 3:
            return QItemDelegate.createEditor(self, parent, option, index)
        return True


def create_connection():
    con = QSqlDatabase.addDatabase('QSQLITE')
    #con.setDatabaseName(':memory:')
    con.setDatabaseName('work.sqlite')
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
        "Known INTEGER NOT NULL DEFAULT 0,"
        "Word VARCHAR NOT NULL,"
        "Stem VARCHAR NOT NULL,"
        "Translate VARCHAR,"
        "Amount INTEGER NOT NULL DEFAULT 0,"
        "Meeting INTEGER NOT NULL DEFAULT 0,"
        "PRIMARY KEY(Stem) )")
    return True


if __name__ == '__main__':
    if not create_connection():
        sys.exit(1)
    app = QApplication([])
    application = MyWindow()
    application.show()
    sys.exit(app.exec_())
