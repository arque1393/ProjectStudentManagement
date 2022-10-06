# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loginWidget.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_LoginForm(object):
    def setupUi(self, LoginForm):
        if not LoginForm.objectName():
            LoginForm.setObjectName(u"LoginForm")
        LoginForm.resize(625, 510)
        font = QFont()
        font.setFamilies([u"Open Sans SemiBold"])
        font.setPointSize(22)
        font.setBold(True)
        LoginForm.setFont(font)
        LoginForm.setStyleSheet(u"QLabel{\n"
"	font-size:20px;\n"
"\n"
"}\n"
"QLineEdit{\n"
"		height:30px;\n"
"		background-color:rgb(240, 255, 248);\n"
"        border-radius: 50px;\n"
"}")
        self.horizontalLayout_5 = QHBoxLayout(LoginForm)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label = QLabel(LoginForm)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"QLabel{\n"
"		color:white;\n"
"		font-size:30px;\n"
"		background-color:rgb(53, 134, 255);\n"
"		border-radius: 20px;\n"
"        text-align: center;\n"
"		padding :0 100%;\n"
"}\n"
"\n"
"")

        self.verticalLayout_4.addWidget(self.label)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_4 = QLabel(LoginForm)
        self.label_4.setObjectName(u"label_4")
        font1 = QFont()
        self.label_4.setFont(font1)

        self.horizontalLayout.addWidget(self.label_4)

        self.comboBox = QComboBox(LoginForm)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(140, 0))

        self.horizontalLayout.addWidget(self.comboBox)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(LoginForm)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)

        self.horizontalLayout_3.addWidget(self.label_2)

        self.lineEdit = QLineEdit(LoginForm)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_3.addWidget(self.lineEdit)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(LoginForm)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.horizontalLayout_4.addWidget(self.label_3)

        self.lineEdit_2 = QLineEdit(LoginForm)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.horizontalLayout_4.addWidget(self.lineEdit_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.pushButton_3 = QPushButton(LoginForm)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(288, 0))

        self.verticalLayout_2.addWidget(self.pushButton_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_2 = QPushButton(LoginForm)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(140, 0))

        self.horizontalLayout_2.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(LoginForm)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(140, 0))

        self.horizontalLayout_2.addWidget(self.pushButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)


        self.horizontalLayout_5.addLayout(self.verticalLayout_4)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)


        self.retranslateUi(LoginForm)

        QMetaObject.connectSlotsByName(LoginForm)
    # setupUi

    def retranslateUi(self, LoginForm):
        LoginForm.setWindowTitle(QCoreApplication.translate("LoginForm", u"Form", None))
        self.label.setText(QCoreApplication.translate("LoginForm", u"Login", None))
        self.label_4.setText(QCoreApplication.translate("LoginForm", u"Login As", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("LoginForm", u"Student", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("LoginForm", u"Faculty", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("LoginForm", u"admin", None))

        self.label_2.setText(QCoreApplication.translate("LoginForm", u"Username", None))
        self.label_3.setText(QCoreApplication.translate("LoginForm", u"Password ", None))
        self.pushButton_3.setText(QCoreApplication.translate("LoginForm", u"Login", None))
        self.pushButton_2.setText(QCoreApplication.translate("LoginForm", u"Close", None))
        self.pushButton.setText(QCoreApplication.translate("LoginForm", u"Reset Form", None))
    # retranslateUi

