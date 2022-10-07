from PySide6 import QtWidgets, QtCore
from .loginWidget import Ui_LoginForm
from .signupWidget import Ui_SignupForm
from home.ui_home import Ui_HomeForm

import sys


class LoginWin(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__()
        self._parent = parent
        self.login_ui = Ui_LoginForm()
        self.login_ui.setupUi(self)
        self.login_ui.close_btn.clicked.connect(self.close)
        self.login_ui.login_btn.clicked.connect(self._parent.login)


class SignupWin(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__()
        self._parent = parent
        self.signup_ui = Ui_SignupForm()
        self.signup_ui.setupUi(self)
        self.signup_ui.close_btn.clicked.connect(self.close)
        self.signup_ui.signup_btn.clicked.connect(self._parent.signup)


class HomeWindow(QtWidgets.QWidget):
    def __init__(self, parent) -> None:
        super(HomeWindow, self).__init__()
        self._parent = parent
        self.home_ui = Ui_HomeForm()
        self.signupWindow = SignupWin(self)
        self.loginWindow = LoginWin(self)

        self.home_ui.setupUi(self)
        self.home_ui.login.clicked.connect(self.openLoginWin)
        self.home_ui.signup.clicked.connect(self.openSignupWin)
        # self.signup_ui.setupUi(self.signupWindow)

    def openLoginWin(self):
        if not self.signupWindow.isVisible():
            self.loginWindow.setMaximumSize(400, 500)

            self.loginWindow.show()

    def openSignupWin(self):
        if not self.loginWindow.isVisible():
            self.signupWindow.setMaximumSize(400, 500)
            self.signupWindow.show()

    def closeEvent(self, event):
        if self.loginWindow:
            self.loginWindow.close()
        if self.signupWindow:
            self.signupWindow.close()

    def login(self):
        print("Loggin")

    def signup(self):
        self._parent.profile.show()
        self.close()
