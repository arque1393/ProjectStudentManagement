
from PySide6 import QtCore, QtWidgets, QtGui


class Home(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.btn3 = QtWidgets.QPushButton("Press Me")
        self.btn2 = QtWidgets.QPushButton("Press Me")
        self.btn1 = QtWidgets.QPushButton("Press Me")
        self.sub_layout = QtWidgets.QHBoxLayout()
        self.sub_layout.addWidget(self.btn1)
        self.sub_layout.addWidget(self.btn2)
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addLayout(self.sub_layout)
        self.layout.addWidget(self.btn3)
