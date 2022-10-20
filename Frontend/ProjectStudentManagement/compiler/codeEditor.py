from PySide6.QtWidgets import QWidget, QApplication, QMainWindow, QPlainTextEdit, QFileDialog
from compilerWin import Ui_compilerWin
from PySide6.QtCore import Slot
import sys
import os
import subprocess


class LineNumberField(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.setMinimumWidth(40)


class EditorField(QPlainTextEdit):
    def __init__(self):
        super().__init__()
        self.lineNumberField = LineNumberField(self)


class CodeEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        # self.ui = MyUI()
        self.ui = Ui_compilerWin()
        self.ui.setupUi(self)
        self.ui.tabWidget.removeTab(1)
        self.ui.tabWidget.removeTab(0)
        self.openedFileList = {}
        self.openedFileSaveList = {}

        # Button Connection
        self.ui.newBtn.clicked.connect(self.createNewFile)
        self.ui.openBtn.clicked.connect(self.openFile)
        self.ui.compileBtn.clicked.connect(self.compileFile)
        self.ui.executeBtn.clicked.connect(self.executeFile)
        self.ui.tabWidget.tabCloseRequested.connect(
            lambda index: self.ui.tabWidget.removeTab(index))

    def createNewFile(self):
        widget = EditorField()
        self.ui.tabWidget.addTab(
            widget, f"untitled{self.ui.tabWidget.count()-len(self.openedFileList)}")

    def openFile(self):
        filePath = QFileDialog.getOpenFileName(
            self, 'open file')[0]

        if filePath != '':
            self.openedFileList[self.ui.tabWidget.count()] = filePath
            self.openedFileSaveList[self.ui.tabWidget.count()] = True
            filename = os.path.basename(filePath)
            f = open(filePath, "r")
            content = f.read()
            widget = EditorField()
            widget.setPlainText(content)
            self.ui.tabWidget.addTab(widget, filename)

    def saveFile(self):
        if self.is_not_save(self):
            QFileDialog.getSaveFileName(self, 'save file')

    def is_not_save(self):
        return True

    def compileFile(self):
        lang_to_extension = {'Python': 'py',
                             'C': 'c', 'C++': 'cpp', 'Java': 'java'}

        lang = self.ui.selectBtn.currentText()
        try:
            currentFileIndex = self.ui.tabWidget.currentIndex()
            path = self.openedFileList[currentFileIndex]
            if self.openedFileSaveList[currentFileIndex]:
                raise "File Not save"
            name, extension = os.path.splitext(path)
            extension = extension[1:]
            if extension == lang_to_extension[lang]:
                if extension == 'py':
                    print("No Compilation needed")
                elif extension == 'java':
                    os.system(f"javac {path}")
                elif extension == 'c':
                    os.system(f"gcc {path} -o {name}.out ")
                elif extension == 'cpp':
                    os.system(f"g++ {path} -o {name}.out ")
            else:
                print(
                    f"selected Language id {lang} please check the extension")
        except:
            print("Open Not save Dialog")

    def executeFile(self):
        lang_to_extension = {'Python': 'py',
                             'C': 'c', 'C++': 'cpp', 'Java': 'java'}

        lang = self.ui.selectBtn.currentText()
        try:
            currentFileIndex = self.ui.tabWidget.currentIndex()
            path = self.openedFileList[currentFileIndex]
            if not self.openedFileSaveList[currentFileIndex]:
                raise "File Not save"
            name, extension = os.path.splitext(path)
            extension = extension[1:]
            if extension == lang_to_extension[lang]:
                if extension == 'py':
                    subprocess.call(['xterm', '-e', f'python {path};read z'])
                elif extension == 'java':
                    subprocess.call(['xterm', '-e', f'java {name};read z'])

                elif extension == 'c' or extension == 'cpp':
                    subprocess.call(['xterm', '-e', f"{name}.out; read z"])

            else:
                print(
                    f"selected Language id {lang} please check the extension")
        except BaseException as ex:
            print("Open Not save Dialog")
            print(ex)


def main():
    app = QApplication(sys.argv)

    win = CodeEditor()
    win.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
