# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

import sys
import os
import MovieSelector

import gspread
from oauth2client.service_account import ServiceAccountCredentials

import random


class Ui_Application(object):
    def setupUi(self, Application):
        Application.setObjectName("Application")
        Application.resize(504, 417)
        self.title = QtWidgets.QLabel(Application)
        self.title.setGeometry(QtCore.QRect(140, 10, 221, 51))
        self.title.setObjectName("title")
        self.label1 = QtWidgets.QLabel(Application)
        self.label1.setGeometry(QtCore.QRect(50, 80, 21, 31))
        self.label1.setObjectName("label1")
        self.label2 = QtWidgets.QLabel(Application)
        self.label2.setGeometry(QtCore.QRect(50, 120, 21, 31))
        self.label2.setObjectName("label2")
        self.label3 = QtWidgets.QLabel(Application)
        self.label3.setGeometry(QtCore.QRect(50, 160, 21, 31))
        self.label3.setObjectName("label3")
        self.label4 = QtWidgets.QLabel(Application)
        self.label4.setGeometry(QtCore.QRect(50, 200, 21, 31))
        self.label4.setObjectName("label4")
        self.label5 = QtWidgets.QLabel(Application)
        self.label5.setGeometry(QtCore.QRect(50, 240, 21, 31))
        self.label5.setObjectName("label5")
        self.rollbutton = QtWidgets.QPushButton(Application)
        self.rollbutton.setGeometry(QtCore.QRect(210, 320, 80, 24))
        self.rollbutton.setObjectName("rollbutton")
        self.movie1 = QtWidgets.QLineEdit(Application)
        self.movie1.setGeometry(QtCore.QRect(80, 80, 371, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.movie1.setFont(font)
        self.movie1.setText("")
        self.movie1.setReadOnly(True)
        self.movie1.setObjectName("movie1")
        self.movie2 = QtWidgets.QLineEdit(Application)
        self.movie2.setGeometry(QtCore.QRect(80, 120, 371, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.movie2.setFont(font)
        self.movie2.setText("")
        self.movie2.setReadOnly(True)
        self.movie2.setObjectName("movie2")
        self.movie3 = QtWidgets.QLineEdit(Application)
        self.movie3.setGeometry(QtCore.QRect(80, 160, 371, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.movie3.setFont(font)
        self.movie3.setText("")
        self.movie3.setReadOnly(True)
        self.movie3.setObjectName("movie3")
        self.movie4 = QtWidgets.QLineEdit(Application)
        self.movie4.setGeometry(QtCore.QRect(80, 200, 371, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.movie4.setFont(font)
        self.movie4.setText("")
        self.movie4.setReadOnly(True)
        self.movie4.setObjectName("movie4")
        self.movie5 = QtWidgets.QLineEdit(Application)
        self.movie5.setGeometry(QtCore.QRect(80, 240, 371, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.movie5.setFont(font)
        self.movie5.setText("")
        self.movie5.setReadOnly(True)
        self.movie5.setObjectName("movie5")

        self.rollbutton.clicked.connect(self.roll)

        self.retranslateUi(Application)
        QtCore.QMetaObject.connectSlotsByName(Application)

    def retranslateUi(self, Application):
        _translate = QtCore.QCoreApplication.translate
        Application.setWindowTitle(_translate("Application", "Application"))
        self.title.setText(_translate("Application", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt;\">Movie Selector</span></p></body></html>"))
        self.label1.setText(_translate("Application", "<html><head/><body><p><span style=\" font-size:20pt;\">1.</span></p></body></html>"))
        self.label2.setText(_translate("Application", "<html><head/><body><p><span style=\" font-size:20pt;\">2.</span></p></body></html>"))
        self.label3.setText(_translate("Application", "<html><head/><body><p><span style=\" font-size:20pt;\">3.</span></p></body></html>"))
        self.label4.setText(_translate("Application", "<html><head/><body><p><span style=\" font-size:20pt;\">4.</span></p></body></html>"))
        self.label5.setText(_translate("Application", "<html><head/><body><p><span style=\" font-size:20pt;\">5.</span></p></body></html>"))
        self.rollbutton.setText(_translate("Application", "Roll"))

    def roll(self):
        # define the scope
        scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

        # add credentials to the account
        creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)

        # authorize the clientsheet 
        client = gspread.authorize(creds)

        # get the instance of the Spreadsheet
        sheet = client.open('List of Suggested Movies')

        # get the first sheet of the Spreadsheet
        sheet_instance = sheet.get_worksheet(0)

        movies = []

        while len(movies) < 5:
            movie = sheet_instance.cell(col=2,row=random.randint(2,sheet_instance.col_count)).value
            if len(movies) == 5:
                break
            if movie in movies:
                movie = sheet_instance.cell(col=2,row=random.randint(2,sheet_instance.col_count)).value
            else:
                movies.append(movie) 
        
        self.movie1.setText(movies[0])
        self.movie2.setText(movies[1])
        self.movie3.setText(movies[2])
        self.movie4.setText(movies[3])
        self.movie5.setText(movies[4])
        movies = []
        return

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Application = QtWidgets.QWidget()
    ui = Ui_Application()
    ui.setupUi(Application)
    Application.show()
    sys.exit(app.exec_())
