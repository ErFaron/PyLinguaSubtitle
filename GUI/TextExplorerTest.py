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
        self.ui.pushButton.clicked.connect(self.fillTable)
        self.ui.ClearButton.clicked.connect(self.clear)
        self.fileName = None

    def fillTable(self):
        fileName, _ = QFileDialog.getOpenFileName(filter='Subrip files (*.srt);;All files(*.*)')
        if fileName:
            subs = pysrt.open(fileName)
            self.ui.textEdit.setText(highlightWordsInText(subs, 'Richmond'))

    def clear(self):
        self.ui.textEdit.clear()


def highlightWordsInText(subs, word):
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
