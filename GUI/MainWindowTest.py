from PySide2.QtCore import Qt
from PySide2.QtSql import QSqlTableModel, QSqlDatabase, QSqlQuery
from PySide2.QtWidgets import QFileDialog, QMessageBox, QMainWindow, QApplication, QHeaderView, QTableWidgetItem, \
    QItemDelegate
from PySide2.QtGui import QTextCursor

from Srt_Item import SRTItem
from GUI.MainWindow import Ui_MainWindow  # importing our generated file
from Highlighter import Highlighter
import sys
from CheckBoxDelegate import CheckBoxDelegate


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.open_subtitle_btn.clicked.connect(self.run_open_file_dialog)
        self.model = QSqlTableModel()
        self.highlighter = Highlighter(self.ui.textBrowser.document())

    def run_open_file_dialog(self):
        file_name, _ = QFileDialog.getOpenFileName(filter='Subrip files (*.srt);;All files(*.*)')
        self.open_subtitle(file_name)

    def open_subtitle(self, file_name):
        if file_name != '':
            self.srt_item = SRTItem(file_name)
            self.initialize_model()
            self.ui.textBrowser.setText(self.srt_item.subs_text_full)

    # def clear_table(self):
    #     for i in range(self.ui.TranslationTable.rowCount(), -1, -1):
    #         self.ui.TranslationTable.removeRow(i)

    def initialize_model(self):
        self.model.setTable('Stems')
        self.model.setEditStrategy(QSqlTableModel.OnManualSubmit)
        self.model.select()
        query = QSqlQuery()
        for r in self.srt_item.get_actual_table():
            str_to_make = (f'insert into Stems values('
                           f'{r.Known},'
                           f'"{r.Word}",'
                           f'"{r.Stem}",'
                           f'"{r.Translate}",'
                           f'{r.Amount},'
                           f'{r.Meeting})')
            query.exec_(str_to_make)
        # query.exec_('SELECT * from Stems')
        self.ui.TranslationTable.setModel(self.model)
        self.fill_tables()

    def fill_tables(self):
        self.model.setHeaderData(self.model.fieldIndex('Meeting'), Qt.Horizontal, "Mentioned before")
        for i in range(0, 5):
            self.ui.TranslationTable.horizontalHeader().setSectionResizeMode(i, QHeaderView.ResizeToContents)
        self.ui.TranslationTable.horizontalHeader().setSectionResizeMode(3, QHeaderView.Stretch)
        self.ui.TranslationTable.horizontalHeader().setSectionResizeMode(5, QHeaderView.Fixed)
        self.ui.TranslationTable.horizontalHeader().setMinimumSectionSize(50)
        self.ui.TranslationTable.sortByColumn(1, Qt.AscendingOrder)

        self.ui.TranslationTable.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ui.TranslationTable.customContextMenuRequested.connect(self.on_right_click)

        item = QTableWidgetItem()
        item.setData(Qt.EditRole, self.srt_item.count_unique_words())
        self.ui.infoTable.setItem(0, 1, item)

        item = QTableWidgetItem()
        item.setData(Qt.EditRole, self.srt_item.count_total_words())
        self.ui.infoTable.setItem(0, 2, item)

        # self.ui.TranslationTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.TranslationTable.setItemDelegate(CustomItemDelegate(self))
        self.ui.TranslationTable.setItemDelegateForColumn(0, CheckBoxDelegate(self))

    def on_right_click(self, q_point):
        index = self.ui.TranslationTable.indexAt(q_point)
        # if index.isValid():
        #    print(f'onClick index.row: {index.row()}, index.col: {index.column()}')
        word = (self.ui.TranslationTable.model().index(index.row(), 2).data())
        # print(word)
        # print(self.srt_item.stem_index[word])
        self.highlighter.change_highlighting_rules(self.srt_item.stem_index[word])
        self.ui.textBrowser.setText(self.srt_item.get_text())
        # Scroll to word
        index = self.srt_item.get_first_index(word)
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
