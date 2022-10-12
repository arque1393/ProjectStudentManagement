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
        SignupForm.resize(732, 746)
        SignupForm.setStyleSheet(u"QLabel{\n"
"		font-size:20px;\n"
"}\n"
"QComboBox{\n"
"		font-size:15px;\n"
"}\n"
"QLineEdit{\n"
"		height:30px;\n"
"		background-color:rgb(240, 255, 248);\n"
"      	font-size:18px;\n"
"		border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton{\n"
"		height:26px;\n"
"		font-size:15px;	\n"
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
        self.designation_label = QLabel(SignupForm)
        self.designation_label.setObjectName(u"designation_label")
        font = QFont()
        self.designation_label.setFont(font)

        self.horizontalLayout.addWidget(self.designation_label)

        self.designation_field = QComboBox(SignupForm)
        self.designation_field.addItem("")
        self.designation_field.addItem("")
        self.designation_field.addItem("")
        self.designation_field.setObjectName(u"designation_field")
        self.designation_field.setMinimumSize(QSize(140, 0))

        self.horizontalLayout.addWidget(self.designation_field)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.message = QLabel(SignupForm)
        self.message.setObjectName(u"message")
        self.message.setEnabled(False)
        self.message.setStyleSheet(u"QLabel{\n"
"		font-size:15px;\n"
"		padding:0 100%;\n"
"		margin:0;\n"
"		text-align: center;\n"
"		color:rgb(200, 0, 0);\n"
"		background-color:rgb(255, 180, 180)\n"
"}\n"
"")

        self.verticalLayout_2.addWidget(self.message)

        self.username_field = QLineEdit(SignupForm)
        self.username_field.setObjectName(u"username_field")
        self.username_field.setDragEnabled(True)

        self.verticalLayout_2.addWidget(self.username_field)

        self.email_field = QLineEdit(SignupForm)
        self.email_field.setObjectName(u"email_field")

        self.verticalLayout_2.addWidget(self.email_field)

        self.passwors1_field = QLineEdit(SignupForm)
        self.passwors1_field.setObjectName(u"passwors1_field")
        self.passwors1_field.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.passwors1_field)

        self.password2_field = QLineEdit(SignupForm)
        self.password2_field.setObjectName(u"password2_field")
        self.password2_field.setAcceptDrops(False)
        self.password2_field.setDragEnabled(True)

        self.verticalLayout_2.addWidget(self.password2_field)

        self.signup_btn = QPushButton(SignupForm)
        self.signup_btn.setObjectName(u"signup_btn")
        self.signup_btn.setMinimumSize(QSize(288, 0))

        self.verticalLayout_2.addWidget(self.signup_btn)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.close_btn = QPushButton(SignupForm)
        self.close_btn.setObjectName(u"close_btn")
        self.close_btn.setMinimumSize(QSize(140, 0))

        self.horizontalLayout_2.addWidget(self.close_btn)

        self.reset_btn = QPushButton(SignupForm)
        self.reset_btn.setObjectName(u"reset_btn")
        self.reset_btn.setMinimumSize(QSize(140, 0))

        self.horizontalLayout_2.addWidget(self.reset_btn)


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
        self.designation_label.setText(QCoreApplication.translate("SignupForm", u"Login As", None))
        self.designation_field.setItemText(0, QCoreApplication.translate("SignupForm", u"Student", None))
        self.designation_field.setItemText(1, QCoreApplication.translate("SignupForm", u"Faculty", None))
        self.designation_field.setItemText(2, QCoreApplication.translate("SignupForm", u"admin", None))

        self.message.setText(QCoreApplication.translate("SignupForm", u"af", None))
        self.username_field.setPlaceholderText(QCoreApplication.translate("SignupForm", u"Enter Username", None))
        self.email_field.setPlaceholderText(QCoreApplication.translate("SignupForm", u"Enter Email Id", None))
        self.passwors1_field.setPlaceholderText(QCoreApplication.translate("SignupForm", u"Password", None))
        self.password2_field.setPlaceholderText(QCoreApplication.translate("SignupForm", u"Retype Password", None))
        self.signup_btn.setText(QCoreApplication.translate("SignupForm", u"Signup", None))
        self.close_btn.setText(QCoreApplication.translate("SignupForm", u"Close", None))
        self.reset_btn.setText(QCoreApplication.translate("SignupForm", u"Reset Form", None))
    # retranslateUi

