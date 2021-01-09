import sys
from PyQt5.QtGui     import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore    import *

class Window(QWidget):
    def __init__(self, rows, columns):
        super().__init__()

        self.table = QTableWidget(rows, columns, self)

        for row in range(rows):
            self.table.setItem(row, columns-1, QTableWidgetItem(str(row)))
            for col in range(columns - 1):
                widget = QWidget()
                checkbox = QCheckBox()
                checkbox.setCheckState(Qt.Unchecked)
                layoutH = QHBoxLayout(widget)
                layoutH.addWidget(checkbox)
                layoutH.setAlignment(Qt.AlignCenter)
                layoutH.setContentsMargins(0, 0, 0, 0)
                self.table.setCellWidget(row, col, widget)

        self.button = QPushButton("Контроль выбранных QCheckBox ")
        self.button.clicked.connect(self.ButtonClicked)

        layoutV     = QVBoxLayout(self)
        layoutV.addWidget(self.table)
        layoutV.addWidget(self.button)


    def ButtonClicked(self):
        checked_list = []
        for i in range(self.table.rowCount()):
            if self.table.cellWidget(i, 0).findChild(type(QCheckBox())).isChecked():
                checked_list.append(self.table.item(i, 1).text())
        print(checked_list)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window(7658, 5)
    window.resize(350, 300)
    window.show()
    sys.exit(app.exec_())