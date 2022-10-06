import sys

from home.ui_home import Ui_HomeForm
from PySide6 import QtWidgets
from home.home import HomeWindow

home_ui = Ui_HomeForm()


def main():
    app = QtWidgets.QApplication(sys.argv)
    win = HomeWindow()
    home_ui.setupUi(win)
    win.show()
    home_ui.login.clicked.connect(win.openLoginWin)
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
