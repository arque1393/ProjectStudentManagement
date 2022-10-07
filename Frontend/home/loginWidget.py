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
        self.designation_label = QLabel(LoginForm)
        self.designation_label.setObjectName(u"designation_label")
        font1 = QFont()
        self.designation_label.setFont(font1)

        self.horizontalLayout.addWidget(self.designation_label)

        self.designation_field = QComboBox(LoginForm)
        self.designation_field.addItem("")
        self.designation_field.addItem("")
        self.designation_field.addItem("")
        self.designation_field.setObjectName(u"designation_field")
        self.designation_field.setMinimumSize(QSize(140, 0))

        self.horizontalLayout.addWidget(self.designation_field)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.username_label = QLabel(LoginForm)
        self.username_label.setObjectName(u"username_label")
        self.username_label.setFont(font1)

        self.horizontalLayout_3.addWidget(self.username_label)

        self.username_field = QLineEdit(LoginForm)
        self.username_field.setObjectName(u"username_field")

        self.horizontalLayout_3.addWidget(self.username_field)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.password_label = QLabel(LoginForm)
        self.password_label.setObjectName(u"password_label")
        self.password_label.setFont(font1)

        self.horizontalLayout_4.addWidget(self.password_label)

        self.password_field = QLineEdit(LoginForm)
        self.password_field.setObjectName(u"password_field")

        self.horizontalLayout_4.addWidget(self.password_field)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.login_btn = QPushButton(LoginForm)
        self.login_btn.setObjectName(u"login_btn")
        self.login_btn.setMinimumSize(QSize(288, 0))

        self.verticalLayout_2.addWidget(self.login_btn)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.close_btn = QPushButton(LoginForm)
        self.close_btn.setObjectName(u"close_btn")
        self.close_btn.setMinimumSize(QSize(140, 0))

        self.horizontalLayout_2.addWidget(self.close_btn)

        self.reset_btn = QPushButton(LoginForm)
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


        self.retranslateUi(LoginForm)

        QMetaObject.connectSlotsByName(LoginForm)
    # setupUi

    def retranslateUi(self, LoginForm):
        LoginForm.setWindowTitle(QCoreApplication.translate("LoginForm", u"Form", None))
        self.label.setText(QCoreApplication.translate("LoginForm", u"Login", None))
        self.designation_label.setText(QCoreApplication.translate("LoginForm", u"Login As", None))
        self.designation_field.setItemText(0, QCoreApplication.translate("LoginForm", u"Student", None))
        self.designation_field.setItemText(1, QCoreApplication.translate("LoginForm", u"Faculty", None))
        self.designation_field.setItemText(2, QCoreApplication.translate("LoginForm", u"admin", None))

        self.username_label.setText(QCoreApplication.translate("LoginForm", u"Username", None))
        self.password_label.setText(QCoreApplication.translate("LoginForm", u"Password ", None))
        self.login_btn.setText(QCoreApplication.translate("LoginForm", u"Login", None))
        self.close_btn.setText(QCoreApplication.translate("LoginForm", u"Close", None))
        self.reset_btn.setText(QCoreApplication.translate("LoginForm", u"Reset Form", None))
    # retranslateUi

