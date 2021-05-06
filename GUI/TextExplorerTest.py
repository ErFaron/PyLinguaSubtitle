from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QFileDialog
import pysrt

from GUI.TextExplorerExample import Ui_MainWindow  # importing our generated file
import sys


class MyWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.fill_textfield)
        self.ui.ClearButton.clicked.connect(self.clear)
        self.fileName = None

    def fill_textfield(self):
        file_name, _ = QFileDialog.getOpenFileName(filter='Subrip files (*.srt);;All files(*.*)')
        if file_name:
            subs = pysrt.open(file_name)
            self.ui.textEdit.setText(highlight_words(subs, 'Crane'))

    def clear(self):
        self.ui.textEdit.clear()


def highlight_words(subs, word):
    a = ''
    show = True
    for k in subs:
        if show:
            a += '<font color="gray">' + f'{k.start} --> {k.end}' + '</font><br>'
        a += (k.text.replace('\n', '<br>')).replace(word, '<font color="red">' + word + '</font>') + '<br>'
    return a


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = MyWindow()
    application.show()
    sys.exit(app.exec())
