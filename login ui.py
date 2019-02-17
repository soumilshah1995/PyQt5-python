# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets



class Ui_Form(object):

    def openwindow(self):

        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Page2()
        self.ui.setupUi(self.window)
        Form.hide()
        self.window.show()


    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(734, 428)
        self.label_username = QtWidgets.QLabel(Form)
        self.label_username.setGeometry(QtCore.QRect(160, 130, 121, 31))
        self.label_username.setObjectName("label_username")
        self.label_password = QtWidgets.QLabel(Form)
        self.label_password.setGeometry(QtCore.QRect(160, 190, 111, 21))
        self.label_password.setObjectName("label_password")
        self.txt_input_username = QtWidgets.QLineEdit(Form)
        self.txt_input_username.setGeometry(QtCore.QRect(380, 140, 201, 21))
        self.txt_input_username.setObjectName("txt_input_username")
        self.txt_input_password = QtWidgets.QLineEdit(Form)
        self.txt_input_password.setGeometry(QtCore.QRect(380, 190, 201, 21))
        self.txt_input_password.setObjectName("txt_input_password")
        self.btn_submit = QtWidgets.QPushButton(Form)
        self.btn_submit.setGeometry(QtCore.QRect(380, 240, 211, 32))
        self.btn_submit.setObjectName("btn_submit")
        self.text_title = QtWidgets.QTextEdit(Form)
        self.text_title.setGeometry(QtCore.QRect(60, 10, 629, 51))
        self.text_title.setObjectName("text_title")
        self.radioButton = QtWidgets.QRadioButton(Form)
        self.radioButton.setGeometry(QtCore.QRect(390, 290, 191, 20))
        self.radioButton.setObjectName("radioButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Login Page"))
        self.label_username.setText(_translate("Form", "Enter User Name"))
        self.label_password.setText(_translate("Form", "Enter Password"))
        self.btn_submit.setText(_translate("Form", "Submit"))



        self.text_title.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                   "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                   "p, li { white-space: pre-wrap; }\n"
                                                   "</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                                                   "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt; color:#cf0f39;\">Welcome to University of Briodgeport Login Page </span></p></body></html>"))
        self.radioButton.setText(_translate("Form", "Keep me Logged In"))

        self.btn_submit.clicked.connect(self.btn_submit_handler)


    def btn_submit_handler(self):
        val_pass = self.txt_input_password.text()
        val_username = self.txt_input_username.text()

        if val_pass == "admin" and val_username == "admin":
            print("welcome")
            print(self.radioButton.text())



            self.openwindow()

            #Page2.show()
            #self.ui.btn_sumbit.clicked.connect(lambda : self.ui.stackedWidget.setCurrentIndex(0))


class Ui_Page2(object):

    def openwindow(self):

        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Form()
        self.ui.setupUi(self.window)
        self.window.show()


    def setupUi(self, Page2):
        Page2.setObjectName("Page2")
        Page2.resize(400, 300)
        self.textEdit_pg2_txt = QtWidgets.QTextEdit(Page2)
        self.textEdit_pg2_txt.setGeometry(QtCore.QRect(90, 20, 171, 31))
        self.textEdit_pg2_txt.setObjectName("textEdit_pg2_txt")
        self.btn_back = QtWidgets.QPushButton(Page2)
        self.btn_back.setGeometry(QtCore.QRect(100, 100, 113, 32))
        self.btn_back.setObjectName("btn_back")

        self.retranslateUi(Page2)
        QtCore.QMetaObject.connectSlotsByName(Page2)

    def retranslateUi(self, Page2):
        _translate = QtCore.QCoreApplication.translate
        Page2.setWindowTitle(_translate("Page2", "Form"))
        self.textEdit_pg2_txt.setHtml(_translate("Page2", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                          "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                          "p, li { white-space: pre-wrap; }\n"
                                                          "</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                                                          "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Page 2</p></body></html>"))
        self.btn_back.setText(_translate("Page2", "Back"))
        self.btn_back.clicked.connect(self.button_handler_back)

    def button_handler_back(self):
        self.openwindow()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()

    sys.exit(app.exec_())
