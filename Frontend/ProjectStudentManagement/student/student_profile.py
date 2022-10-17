from PySide6 import QtCore, QtWidgets
import requests
from .profile import Ui_studentProfile
endpoint = "http://127.0.0.1:8000/api/student/profile"


class StudentProfile(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__()
        self._parent = parent
        self.ui = Ui_studentProfile()
        self.ui.setupUi(self)

    def start(self):
        data = self._parent.loggedin_user_info
        data['update'] = False
        print(data)
        data2 = requests.post(endpoint, data=data).json()
        print(data2)
        # Bbutton
        # self.ui.backToHomeBtn
        # self.ui.fileBrowseBtn
        # self.ui.updateBtn
        # self.ui.resetBtn
        # self.ui.fileHandlingBtn
        # Text Field
        # self.ui.usernameValue.setText(data['username'])
        # self.ui.firstNameValue.setText(data['first_name'])
        # self.ui.lastNameValue.setText(data['last_name'])
        # self.ui.departmentValue.setText(data['roll_no'])
        # self.ui.rollNoValue.setText(data['department'])
        # self.ui.contuctNoValue.setText(data['contuct_no'])
        # self.ui.filePathLoaderValue
        self.show()
