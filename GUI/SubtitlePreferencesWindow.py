# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SubtitlePreferencesWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Preferences(object):
    def setupUi(self, Preferences):
        if not Preferences.objectName():
            Preferences.setObjectName(u"Preferences")
        Preferences.resize(477, 394)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Preferences.sizePolicy().hasHeightForWidth())
        Preferences.setSizePolicy(sizePolicy)
        Preferences.setModal(True)
        self.verticalLayout = QVBoxLayout(Preferences)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(Preferences)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.horizontalLayout = QHBoxLayout(self.tab)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout_6 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_8)

        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_9)

        self.label_10 = QLabel(self.groupBox)
        self.label_10.setObjectName(u"label_10")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_10)


        self.horizontalLayout_6.addLayout(self.formLayout_2)

        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.label_12 = QLabel(self.groupBox)
        self.label_12.setObjectName(u"label_12")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_12)

        self.label_13 = QLabel(self.groupBox)
        self.label_13.setObjectName(u"label_13")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_13)

        self.label_14 = QLabel(self.groupBox)
        self.label_14.setObjectName(u"label_14")

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.label_14)


        self.horizontalLayout_6.addLayout(self.formLayout_3)


        self.verticalLayout_2.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.tab)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.checkBox_2 = QCheckBox(self.groupBox_2)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.horizontalLayout_2.addWidget(self.checkBox_2)

        self.horizontalSpacer = QSpacerItem(103, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.lineEdit = QLineEdit(self.groupBox_2)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_2.addWidget(self.lineEdit)

        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)


        self.verticalLayout_2.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.tab)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_2 = QLabel(self.groupBox_3)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.label_3 = QLabel(self.groupBox_3)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.label_4 = QLabel(self.groupBox_3)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_4)

        self.label_5 = QLabel(self.groupBox_3)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_5)

        self.fontComboBox = QFontComboBox(self.groupBox_3)
        self.fontComboBox.setObjectName(u"fontComboBox")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.fontComboBox)

        self.lineEdit_2 = QLineEdit(self.groupBox_3)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMaximumSize(QSize(50, 16777215))

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEdit_2)

        self.lineEdit_3 = QLineEdit(self.groupBox_3)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMaximumSize(QSize(50, 16777215))

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lineEdit_3)

        self.horizontalSlider = QSlider(self.groupBox_3)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.horizontalSlider)


        self.verticalLayout_3.addLayout(self.formLayout)


        self.verticalLayout_2.addWidget(self.groupBox_3)

        self.checkBox = QCheckBox(self.tab)
        self.checkBox.setObjectName(u"checkBox")

        self.verticalLayout_2.addWidget(self.checkBox)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_5 = QVBoxLayout(self.tab_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.groupBox_4 = QGroupBox(self.tab_2)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setMinimumSize(QSize(150, 0))
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.checkBox_3 = QCheckBox(self.groupBox_4)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.verticalLayout_6.addWidget(self.checkBox_3)

        self.checkBox_4 = QCheckBox(self.groupBox_4)
        self.checkBox_4.setObjectName(u"checkBox_4")

        self.verticalLayout_6.addWidget(self.checkBox_4)

        self.checkBox_5 = QCheckBox(self.groupBox_4)
        self.checkBox_5.setObjectName(u"checkBox_5")

        self.verticalLayout_6.addWidget(self.checkBox_5)


        self.horizontalLayout_5.addWidget(self.groupBox_4)

        self.groupBox_5 = QGroupBox(self.tab_2)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.checkBox_6 = QCheckBox(self.groupBox_5)
        self.checkBox_6.setObjectName(u"checkBox_6")

        self.verticalLayout_4.addWidget(self.checkBox_6)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_6 = QLabel(self.groupBox_5)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_3.addWidget(self.label_6)

        self.lineEdit_4 = QLineEdit(self.groupBox_5)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_3.addWidget(self.lineEdit_4)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.comboBox = QComboBox(self.groupBox_5)
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout_4.addWidget(self.comboBox)

        self.label_7 = QLabel(self.groupBox_5)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_4.addWidget(self.label_7)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)


        self.horizontalLayout_5.addWidget(self.groupBox_5)


        self.verticalLayout_5.addLayout(self.horizontalLayout_5)

        self.verticalSpacer = QSpacerItem(20, 116, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout.addWidget(self.tabWidget)

        self.buttonBox = QDialogButtonBox(Preferences)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(Preferences)
        self.buttonBox.accepted.connect(Preferences.accept)
        self.buttonBox.rejected.connect(Preferences.reject)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Preferences)
    # setupUi

    def retranslateUi(self, Preferences):
        Preferences.setWindowTitle(QCoreApplication.translate("Preferences", u"Preferences", None))
        self.groupBox.setTitle(QCoreApplication.translate("Preferences", u"Color", None))
        self.label_8.setText(QCoreApplication.translate("Preferences", u"Translation", None))
        self.label_9.setText(QCoreApplication.translate("Preferences", u"Unknown words", None))
        self.label_10.setText(QCoreApplication.translate("Preferences", u"Known words", None))
        self.label_12.setText(QCoreApplication.translate("Preferences", u"Studied words", None))
        self.label_13.setText(QCoreApplication.translate("Preferences", u"Name", None))
        self.label_14.setText(QCoreApplication.translate("Preferences", u"Difficult words", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Preferences", u"Timings", None))
        self.checkBox_2.setText(QCoreApplication.translate("Preferences", u"Automatic durations", None))
        self.label.setText(QCoreApplication.translate("Preferences", u"Milliseconds per character", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Preferences", u"ASS Subtitle", None))
        self.label_2.setText(QCoreApplication.translate("Preferences", u"Font name", None))
        self.label_3.setText(QCoreApplication.translate("Preferences", u"Main font size", None))
        self.label_4.setText(QCoreApplication.translate("Preferences", u"Translate font size", None))
        self.label_5.setText(QCoreApplication.translate("Preferences", u"Transparence of known words", None))
        self.checkBox.setText(QCoreApplication.translate("Preferences", u"Don't show subtitles with all words known", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Preferences", u"Export to subtitle ", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Preferences", u"Type words", None))
        self.checkBox_3.setText(QCoreApplication.translate("Preferences", u"Unknown words", None))
        self.checkBox_4.setText(QCoreApplication.translate("Preferences", u"Study words", None))
        self.checkBox_5.setText(QCoreApplication.translate("Preferences", u"Known words", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("Preferences", u"Parameters", None))
        self.checkBox_6.setText(QCoreApplication.translate("Preferences", u"No blank translation ", None))
        self.label_6.setText(QCoreApplication.translate("Preferences", u"  Mentioned more than", None))
        self.label_7.setText(QCoreApplication.translate("Preferences", u"Language", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Preferences", u"Export from database", None))
    # retranslateUi

