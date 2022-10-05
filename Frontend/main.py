import sys
from base import Home
from PySide6 import QtWidgets


def main():
    app = QtWidgets.QApplication(sys.argv)
    win = Home()
    win.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
