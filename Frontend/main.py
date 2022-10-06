import sys

from home.home import Ui_HomeForm
from home.loginWidget import Ui_LoginForm
from PySide6 import QtWidgets

from home.actionHandler import openLoginWin
home_ui = Ui_HomeForm()
login_ui = Ui_LoginForm()


class Window(QtWidgets.QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.subWindow = None

    def close_all_child(self):
        if self.subWindow:
            self.subWindow.close()


def main():
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    app.aboutToQuit.connect(win.close_all_child)
    # login_win = QtWidgets.QWidget()
    win.subWindow = QtWidgets.QWidget()
    win.subWindow.setMaximumSize(400, 500)
    home_ui.setupUi(win)
    login_ui.setupUi(win.subWindow)
    win.show()

    home_ui.login.clicked.connect(win.subWindow.show)
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
