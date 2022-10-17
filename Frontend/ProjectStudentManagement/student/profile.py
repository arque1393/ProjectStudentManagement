# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'profile.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_studentProfile(object):
    def setupUi(self, studentProfile):
        if not studentProfile.objectName():
            studentProfile.setObjectName(u"studentProfile")
        studentProfile.resize(1147, 599)
        studentProfile.setMinimumSize(QSize(0, 0))
        studentProfile.setStyleSheet(u"QLabel{\n"
"	background-color:rgb(216, 232, 255);\n"
"	padding: 1% 3%;\n"
"	padding-left:7%;\n"
"	border-top-left-radius: 20px;\n"
"	border-bottom-left-radius: 20px;\n"
"	font-size:19px;\n"
"}\n"
"\n"
"QLineEdit{\n"
"	font-size:20px;\n"
"	border-top-right-radius: 20px;\n"
"	border-bottom-right-radius: 20px;\n"
"	border: solid;\n"
"	 padding: 2% 10%;\n"
"}\n"
"\n"
"QPushButton{\n"
"		font-size:20px;\n"
"\n"
"}")
        self.verticalLayout = QVBoxLayout(studentProfile)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(studentProfile)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 5))
        self.label_2.setMaximumSize(QSize(16777215, 45))
        self.label_2.setStyleSheet(u"QLabel{\n"
"		color:white;\n"
"		\n"
"		font: 20pt \"Sans Serif\";\n"
"		background-color:rgb(53, 134, 255);\n"
"		border-radius: 20px;\n"
"        text-align: center;\n"
"		padding:  3px 40px;\n"
"}\n"
"\n"
"")

        self.verticalLayout.addWidget(self.label_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(10, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.profilePicLabel = QLabel(studentProfile)
        self.profilePicLabel.setObjectName(u"profilePicLabel")
        self.profilePicLabel.setMinimumSize(QSize(150, 150))
        self.profilePicLabel.setMaximumSize(QSize(200, 200))
        self.profilePicLabel.setStyleSheet(u"QLabel{\n"
"	height:100%;\n"
"	width:100%;\n"
"	border-radius:100%;\n"
"	background-color:green;\n"
"	color:white;\n"
"	padding:100px;\n"
"}")

        self.verticalLayout_2.addWidget(self.profilePicLabel)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.backToHomeBtn = QPushButton(studentProfile)
        self.backToHomeBtn.setObjectName(u"backToHomeBtn")

        self.verticalLayout_2.addWidget(self.backToHomeBtn)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.usernameLabel = QLabel(studentProfile)
        self.usernameLabel.setObjectName(u"usernameLabel")
        self.usernameLabel.setMinimumSize(QSize(130, 30))
        self.usernameLabel.setMaximumSize(QSize(140, 16777215))

        self.horizontalLayout_11.addWidget(self.usernameLabel)

        self.usernameValue = QLabel(studentProfile)
        self.usernameValue.setObjectName(u"usernameValue")
        self.usernameValue.setMinimumSize(QSize(400, 45))
        self.usernameValue.setStyleSheet(u"QLabel{\n"
"	font-size:20px;\n"
"	border-top-right-radius: 20px;\n"
"	border-bottom-right-radius: 20px;\n"
"	border-top-left-radius: 0px;\n"
"	border-bottom-left-radius: 0px;\n"
"	border: solid;\n"
"	 padding: 2% 10%;\n"
"	background-color:rgb(255, 245, 250)\n"
"}")

        self.horizontalLayout_11.addWidget(self.usernameValue)


        self.verticalLayout_3.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.firstNameLabel = QLabel(studentProfile)
        self.firstNameLabel.setObjectName(u"firstNameLabel")
        self.firstNameLabel.setMinimumSize(QSize(130, 30))

        self.horizontalLayout_2.addWidget(self.firstNameLabel)

        self.firstNameValue = QLineEdit(studentProfile)
        self.firstNameValue.setObjectName(u"firstNameValue")
        self.firstNameValue.setMinimumSize(QSize(400, 45))

        self.horizontalLayout_2.addWidget(self.firstNameValue)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_7 = QLabel(studentProfile)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(130, 30))

        self.horizontalLayout_6.addWidget(self.label_7)

        self.lastNameValue = QLineEdit(studentProfile)
        self.lastNameValue.setObjectName(u"lastNameValue")
        self.lastNameValue.setMinimumSize(QSize(400, 45))

        self.horizontalLayout_6.addWidget(self.lastNameValue)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_5 = QLabel(studentProfile)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(130, 30))

        self.horizontalLayout_4.addWidget(self.label_5)

        self.departmentValue = QLineEdit(studentProfile)
        self.departmentValue.setObjectName(u"departmentValue")
        self.departmentValue.setMinimumSize(QSize(400, 45))

        self.horizontalLayout_4.addWidget(self.departmentValue)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(studentProfile)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(130, 30))

        self.horizontalLayout_3.addWidget(self.label_4)

        self.rollNoValue = QLineEdit(studentProfile)
        self.rollNoValue.setObjectName(u"rollNoValue")
        self.rollNoValue.setMinimumSize(QSize(400, 45))

        self.horizontalLayout_3.addWidget(self.rollNoValue)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_9 = QLabel(studentProfile)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(130, 30))

        self.horizontalLayout_8.addWidget(self.label_9)

        self.contuctNoValue = QLineEdit(studentProfile)
        self.contuctNoValue.setObjectName(u"contuctNoValue")
        self.contuctNoValue.setMinimumSize(QSize(400, 45))

        self.horizontalLayout_8.addWidget(self.contuctNoValue)


        self.verticalLayout_3.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.updateBtn = QPushButton(studentProfile)
        self.updateBtn.setObjectName(u"updateBtn")
        self.updateBtn.setMinimumSize(QSize(0, 40))

        self.horizontalLayout_5.addWidget(self.updateBtn)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)

        self.resetBtn = QPushButton(studentProfile)
        self.resetBtn.setObjectName(u"resetBtn")
        self.resetBtn.setMinimumSize(QSize(0, 40))

        self.horizontalLayout_5.addWidget(self.resetBtn)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_3.addItem(self.horizontalSpacer_2)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout_5.addItem(self.verticalSpacer_5)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.filePathLoaderValue = QLineEdit(studentProfile)
        self.filePathLoaderValue.setObjectName(u"filePathLoaderValue")
        self.filePathLoaderValue.setMinimumSize(QSize(240, 0))
        self.filePathLoaderValue.setStyleSheet(u"QLineEdit{\n"
"	font-size:17px;\n"
"	border-radius: 20px;\n"
"	border: solid;\n"
"	 padding: 0% 10%;\n"
"}")

        self.horizontalLayout_13.addWidget(self.filePathLoaderValue)

        self.fileBrowseBtn = QPushButton(studentProfile)
        self.fileBrowseBtn.setObjectName(u"fileBrowseBtn")
        self.fileBrowseBtn.setMaximumSize(QSize(60, 16777215))
        font = QFont()
        self.fileBrowseBtn.setFont(font)
        self.fileBrowseBtn.setStyleSheet(u"QPushButton{\n"
" font-size:15px\n"
"}")

        self.horizontalLayout_13.addWidget(self.fileBrowseBtn)


        self.verticalLayout_5.addLayout(self.horizontalLayout_13)

        self.fileHandlingBtn = QPushButton(studentProfile)
        self.fileHandlingBtn.setObjectName(u"fileHandlingBtn")
        self.fileHandlingBtn.setMinimumSize(QSize(150, 0))

        self.verticalLayout_5.addWidget(self.fileHandlingBtn)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_6)


        self.horizontalLayout.addLayout(self.verticalLayout_5)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.bottomBarLabel = QLabel(studentProfile)
        self.bottomBarLabel.setObjectName(u"bottomBarLabel")
        self.bottomBarLabel.setMinimumSize(QSize(0, 25))
        self.bottomBarLabel.setMaximumSize(QSize(16777215, 45))

        self.horizontalLayout_9.addWidget(self.bottomBarLabel)


        self.verticalLayout.addLayout(self.horizontalLayout_9)


        self.retranslateUi(studentProfile)

        QMetaObject.connectSlotsByName(studentProfile)
    # setupUi

    def retranslateUi(self, studentProfile):
        studentProfile.setWindowTitle(QCoreApplication.translate("studentProfile", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("studentProfile", u"Student Profile", None))
        self.profilePicLabel.setText("")
        self.backToHomeBtn.setText(QCoreApplication.translate("studentProfile", u"Back to Home", None))
        self.usernameLabel.setText(QCoreApplication.translate("studentProfile", u"Username", None))
        self.usernameValue.setText(QCoreApplication.translate("studentProfile", u"TextLabel", None))
        self.firstNameLabel.setText(QCoreApplication.translate("studentProfile", u"First Name", None))
        self.firstNameValue.setText(QCoreApplication.translate("studentProfile", u"I am Greate", None))
        self.label_7.setText(QCoreApplication.translate("studentProfile", u"Lastt Name", None))
        self.lastNameValue.setText(QCoreApplication.translate("studentProfile", u"I am Greate", None))
        self.label_5.setText(QCoreApplication.translate("studentProfile", u"Department", None))
        self.departmentValue.setText(QCoreApplication.translate("studentProfile", u"I am Greate", None))
        self.label_4.setText(QCoreApplication.translate("studentProfile", u"Roll No", None))
        self.rollNoValue.setText(QCoreApplication.translate("studentProfile", u"I am Greate", None))
        self.label_9.setText(QCoreApplication.translate("studentProfile", u"Contuct No.", None))
        self.contuctNoValue.setText(QCoreApplication.translate("studentProfile", u"I am Greate", None))
        self.updateBtn.setText(QCoreApplication.translate("studentProfile", u"Update", None))
        self.resetBtn.setText(QCoreApplication.translate("studentProfile", u"Resert", None))
        self.filePathLoaderValue.setText(QCoreApplication.translate("studentProfile", u"I am Greate", None))
        self.fileBrowseBtn.setText(QCoreApplication.translate("studentProfile", u"Browse", None))
        self.fileHandlingBtn.setText(QCoreApplication.translate("studentProfile", u"File Handling", None))
        self.bottomBarLabel.setText(QCoreApplication.translate("studentProfile", u"Bottom Bar", None))
    # retranslateUi

