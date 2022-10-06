# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'home.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_HomeForm(object):
    def setupUi(self, HomeForm):
        if not HomeForm.objectName():
            HomeForm.setObjectName(u"HomeForm")
        HomeForm.resize(1275, 662)
        HomeForm.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(HomeForm)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(HomeForm)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"NotoSerifTamilSlanted Medium"])
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setStyleSheet(u"QLabel{\n"
"		color:white;\n"
"		background-color:rgb(53, 134, 255);\n"
"		border-radius: 20px;\n"
"        text-align: center;\n"
"		padding: 0 40px;\n"
"}\n"
"\n"
"")

        self.horizontalLayout.addWidget(self.label)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.login_signup_layout = QHBoxLayout()
        self.login_signup_layout.setObjectName(u"login_signup_layout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.login_signup_layout.addItem(self.horizontalSpacer_2)

        self.signup = QPushButton(HomeForm)
        self.signup.setObjectName(u"signup")
        self.signup.setStyleSheet(u"\n"
"QPushButton{\n"
"		height:40px;\n"
"		width:100px;\n"
"	\n"
"		font: 500 14pt \"Noto Sans Gujarati UI Medium\";\n"
"        background-color: #7b38d8;\n"
"        border-radius: 20px;\n"
"        border: 4px double #cccccc;\n"
"        color: #eeeeee;\n"
"        text-align: center;\n"
"        font-size: 28px;\n"
"        padding: 5px 10px;  \n"
"        margin: 5px;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"		 background-color: #9843e2;\n"
"}\n"
"QPushButton:pressed{\n"
"		 background-color: #b853f2;\n"
"}")

        self.login_signup_layout.addWidget(self.signup)

        self.login = QPushButton(HomeForm)
        self.login.setObjectName(u"login")
        self.login.setStyleSheet(u"QPushButton{\n"
"		height:40px;\n"
"		width:100px;\n"
"	\n"
"		font: 500 14pt \"Noto Sans Gujarati UI Medium\";\n"
"        background-color: #7b38d8;\n"
"        border-radius: 20px;\n"
"        border: 4px double #cccccc;\n"
"        color: #eeeeee;\n"
"        text-align: center;\n"
"        font-size: 28px;\n"
"        padding: 5px 10px;  \n"
"        margin: 5px;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"		 background-color: #9843e2;\n"
"}\n"
"QPushButton:pressed{\n"
"		 background-color: #b853f2;\n"
"}")

        self.login_signup_layout.addWidget(self.login)


        self.verticalLayout_2.addLayout(self.login_signup_layout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.horizontalLayout_3.addItem(self.verticalSpacer)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)


        self.retranslateUi(HomeForm)

        QMetaObject.connectSlotsByName(HomeForm)
    # setupUi

    def retranslateUi(self, HomeForm):
        HomeForm.setWindowTitle(QCoreApplication.translate("HomeForm", u"Form", None))
        self.label.setText(QCoreApplication.translate("HomeForm", u"System to manage Instritute", None))
        self.signup.setText(QCoreApplication.translate("HomeForm", u"SignUp", None))
        self.login.setText(QCoreApplication.translate("HomeForm", u"Login", None))
    # retranslateUi

