import email
from PySide6 import QtWidgets, QtCore
# from PySide6 import QtNetwork
import re
import requests
from .loginWidget import Ui_LoginForm
from .signupWidget import Ui_SignupForm
from home.ui_home import Ui_HomeForm

import sys
import time

# Multipart Data
# data = QtNetwork.QHttpMultiPart()
# textPart = QtNetwork.QHttpPart()
# textPart.setHeader(QtNetwork.QNetworkRequest.ContentDispositionHeader,
#                    "form-data; name=\"text\"")
# textPart.setBody("my text")
# data.append(textPart)


class LoginWin(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__()
        self._parent = parent
        self.login_ui = Ui_LoginForm()
        self.login_ui.setupUi(self)
        self.login_ui.close_btn.clicked.connect(self.close)
        self.login_ui.login_btn.clicked.connect(self._parent.login)


class SignupWin(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__()
        self._parent = parent
        self.signup_ui = Ui_SignupForm()
        self.signup_ui.setupUi(self)
        self.signup_ui.close_btn.clicked.connect(self.close)
        self.signup_ui.signup_btn.clicked.connect(self._parent.signup)


class HomeWindow(QtWidgets.QWidget):
    def __init__(self, parent) -> None:
        super(HomeWindow, self).__init__()
        self._parent = parent
        self.home_ui = Ui_HomeForm()
        self.signupWindow = SignupWin(self)
        self.loginWindow = LoginWin(self)

        self.home_ui.setupUi(self)
        self.home_ui.login.clicked.connect(self.openLoginWin)
        self.home_ui.signup.clicked.connect(self.openSignupWin)

        # self.url = QtCore.QUrl("http://127.0.0.1:8000")
        # self.request = QtNetwork.QNetworkRequest()
        # self.request.setUrl(self.url)
        # self.network_manager = QtNetwork.QNetworkAccessManager()
        # self.response = None
        # self.signup_ui.setupUi(self.signupWindow)

    def openLoginWin(self):
        if not self.signupWindow.isVisible():
            self.loginWindow.setMaximumSize(400, 500)
            self.loginWindow.login_ui.message.setVisible(False)
            self.loginWindow.login_ui.message.setEnabled(False)
            self.loginWindow.show()

    def openSignupWin(self):
        if not self.loginWindow.isVisible():
            self.signupWindow.setMaximumSize(400, 500)
            self.signupWindow.signup_ui.message.setEnabled(False)
            self.signupWindow.signup_ui.message.setVisible(False)
            self.signupWindow.show()

    def closeEvent(self, event):
        if self.loginWindow:
            self.loginWindow.close()
        if self.signupWindow:
            self.signupWindow.close()

    def login(self):
        email = None
        designation = 'student'
        username = self.loginWindow.login_ui.username_field.text()
        passwd = self.loginWindow.login_ui.password_field.text()
        if username == '' or passwd == '':
            self.loginWindow.login_ui.message.setVisible(True)
            self.loginWindow.login_ui.message.setEnabled(True)
            self.loginWindow.login_ui.message.setText(
                "No Field cannot be empty")
        elif re.fullmatch("[a-z][a-z0-9]*@[a-z0-9]*\.[A-Za-z]*", username):
            email = username
            data = {
                "designation": designation,
                "email": email,
                "passwd": passwd,
            }
        else:
            data = {
                "designation": designation,
                "username": username,
                "passwd": passwd,
            }
        response = requests.post(
            "http://127.0.0.1:8000/api/student/login", json=data)
        data = response.json()
        if data['success']:
            self._parent.profile.show()
            self.close()
        else:
            self.loginWindow.login_ui.message.setVisible(True)
            self.loginWindow.login_ui.message.setEnabled(True)
            self.loginWindow.login_ui.message.setText(data["message"])

    def signup(self):
        designation = 'student'
        email = self.signupWindow.signup_ui.email_field.text()
        username = self.signupWindow.signup_ui.username_field.text()
        passwd1 = self.signupWindow.signup_ui.password1_field.text()
        passwd2 = self.signupWindow.signup_ui.password2_field.text()
        if email == '' or username == '' or passwd1 == '' or passwd2 == '':
            self.signupWindow.signup_ui.message.setVisible(True)
            self.signupWindow.signup_ui.message.setEnabled(True)
            self.signupWindow.signup_ui.message.setText(
                "No Field cannot be empty")
        elif not re.fullmatch("[a-z][a-z0-9]*@[a-z0-9]*\.[A-Za-z]*", email):
            self.signupWindow.signup_ui.message.setVisible(True)
            self.signupWindow.signup_ui.message.setEnabled(True)
            self.signupWindow.signup_ui.message.setText(
                "Enter a correct Email")
        elif passwd1 != passwd2:
            self.signupWindow.signup_ui.message.setVisible(True)
            self.signupWindow.signup_ui.message.setEnabled(True)
            self.signupWindow.signup_ui.message.setText(
                "Password Mismatch")
        else:
            data = {
                "designation": designation,
                "email": email,
                "username": username,
                "passwd": passwd1


            }
            response = requests.post(
                "http://127.0.0.1:8000/api/student/signup", json=data)
            data = response.json()
            if data['success']:
                self.signupWindow.close()
                self.openLoginWin()
            else:
                self.signupWindow.signup_ui.message.setVisible(True)
                self.signupWindow.signup_ui.message.setEnabled(True)
                self.signupWindow.signup_ui.message.setText(data['message'])
