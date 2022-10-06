from PySide6 import QtWidgets
from .loginWidget import Ui_LoginForm

login_ui = Ui_LoginForm()


class HomeWindow(QtWidgets.QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.loginWindow = None
        self.signupWindow = None

    def openLoginWin(self):
        self.loginWindow = QtWidgets.QWidget()
        self.loginWindow.setMaximumSize(400, 500)
        login_ui.setupUi(self.loginWindow)
        self.loginWindow.show()

    def closeEvent(self, event):
        if self.loginWindow:
            self.loginWindow.close()
