from PySide2.QtCore import QEvent, QPoint, QRect
from PySide2.QtGui import Qt
from PySide2.QtWidgets import QStyledItemDelegate, QStyleOptionButton, QStyle, QApplication


class CheckBoxDelegate(QStyledItemDelegate):
    def __init__(self, parent=None):
        QStyledItemDelegate.__init__(self, parent)

    def createEditor(self, parent, option, index):
        '''
        Important, otherwise an editor is created if the user clicks in this cell.
        '''
        return None

    def paint(self, painter, option, index):
        '''
        Paint a checkbox without the label.
        '''
        checked = bool(index.model().data(index, Qt.DisplayRole))
        check_box_style_option = QStyleOptionButton()

        if (index.flags() & Qt.ItemIsEditable) > 0:
            check_box_style_option.state |= QStyle.State_Enabled
        else:
            check_box_style_option.state |= QStyle.State_ReadOnly

        if checked:
            check_box_style_option.state |= QStyle.State_On
        else:
            check_box_style_option.state |= QStyle.State_Off

        check_box_style_option.rect = self.getCheckBoxRect(option)
        if (index.flags() & Qt.ItemIsEditable) == 0:
            check_box_style_option.state |= QStyle.State_ReadOnly

        QApplication.style().drawControl(QStyle.CE_CheckBox, check_box_style_option, painter)

    def editorEvent(self, event, model, option, index):
        '''
        Change the data in the model and the state of the checkbox
        if the user presses the left mousebutton or presses
        Key_Space or Key_Select and this cell is editable. Otherwise do nothing.
        '''
        if not (index.flags() & Qt.ItemIsEditable) > 0:
            return False

        # Do not change the checkbox-state
        if event.type() == QEvent.MouseButtonRelease or event.type() == QEvent.MouseButtonDblClick:
            if event.button() != Qt.LeftButton or not self.getCheckBoxRect(option).contains(event.pos()):
                return False
            if event.type() == QEvent.MouseButtonDblClick:
                return True
        elif event.type() == QEvent.KeyPress:
            if event.key() != Qt.Key_Space and event.key() != Qt.Key_Select:
                return False
        else:
            return False

        # Change the checkbox-state
        self.setModelData(None, model, index)
        return True

    def setModelData(self, editor, model, index):
        '''
        The user wanted to change the old state in the opposite.
        '''
        newValue = not bool(index.model().data(index, Qt.DisplayRole))
        model.setData(index, newValue, Qt.EditRole)

    def getCheckBoxRect(self, option):
        check_box_style_option = QStyleOptionButton()
        check_box_rect = QApplication.style().subElementRect(QStyle.SE_CheckBoxIndicator, check_box_style_option, None)
        check_box_point = QPoint(option.rect.x() +
                                 option.rect.width() / 2 -
                                 check_box_rect.width() / 2,
                                 option.rect.y() +
                                 option.rect.height() / 2 -
                                 check_box_rect.height() / 2)
        return QRect(check_box_point, check_box_rect.size())
