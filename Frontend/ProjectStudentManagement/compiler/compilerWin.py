# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'compilerWin.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QTabWidget,
    QVBoxLayout, QWidget)

class Ui_compilerWin(object):
    def setupUi(self, compilerWin):
        if not compilerWin.objectName():
            compilerWin.setObjectName(u"compilerWin")
        compilerWin.resize(1019, 640)
        compilerWin.setStyleSheet(u"QWidget{\n"
"	background-color:rgb(240,240, 255);\n"
"	\n"
"}\n"
"\n"
"QMainWindow{\n"
"	background-color:rgb(50, 0, 90);\n"
"}\n"
"QTabWidget{\n"
"	background-color:rgb(85, 0, 127);\n"
"	color:rgb(255, 255, 255)\n"
"}\n"
"QMenuBar{\n"
"	background-color:rgb(50, 0, 90);\n"
"	color:white;\n"
"	font-weight:bold;\n"
"}\n"
"QLabel{\n"
"	background-color:rgb(50, 0, 90);\n"
"	color:white;\n"
"	padding:2%;\n"
"}\n"
"QStatusBar{\n"
"	background-color:rgb(85, 0, 127)\n"
"}")
        self.actionNew = QAction(compilerWin)
        self.actionNew.setObjectName(u"actionNew")
        self.actionOprn = QAction(compilerWin)
        self.actionOprn.setObjectName(u"actionOprn")
        self.actionSave = QAction(compilerWin)
        self.actionSave.setObjectName(u"actionSave")
        self.actionSave_as = QAction(compilerWin)
        self.actionSave_as.setObjectName(u"actionSave_as")
        self.actionUndo = QAction(compilerWin)
        self.actionUndo.setObjectName(u"actionUndo")
        self.actionRedo = QAction(compilerWin)
        self.actionRedo.setObjectName(u"actionRedo")
        self.actionCut = QAction(compilerWin)
        self.actionCut.setObjectName(u"actionCut")
        self.actionCopy = QAction(compilerWin)
        self.actionCopy.setObjectName(u"actionCopy")
        self.actionPest = QAction(compilerWin)
        self.actionPest.setObjectName(u"actionPest")
        self.actionCompile = QAction(compilerWin)
        self.actionCompile.setObjectName(u"actionCompile")
        self.actionExecute = QAction(compilerWin)
        self.actionExecute.setObjectName(u"actionExecute")
        self.actionAbou_Us = QAction(compilerWin)
        self.actionAbou_Us.setObjectName(u"actionAbou_Us")
        self.centralwidget = QWidget(compilerWin)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.horizontalLayout_3 = QHBoxLayout(self.tab)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.horizontalLayout_4 = QHBoxLayout(self.tab_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.tabWidget.addTab(self.tab_2, "")

        self.horizontalLayout.addWidget(self.tabWidget)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.verticalLayout_2.addWidget(self.pushButton_4)

        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.verticalLayout_2.addWidget(self.pushButton_3)

        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.verticalLayout_2.addWidget(self.pushButton_5)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.verticalLayout_2.addWidget(self.comboBox)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_2.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout_2.addWidget(self.pushButton_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        compilerWin.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(compilerWin)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1019, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuRun = QMenu(self.menubar)
        self.menuRun.setObjectName(u"menuRun")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        compilerWin.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(compilerWin)
        self.statusbar.setObjectName(u"statusbar")
        compilerWin.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuRun.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOprn)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_as)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPest)
        self.menuRun.addAction(self.actionCompile)
        self.menuRun.addAction(self.actionExecute)
        self.menuHelp.addAction(self.actionAbou_Us)

        self.retranslateUi(compilerWin)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(compilerWin)
    # setupUi

    def retranslateUi(self, compilerWin):
        compilerWin.setWindowTitle(QCoreApplication.translate("compilerWin", u"MainWindow", None))
        self.actionNew.setText(QCoreApplication.translate("compilerWin", u"New", None))
        self.actionOprn.setText(QCoreApplication.translate("compilerWin", u"Oprn", None))
        self.actionSave.setText(QCoreApplication.translate("compilerWin", u"Save", None))
        self.actionSave_as.setText(QCoreApplication.translate("compilerWin", u"Save As", None))
        self.actionUndo.setText(QCoreApplication.translate("compilerWin", u"Undo", None))
        self.actionRedo.setText(QCoreApplication.translate("compilerWin", u"Redo", None))
        self.actionCut.setText(QCoreApplication.translate("compilerWin", u"Cut", None))
        self.actionCopy.setText(QCoreApplication.translate("compilerWin", u"Copy", None))
        self.actionPest.setText(QCoreApplication.translate("compilerWin", u"Pest", None))
        self.actionCompile.setText(QCoreApplication.translate("compilerWin", u"Compile", None))
        self.actionExecute.setText(QCoreApplication.translate("compilerWin", u"Execute", None))
        self.actionAbou_Us.setText(QCoreApplication.translate("compilerWin", u"Abou Us", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("compilerWin", u"Tab 1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("compilerWin", u"Tab 2", None))
        self.label.setText(QCoreApplication.translate("compilerWin", u"File", None))
        self.pushButton_4.setText(QCoreApplication.translate("compilerWin", u"New", None))
        self.pushButton_3.setText(QCoreApplication.translate("compilerWin", u"Open", None))
        self.pushButton_5.setText(QCoreApplication.translate("compilerWin", u"Save", None))
        self.label_2.setText(QCoreApplication.translate("compilerWin", u"Compiler", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("compilerWin", u"Java", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("compilerWin", u"C", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("compilerWin", u"C++", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("compilerWin", u"Python", None))

        self.pushButton.setText(QCoreApplication.translate("compilerWin", u"Compile", None))
        self.pushButton_2.setText(QCoreApplication.translate("compilerWin", u"Execute", None))
        self.menuFile.setTitle(QCoreApplication.translate("compilerWin", u"File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("compilerWin", u"Edit", None))
        self.menuRun.setTitle(QCoreApplication.translate("compilerWin", u"Run", None))
        self.menuHelp.setTitle(QCoreApplication.translate("compilerWin", u"Help", None))
    # retranslateUi

