# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1030, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(800, 600))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy1)
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.left_part = QWidget(self.centralwidget)
        self.left_part.setObjectName(u"left_part")
        self.horizontalLayout_3 = QHBoxLayout(self.left_part)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.textBrowser = QTextBrowser(self.left_part)
        self.textBrowser.setObjectName(u"textBrowser")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy2)
        self.textBrowser.setMinimumSize(QSize(250, 0))
        self.textBrowser.setMaximumSize(QSize(250, 16777215))
        self.textBrowser.setBaseSize(QSize(250, 0))

        self.horizontalLayout_3.addWidget(self.textBrowser)


        self.horizontalLayout.addWidget(self.left_part)

        self.right_part = QWidget(self.centralwidget)
        self.right_part.setObjectName(u"right_part")
        self.verticalLayout = QVBoxLayout(self.right_part)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.TranslationTable = QTableView(self.right_part)
        self.TranslationTable.setObjectName(u"TranslationTable")
        self.TranslationTable.setEnabled(True)
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(100)
        sizePolicy3.setVerticalStretch(100)
        sizePolicy3.setHeightForWidth(self.TranslationTable.sizePolicy().hasHeightForWidth())
        self.TranslationTable.setSizePolicy(sizePolicy3)
        self.TranslationTable.setMinimumSize(QSize(100, 100))
        self.TranslationTable.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.TranslationTable.setSortingEnabled(True)
        self.TranslationTable.horizontalHeader().setStretchLastSection(False)
        self.TranslationTable.verticalHeader().setVisible(False)

        self.verticalLayout.addWidget(self.TranslationTable)

        self.infoTable = QTableWidget(self.right_part)
        if (self.infoTable.columnCount() < 3):
            self.infoTable.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.infoTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.infoTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.infoTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        if (self.infoTable.rowCount() < 4):
            self.infoTable.setRowCount(4)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.infoTable.setVerticalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.infoTable.setVerticalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.infoTable.setVerticalHeaderItem(2, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.infoTable.setVerticalHeaderItem(3, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.infoTable.setItem(0, 0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.infoTable.setItem(1, 0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.infoTable.setItem(2, 0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.infoTable.setItem(3, 0, __qtablewidgetitem10)
        self.infoTable.setObjectName(u"infoTable")
        self.infoTable.setEnabled(False)
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(100)
        sizePolicy4.setHeightForWidth(self.infoTable.sizePolicy().hasHeightForWidth())
        self.infoTable.setSizePolicy(sizePolicy4)
        self.infoTable.setMinimumSize(QSize(0, 145))
        self.infoTable.setMaximumSize(QSize(16777215, 145))
        self.infoTable.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.infoTable.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.infoTable.setCornerButtonEnabled(False)
        self.infoTable.horizontalHeader().setVisible(True)
        self.infoTable.horizontalHeader().setCascadingSectionResizes(False)
        self.infoTable.horizontalHeader().setMinimumSectionSize(39)
        self.infoTable.horizontalHeader().setDefaultSectionSize(250)
        self.infoTable.horizontalHeader().setHighlightSections(True)
        self.infoTable.horizontalHeader().setStretchLastSection(True)
        self.infoTable.verticalHeader().setVisible(False)
        self.infoTable.verticalHeader().setStretchLastSection(True)

        self.verticalLayout.addWidget(self.infoTable)

        self.ButtonsRow = QFrame(self.right_part)
        self.ButtonsRow.setObjectName(u"ButtonsRow")
        self.ButtonsRow.setEnabled(True)
        self.ButtonsRow.setMinimumSize(QSize(0, 40))
        self.ButtonsRow.setFrameShape(QFrame.StyledPanel)
        self.ButtonsRow.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.ButtonsRow)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.LanguageOfSubtitles = QLabel(self.ButtonsRow)
        self.LanguageOfSubtitles.setObjectName(u"LanguageOfSubtitles")

        self.horizontalLayout_2.addWidget(self.LanguageOfSubtitles)

        self.comboBox = QComboBox(self.ButtonsRow)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_2.addWidget(self.comboBox)

        self.HideKnown_Chekbox = QCheckBox(self.ButtonsRow)
        self.HideKnown_Chekbox.setObjectName(u"HideKnown_Chekbox")

        self.horizontalLayout_2.addWidget(self.HideKnown_Chekbox)

        self.HideTranslated_Chekbox = QCheckBox(self.ButtonsRow)
        self.HideTranslated_Chekbox.setObjectName(u"HideTranslated_Chekbox")

        self.horizontalLayout_2.addWidget(self.HideTranslated_Chekbox)

        self.horizontalSpacer = QSpacerItem(10, 10, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.open_subtitle_btn = QPushButton(self.ButtonsRow)
        self.open_subtitle_btn.setObjectName(u"open_subtitle_btn")

        self.horizontalLayout_2.addWidget(self.open_subtitle_btn)

        self.save_subtitle_btn = QPushButton(self.ButtonsRow)
        self.save_subtitle_btn.setObjectName(u"save_subtitle_btn")

        self.horizontalLayout_2.addWidget(self.save_subtitle_btn)


        self.verticalLayout.addWidget(self.ButtonsRow)


        self.horizontalLayout.addWidget(self.right_part)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"PyLinguaSubtitle", None))
        ___qtablewidgetitem = self.infoTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Parameter", None));
        ___qtablewidgetitem1 = self.infoTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Unique", None));
        ___qtablewidgetitem2 = self.infoTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Total", None));
        ___qtablewidgetitem3 = self.infoTable.verticalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Number of words", None));
        ___qtablewidgetitem4 = self.infoTable.verticalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Number of unknown words", None));
        ___qtablewidgetitem5 = self.infoTable.verticalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Number of known words", None));
        ___qtablewidgetitem6 = self.infoTable.verticalHeaderItem(3)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Number of new words", None));

        __sortingEnabled = self.infoTable.isSortingEnabled()
        self.infoTable.setSortingEnabled(False)
        ___qtablewidgetitem7 = self.infoTable.item(0, 0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Number of words", None));
        ___qtablewidgetitem8 = self.infoTable.item(1, 0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Number of unknown words", None));
        ___qtablewidgetitem9 = self.infoTable.item(2, 0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Number of known words", None));
        ___qtablewidgetitem10 = self.infoTable.item(3, 0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Number of new words", None));
        self.infoTable.setSortingEnabled(__sortingEnabled)

        self.LanguageOfSubtitles.setText(QCoreApplication.translate("MainWindow", u"Language of subtitles:", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"New Item", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"New Item", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"New Item", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"New Item", None))

        self.HideKnown_Chekbox.setText(QCoreApplication.translate("MainWindow", u"Hide known", None))
        self.HideTranslated_Chekbox.setText(QCoreApplication.translate("MainWindow", u"Hide translated", None))
        self.open_subtitle_btn.setText(QCoreApplication.translate("MainWindow", u"Open subtitle", None))
        self.save_subtitle_btn.setText(QCoreApplication.translate("MainWindow", u"Save subtitle", None))
    # retranslateUi

