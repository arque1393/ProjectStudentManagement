from PySide6.QtWidgets import QWidget, QApplication, QMainWindow, QPlainTextEdit
from compilerWin import Ui_compilerWin
import sys


class LineNumberField(QWidget):
    def __init__(self, parent):
        super().__init__(parent)


class EditorField(QPlainTextEdit):
    def __init__(self):
        super().__init__()
        self.lineNumberField = LineNumberField(self)


class CodeEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_compilerWin()
        self.ui.setupUi(self)
        self.ui.tabWidget.addTab(EditorField(), "new Tab")
        # self.ui.tabWidget.clear()
        self.ui.tabWidget.removeTab(1)
        self.ui.tabWidget.removeTab(0)
        self.ui.tabWidget.removeTab(0)
        # self.textEdit = EditorField(self.ui.tabWidget.children()[0])
        # self.ui.textContainerField.LineWrapMode(
        #     self.ui.textContainerField.NoWrap)
        # self.ui.textContainerField.NoWrap = self.ui.textContainerField.LineWrapMode.NoWrap
        # print(self.ui.textContainerField.WidgetWidth)


def main():
    app = QApplication(sys.argv)

    win = CodeEditor()
    win.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
