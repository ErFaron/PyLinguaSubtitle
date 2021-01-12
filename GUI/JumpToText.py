import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class GoToDialog(QtWidgets.QDialog):
    gotoSignal = QtCore.pyqtSignal(int)

    def __init__(self, text_edit, parent=None):
        super().__init__(parent)

        self.m_text_edit = text_edit

        self.spinbox = QtWidgets.QSpinBox(minimum=1)
        self.m_text_edit.document().blockCountChanged.connect(self.spinbox.setMaximum)
        self.spinbox.setMaximum(self.m_text_edit.document().blockCount())

        self.buttonGoto = QtWidgets.QPushButton("Go to...")
        self.buttonGoto.clicked.connect(self.onAccepted)
        self.buttonCancel = QtWidgets.QPushButton("Cancel")
        self.buttonCancel.clicked.connect(self.reject)

        vlay = QtWidgets.QVBoxLayout(self)
        hlay = QtWidgets.QHBoxLayout()
        hlay.addWidget(self.buttonGoto)
        hlay.addWidget(self.buttonCancel)
        vlay.addWidget(QtWidgets.QLabel("Go to..."))
        vlay.addWidget(self.spinbox)
        vlay.addLayout(hlay)
        self.setFixedSize(300, 100)

    def onAccepted(self):
        n = self.spinbox.value() - 1
        if 0 <= n < self.m_text_edit.document().blockCount():
            cursor = QtGui.QTextCursor(
                self.m_text_edit.document().findBlockByLineNumber(n)
            )
            self.m_text_edit.setTextCursor(cursor)
        self.reject()


class Writter(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.text_edit = QtWidgets.QTextEdit()
        self.setCentralWidget(self.text_edit)

        self.goto_dialog = GoToDialog(self.text_edit, self)

        menubar = self.menuBar()
        editMenu = menubar.addMenu("Edit")

        goto_edit = QtWidgets.QAction("Go To...", self)
        goto_edit.setShortcut("Ctrl+T")
        goto_edit.triggered.connect(self.goto_dialog.show)
        editMenu.addAction(goto_edit)

        self.resize(600, 500)
        self.center()

    def center(self):
        self.setGeometry(
            QtWidgets.QStyle.alignedRect(
                QtCore.Qt.LeftToRight,
                QtCore.Qt.AlignCenter,
                self.size(),
                QtWidgets.qApp.desktop().availableGeometry(),
            )
        )


def main():
    app = QtWidgets.QApplication(sys.argv)
    w = Writter()
    w.show()
    return app.exec_()


if __name__ == "__main__":
    sys.exit(main())