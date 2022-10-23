import sys


from PySide6 import QtWidgets
from home.home import HomeWindow
from student.student_profile import StudentProfile
from compiler.codeEditor import CodeEditor


class MainApp:
    def __init__(self) -> None:
        self.is_loggedin = False
        self.loggedin_user_info = None
        self.home = HomeWindow(self)
        self.profile = StudentProfile(self)
        self.codeEditorWin = CodeEditor(self)


def main():
    app = QtWidgets.QApplication(sys.argv)

    win = MainApp()
    win.home.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
