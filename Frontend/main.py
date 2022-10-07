import sys


from PySide6 import QtWidgets
from home.home import HomeWindow


class MainApp:
    def __init__(self) -> None:
        self.home = HomeWindow(self)
        self.profile = QtWidgets.QWidget()


def main():
    app = QtWidgets.QApplication(sys.argv)

    win = MainApp()
    win.home.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
