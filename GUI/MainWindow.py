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
        MainWindow.resize(1132, 947)
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
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setEnabled(True)
        self.splitter.setOrientation(Qt.Horizontal)
        self.textBrowser = QTextBrowser(self.splitter)
        self.textBrowser.setObjectName(u"textBrowser")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy2)
        self.textBrowser.setMinimumSize(QSize(250, 0))
        self.textBrowser.setMaximumSize(QSize(250, 16777215))
        self.textBrowser.setBaseSize(QSize(250, 0))
        self.splitter.addWidget(self.textBrowser)
        self.tabWidget = QTabWidget(self.splitter)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy1.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy1)
        self.tabWidget.setMinimumSize(QSize(611, 551))
        self.Processing = QWidget()
        self.Processing.setObjectName(u"Processing")
        self.verticalLayout = QVBoxLayout(self.Processing)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.TranslationTable = QTableView(self.Processing)
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

        self.infoTable = QTableWidget(self.Processing)
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
        self.infoTable.horizontalHeader().setVisible(True)
        self.infoTable.horizontalHeader().setDefaultSectionSize(300)
        self.infoTable.horizontalHeader().setStretchLastSection(True)
        self.infoTable.verticalHeader().setVisible(False)
        self.infoTable.verticalHeader().setStretchLastSection(True)

        self.verticalLayout.addWidget(self.infoTable)

        self.ButtonsRow = QFrame(self.Processing)
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


        self.verticalLayout.addWidget(self.ButtonsRow)

        self.tabWidget.addTab(self.Processing, "")
        self.Export = QWidget()
        self.Export.setObjectName(u"Export")
        self.verticalLayout_4 = QVBoxLayout(self.Export)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.groupBox_2 = QGroupBox(self.Export)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy5)
        font = QFont()
        font.setBold(False)
        font.setWeight(50)
        self.groupBox_2.setFont(font)
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(260, 32))
        self.label.setWordWrap(True)

        self.horizontalLayout_3.addWidget(self.label)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pushButton_2 = QPushButton(self.groupBox_2)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout_2.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.groupBox_2)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.verticalLayout_2.addWidget(self.pushButton_3)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)


        self.verticalLayout_4.addWidget(self.groupBox_2)

        self.groupBox = QGroupBox(self.Export)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout_4 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_2 = QSpacerItem(481, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.pushButton_4 = QPushButton(self.groupBox)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.verticalLayout_3.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.groupBox)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.verticalLayout_3.addWidget(self.pushButton_5)


        self.horizontalLayout_4.addLayout(self.verticalLayout_3)


        self.verticalLayout_4.addWidget(self.groupBox)

        self.verticalSpacer_2 = QSpacerItem(20, 349, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.tabWidget.addTab(self.Export, "")
        self.splitter.addWidget(self.tabWidget)

        self.horizontalLayout.addWidget(self.splitter)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


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
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Processing), QCoreApplication.translate("MainWindow", u"Processing", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Export subtitle", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Set a monospaced font (Consolas, courier New etc.) for SubRip (srt) subtitles in your media player", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Export subtitle", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Export from database", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Export), QCoreApplication.translate("MainWindow", u"Export", None))
    # retranslateUi

