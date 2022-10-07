# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'signupWidget.ui'
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

class Ui_SignupForm(object):
    def setupUi(self, SignupForm):
        if not SignupForm.objectName():
            SignupForm.setObjectName(u"SignupForm")
        SignupForm.resize(865, 591)
        SignupForm.setStyleSheet(u"QLabel{\n"
"	font-size:20px;\n"
"\n"
"}\n"
"QLineEdit{\n"
"		height:30px;\n"
"		background-color:rgb(240, 255, 248);\n"
"        border-radius: 50px;\n"
"}")
        self.horizontalLayout_5 = QHBoxLayout(SignupForm)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label = QLabel(SignupForm)
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
        self.label_4 = QLabel(SignupForm)
        self.label_4.setObjectName(u"label_4")
        font = QFont()
        self.label_4.setFont(font)

        self.horizontalLayout.addWidget(self.label_4)

        self.comboBox = QComboBox(SignupForm)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(140, 0))

        self.horizontalLayout.addWidget(self.comboBox)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(SignupForm)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.horizontalLayout_3.addWidget(self.label_2)

        self.lineEdit = QLineEdit(SignupForm)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_3.addWidget(self.lineEdit)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_7 = QLabel(SignupForm)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)

        self.horizontalLayout_10.addWidget(self.label_7)

        self.lineEdit_5 = QLineEdit(SignupForm)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.horizontalLayout_10.addWidget(self.lineEdit_5)


        self.verticalLayout_2.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(SignupForm)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.horizontalLayout_4.addWidget(self.label_3)

        self.lineEdit_2 = QLineEdit(SignupForm)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.horizontalLayout_4.addWidget(self.lineEdit_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_5 = QLabel(SignupForm)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.horizontalLayout_8.addWidget(self.label_5)

        self.lineEdit_3 = QLineEdit(SignupForm)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.horizontalLayout_8.addWidget(self.lineEdit_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_8)

        self.pushButton_3 = QPushButton(SignupForm)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(288, 0))

        self.verticalLayout_2.addWidget(self.pushButton_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_2 = QPushButton(SignupForm)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(140, 0))

        self.horizontalLayout_2.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(SignupForm)
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


        self.retranslateUi(SignupForm)

        QMetaObject.connectSlotsByName(SignupForm)
    # setupUi

    def retranslateUi(self, SignupForm):
        SignupForm.setWindowTitle(QCoreApplication.translate("SignupForm", u"Form", None))
        self.label.setText(QCoreApplication.translate("SignupForm", u"SignUp", None))
        self.label_4.setText(QCoreApplication.translate("SignupForm", u"Login As", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("SignupForm", u"Student", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("SignupForm", u"Faculty", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("SignupForm", u"admin", None))

        self.label_2.setText(QCoreApplication.translate("SignupForm", u"Username", None))
        self.label_7.setText(QCoreApplication.translate("SignupForm", u"Email Id", None))
        self.label_3.setText(QCoreApplication.translate("SignupForm", u"Password ", None))
        self.label_5.setText(QCoreApplication.translate("SignupForm", u"Confirm Password", None))
        self.pushButton_3.setText(QCoreApplication.translate("SignupForm", u"Signup", None))
        self.pushButton_2.setText(QCoreApplication.translate("SignupForm", u"Close", None))
        self.pushButton.setText(QCoreApplication.translate("SignupForm", u"Reset Form", None))
    # retranslateUi

