
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
        response = requests.post(endpoint, json=data)
        data2 = response.json()
        print(data2)
        # Bbutton
        # self.ui.backToHomeBtn
        self.ui.fileBrowseBtn.clicked.connect(self.fileBrowse)
        self.ui.updateBtn.clicked.connect(self.updataProfile)
        # self.ui.resetBtn
        # self.ui.fileHandlingBtn
        # Text Field
        self.ui.usernameValue.setText(data2['username'])
        self.ui.firstNameValue.setText(data2['first_name'])
        self.ui.lastNameValue.setText(data2['last_name'])
        self.ui.rollNoValue.setText(str(data2['roll_no']))
        self.ui.departmentValue.setText(data2['department'])
        # self.ui.contuctNoValue.setText(data2['contuct_no'])
        # self.ui.filePathLoaderValue
        self.show()

    def updataProfile(self):
        data = self._parent.loggedin_user_info
        data['update'] = True
        data['username'] = self.ui.usernameValue.text()
        data['first_name'] = self.ui.firstNameValue.text()
        data['last_name'] = self.ui.lastNameValue.text()
        data['roll_no'] = int(self.ui.rollNoValue.text())
        data['department'] = self.ui.departmentValue.text()
        response = requests.post(endpoint, json=data)

        # data['contuct_no'] = self.ui.contuctNoValue.text()
    def resetProfile(self):
        data = self._parent.loggedin_user_info
        data['update'] = False
        response = requests.post(endpoint, json=data)
        data2 = response.json()
        self.ui.usernameValue.setText(data2['username'])
        self.ui.firstNameValue.setText(data2['first_name'])
        self.ui.lastNameValue.setText(data2['last_name'])
        self.ui.rollNoValue.setText(str(data2['roll_no']))
        self.ui.departmentValue.setText(data2['department'])
        # self.ui.contuctNoValue.setText(data2['contuct_no'])

    def fileBrowse(self):
        filename = QtWidgets.QFileDialog.getOpenFileName(
            self, 'open file')
        self.ui.filePathLoaderValue.setText(filename)
