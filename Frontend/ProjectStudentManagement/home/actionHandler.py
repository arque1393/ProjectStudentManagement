from home.loginWidget import Ui_LoginForm
from PySide6.QtWidgets import QWidget
from PySide6 import QtCore
import time


@QtCore.Slot()
def openLoginWin():
    win = QWidget()
    ui = Ui_LoginForm()
    ui.setupUi(win)
    win.show()


def openSignupWin():
    pass
