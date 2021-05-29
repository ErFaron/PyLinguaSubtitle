from PyQt5.QtCore import QRegExp, Qt
from PyQt5.QtGui import QSyntaxHighlighter, QTextCharFormat
from PyQt5.QtWidgets import (QApplication, QFileDialog, QMainWindow)

import pysrt
from Highlighter import Highlighter

from GUI.TextExplorerExample import Ui_MainWindow  # importing our generated file
import sys


class MyWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.open_srt_file)
        self.ui.ClearButton.clicked.connect(self.clear)
        self.fileName = None
        self.text = ''
        self.text_array = []
        self.subs = None
        self.highlighter = Highlighter(self.ui.textEdit.document())

    def find_containing_rows(self, word):
        i = 0
        for string in self.text_array:
            if word in string:
                print(string)
                i += 1
        print(i)

    def open_srt_file(self):
        file_name, _ = QFileDialog.getOpenFileName(filter='Subrip files (*.srt);;All files(*.*)')
        if file_name:
            self.subs = pysrt.open(file_name)
            self.generate_text()
            self.clear()
            self.ui.textEdit.setText(self.text)
            self.text_array = self.text.split('\n')
            self.clear()
            self.highlighter.change_highlighting_rules(["\\Carter\\b"])
            self.ui.textEdit.setText(self.text)
            self.jump_to_text('Carter')

            self.find_containing_rows('Carter')
            # print(f'srtCount={self.ui.textEdit.document().lineCount()}')
            # print(f'srtCount={len(self.text_array)}')

    def jump_to_text(self, word):
        self.ui.textEdit.setTextCursor(self.ui.textEdit.document().find(word))

    def clear(self):
        self.ui.textEdit.clear()

    def generate_text(self):
        show = True
        for k in self.subs:
            if show:
                self.text += f'{k.start} --> {k.end}\n'
            self.text += f'{k.text}\n'

if __name__ == '__main__':
    app = QApplication([])
    application = MyWindow()
    application.show()
    sys.exit(app.exec())
