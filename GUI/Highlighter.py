from PySide2.QtCore import Qt, QRegExp
from PySide2.QtGui import QSyntaxHighlighter, QTextCharFormat


class Highlighter(QSyntaxHighlighter):
    def __init__(self, parent=None):
        super(Highlighter, self).__init__(parent)
        keyword_format = QTextCharFormat()
        keyword_format.setForeground(Qt.red)
        keyword_patterns = []
        self.highlightingRules = [(QRegExp(pattern), keyword_format) for pattern in keyword_patterns]

        time_format = QTextCharFormat()
        time_format.setForeground(Qt.darkGray)
        self.highlightingRules.append((QRegExp("^.+--\>.+$"), time_format))

    def change_highlighting_rules(self, words):
        keyword_format = QTextCharFormat()
        keyword_format.setForeground(Qt.red)
        keyword_patterns = words
        self.highlightingRules = [(QRegExp(pattern), keyword_format) for pattern in keyword_patterns]

        time_format = QTextCharFormat()
        time_format.setForeground(Qt.darkGray)
        self.highlightingRules.append((QRegExp("^.+--\>.+$"), time_format))

    def highlightBlock(self, text):
        for pattern, format in self.highlightingRules:
            expression = QRegExp(pattern)
            index = expression.indexIn(text)
            while index >= 0:
                length = expression.matchedLength()
                self.setFormat(index, length, format)
                index = expression.indexIn(text, index + length)
        self.setCurrentBlockState(0)
