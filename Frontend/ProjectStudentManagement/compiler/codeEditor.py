from PySide6.QtWidgets import QWidget, QApplication, QMainWindow, QPlainTextEdit
from compilerWin import Ui_compilerWin
import sys


class CodeEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_compilerWin()
        self.ui.setupUi(self)
        self.ui.tabWidget.children(1)
        # self.ui.textContainerField.LineWrapMode(
        #     self.ui.textContainerField.NoWrap)
        # self.ui.textContainerField.NoWrap = self.ui.textContainerField.LineWrapMode.NoWrap
        # print(self.ui.textContainerField.WidgetWidth)


class LineNumberField(QWidget):
    def __init__(self, parent):
        super().__init__(parent)


class EditorField(QPlainTextEdit):
    def __init__(self):
        super().__init__()
        self.lineNumberField = LineNumberField(self)


def main():
    app = QApplication(sys.argv)

    win = CodeEditor()
    win.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
