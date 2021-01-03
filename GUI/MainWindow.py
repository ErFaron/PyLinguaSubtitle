from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFileDialog

from GUI.fr import Ui_MainWindow  # importing our generated file
import sys
import pysrt


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # Модификация таблицы перевода
        for i in range(3):
            self.ui.TranslationTable.setColumnWidth(i, 45)
        self.ui.TranslationTable.setColumnWidth(3, 100)
        self.ui.TranslationTable.setColumnWidth(4, 300)
        self.ui.TranslationTable.setColumnWidth(6, 50)
        self.ui.TranslationTable.setColumnWidth(5, 50)
        self.ui.TranslationTable.horizontalHeaderItem(6).setTextAlignment(Qt.AlignLeft)

        self.ui.open_subtitle_btn.clicked.connect(self.openSubtitle)

    def openSubtitle(self):
        fileName, _ = QFileDialog.getOpenFileName(filter='Subrip files (*.srt);;All files(*.*)')
        if fileName is None:
            pass
        else:
            subs = pysrt.open(fileName)
            a = ''
            show = True
            for k in subs:
                if show:
                    a += '<font color="lightgray">' + f'{k.start} --> {k.end}' + '</font><br>'
                a += (k.text.replace('\n', '<br>')).replace('Carter', '<font color="red">Carter</font>') + '<br>'
            self.ui.textEdit.setText(a)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = MyWindow()
    application.show()
    sys.exit(app.exec())
