from PySide6 import QtWidgets
from .loginWidget import Ui_LoginForm
from .signupWidget import Ui_SignupForm

login_ui = Ui_LoginForm()
signup_ui = Ui_SignupForm()


class LoginWin(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()


class SignupWin(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()


class HomeWindow(QtWidgets.QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.loginWindow = LoginWin()
        login_ui.setupUi(self.loginWindow)
        self.signupWindow = SignupWin()
        signup_ui.setupUi(self.signupWindow)

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
