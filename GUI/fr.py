# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fr_QtableView.ui'
#
# Created by: PySide2 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PySide2 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1132, 947)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setEnabled(True)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.textBrowser = QtWidgets.QTextBrowser(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        self.textBrowser.setMinimumSize(QtCore.QSize(250, 0))
        self.textBrowser.setMaximumSize(QtCore.QSize(250, 16777215))
        self.textBrowser.setBaseSize(QtCore.QSize(250, 0))
        self.textBrowser.setObjectName("textBrowser")
        self.tabWidget = QtWidgets.QTabWidget(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(611, 551))
        self.tabWidget.setObjectName("tabWidget")
        self.Processing = QtWidgets.QWidget()
        self.Processing.setObjectName("Processing")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.Processing)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.TranslationTable = QtWidgets.QTableView(self.Processing)
        self.TranslationTable.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.TranslationTable.sizePolicy().hasHeightForWidth())
        self.TranslationTable.setSizePolicy(sizePolicy)
        self.TranslationTable.setMinimumSize(QtCore.QSize(100, 100))
        self.TranslationTable.setSortingEnabled(True)
        self.TranslationTable.setObjectName("TranslationTable")
        self.verticalLayout.addWidget(self.TranslationTable)
        self.infoTable = QtWidgets.QTableWidget(self.Processing)
        self.infoTable.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.infoTable.sizePolicy().hasHeightForWidth())
        self.infoTable.setSizePolicy(sizePolicy)
        self.infoTable.setMinimumSize(QtCore.QSize(0, 175))
        self.infoTable.setMaximumSize(QtCore.QSize(16777215, 100))
        self.infoTable.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.infoTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.infoTable.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.infoTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectColumns)
        self.infoTable.setObjectName("infoTable")
        self.infoTable.setColumnCount(3)
        self.infoTable.setRowCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.infoTable.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.infoTable.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.infoTable.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.infoTable.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.infoTable.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.infoTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.infoTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.infoTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.infoTable.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.infoTable.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.infoTable.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.infoTable.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.infoTable.setItem(4, 0, item)
        self.infoTable.horizontalHeader().setVisible(True)
        self.infoTable.horizontalHeader().setDefaultSectionSize(170)
        self.infoTable.horizontalHeader().setStretchLastSection(True)
        self.infoTable.verticalHeader().setVisible(False)
        self.infoTable.verticalHeader().setStretchLastSection(False)
        self.verticalLayout.addWidget(self.infoTable)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.ButtonsRow = QtWidgets.QFrame(self.Processing)
        self.ButtonsRow.setEnabled(True)
        self.ButtonsRow.setMinimumSize(QtCore.QSize(0, 40))
        self.ButtonsRow.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ButtonsRow.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ButtonsRow.setObjectName("ButtonsRow")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.ButtonsRow)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.LanguageOfSubtitles = QtWidgets.QLabel(self.ButtonsRow)
        self.LanguageOfSubtitles.setObjectName("LanguageOfSubtitles")
        self.horizontalLayout_2.addWidget(self.LanguageOfSubtitles)
        self.comboBox = QtWidgets.QComboBox(self.ButtonsRow)
        self.comboBox.setMinimumSize(QtCore.QSize(100, 0))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox)
        self.checkBox = QtWidgets.QCheckBox(self.ButtonsRow)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_2.addWidget(self.checkBox)
        self.checkBox_2 = QtWidgets.QCheckBox(self.ButtonsRow)
        self.checkBox_2.setObjectName("checkBox_2")
        self.horizontalLayout_2.addWidget(self.checkBox_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.open_subtitle_btn = QtWidgets.QPushButton(self.ButtonsRow)
        self.open_subtitle_btn.setObjectName("open_subtitle_btn")
        self.horizontalLayout_2.addWidget(self.open_subtitle_btn)
        self.verticalLayout.addWidget(self.ButtonsRow)
        self.ButtonsRow.raise_()
        self.TranslationTable.raise_()
        self.infoTable.raise_()
        self.tabWidget.addTab(self.Processing, "")
        self.Export = QtWidgets.QWidget()
        self.Export.setObjectName("Export")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.Export)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox_2 = QtWidgets.QGroupBox(self.Export)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(260, 32))
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_2.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_2.addWidget(self.pushButton_3)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout_4.addWidget(self.groupBox_2)
        self.groupBox = QtWidgets.QGroupBox(self.Export)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem3 = QtWidgets.QSpacerItem(481, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_3.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_3.addWidget(self.pushButton_5)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        self.verticalLayout_4.addWidget(self.groupBox)
        spacerItem4 = QtWidgets.QSpacerItem(20, 349, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem4)
        self.tabWidget.addTab(self.Export, "")
        self.horizontalLayout.addWidget(self.splitter)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PyLinguaSubtitle"))
        item = self.infoTable.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Number of words"))
        item = self.infoTable.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "Number of unknown words"))
        item = self.infoTable.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "Number of known words"))
        item = self.infoTable.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "Number of studied words"))
        item = self.infoTable.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "Number of new words"))
        item = self.infoTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Parameter"))
        item = self.infoTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Unique"))
        item = self.infoTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Total"))
        __sortingEnabled = self.infoTable.isSortingEnabled()
        self.infoTable.setSortingEnabled(False)
        item = self.infoTable.item(0, 0)
        item.setText(_translate("MainWindow", "Number of words"))
        item = self.infoTable.item(1, 0)
        item.setText(_translate("MainWindow", "Number of unknown words"))
        item = self.infoTable.item(2, 0)
        item.setText(_translate("MainWindow", "Number of known words"))
        item = self.infoTable.item(3, 0)
        item.setText(_translate("MainWindow", "Number of studied words"))
        item = self.infoTable.item(4, 0)
        item.setText(_translate("MainWindow", "Number of new words"))
        self.infoTable.setSortingEnabled(__sortingEnabled)
        self.LanguageOfSubtitles.setText(_translate("MainWindow", "Language of subtitles:"))
        self.comboBox.setItemText(0, _translate("MainWindow", "New Item"))
        self.comboBox.setItemText(1, _translate("MainWindow", "New Item"))
        self.comboBox.setItemText(2, _translate("MainWindow", "New Item"))
        self.comboBox.setItemText(3, _translate("MainWindow", "New Item"))
        self.checkBox.setText(_translate("MainWindow", "Hide known"))
        self.checkBox_2.setText(_translate("MainWindow", "Hide translated"))
        self.open_subtitle_btn.setText(_translate("MainWindow", "Open subtitle"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Processing), _translate("MainWindow", "Processing"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Export subtitle"))
        self.label.setText(_translate("MainWindow", "Set a monospaced font (Consolas, courier New etc.) for SubRip (srt) subtitles in your media player"))
        self.pushButton_2.setText(_translate("MainWindow", "Settings"))
        self.pushButton_3.setText(_translate("MainWindow", "Export subtitle"))
        self.groupBox.setTitle(_translate("MainWindow", "Export from database"))
        self.pushButton_4.setText(_translate("MainWindow", "Settings"))
        self.pushButton_5.setText(_translate("MainWindow", "Export"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Export), _translate("MainWindow", "Export"))
