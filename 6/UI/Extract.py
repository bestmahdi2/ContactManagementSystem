# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Extract.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogEx(object):
    def setupUi(self, DialogEx):
        DialogEx.setObjectName("DialogEx")
        DialogEx.resize(630, 737)
        DialogEx.setStyleSheet("background-color:#676767")
        self.label_3 = QtWidgets.QLabel(DialogEx)
        self.label_3.setGeometry(QtCore.QRect(10, 150, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:#FFDB00")
        self.label_3.setFrameShape(QtWidgets.QFrame.Box)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.textBrowser = QtWidgets.QTextBrowser(DialogEx)
        self.textBrowser.setGeometry(QtCore.QRect(11, 191, 599, 150))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.textBrowser.setFont(font)
        self.textBrowser.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.textBrowser.setStyleSheet("color:white")
        self.textBrowser.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser.setReadOnly(False)
        self.textBrowser.setObjectName("textBrowser")
        self.label_4 = QtWidgets.QLabel(DialogEx)
        self.label_4.setGeometry(QtCore.QRect(10, 460, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:#FFDB00")
        self.label_4.setFrameShape(QtWidgets.QFrame.Box)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.text_2 = QtWidgets.QTextBrowser(DialogEx)
        self.text_2.setGeometry(QtCore.QRect(10, 460, 291, 192))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.text_2.setFont(font)
        self.text_2.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.text_2.setReadOnly(True)
        self.text_2.setObjectName("text_2")
        self.label_2 = QtWidgets.QLabel(DialogEx)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 611, 61))
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:#FFDB00")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.text_3 = QtWidgets.QTextBrowser(DialogEx)
        self.text_3.setGeometry(QtCore.QRect(320, 460, 291, 192))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.text_3.setFont(font)
        self.text_3.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.text_3.setReadOnly(True)
        self.text_3.setObjectName("text_3")
        self.label_5 = QtWidgets.QLabel(DialogEx)
        self.label_5.setGeometry(QtCore.QRect(320, 460, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color:#FFDB00")
        self.label_5.setFrameShape(QtWidgets.QFrame.Box)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(DialogEx)
        self.pushButton.setGeometry(QtCore.QRect(500, 370, 111, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color:#7018EB;color:white")
        self.pushButton.setObjectName("pushButton")
        self.text = QtWidgets.QTextBrowser(DialogEx)
        self.text.setGeometry(QtCore.QRect(10, 150, 601, 192))
        self.text.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.text.setReadOnly(True)
        self.text.setObjectName("text")
        self.textBrowser_2 = QtWidgets.QTextBrowser(DialogEx)
        self.textBrowser_2.setGeometry(QtCore.QRect(11, 501, 289, 150))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.textBrowser_2.setFont(font)
        self.textBrowser_2.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.textBrowser_2.setStyleSheet("color:white")
        self.textBrowser_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser_2.setReadOnly(True)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textBrowser_3 = QtWidgets.QTextBrowser(DialogEx)
        self.textBrowser_3.setGeometry(QtCore.QRect(321, 501, 289, 150))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.textBrowser_3.setFont(font)
        self.textBrowser_3.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.textBrowser_3.setStyleSheet("color:white")
        self.textBrowser_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser_3.setReadOnly(True)
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.text.raise_()
        self.textBrowser.raise_()
        self.text_2.raise_()
        self.label_3.raise_()
        self.label_2.raise_()
        self.label_4.raise_()
        self.text_3.raise_()
        self.label_5.raise_()
        self.pushButton.raise_()
        self.textBrowser_2.raise_()
        self.textBrowser_3.raise_()

        self.retranslateUi(DialogEx)
        QtCore.QMetaObject.connectSlotsByName(DialogEx)

    def retranslateUi(self, DialogEx):
        _translate = QtCore.QCoreApplication.translate
        DialogEx.setWindowTitle(_translate("DialogEx", "Dialog"))
        self.label_3.setText(_translate("DialogEx", "Input:"))
        self.textBrowser.setPlaceholderText(_translate("DialogEx", "Enter text ..."))
        self.label_4.setText(_translate("DialogEx", "Names:"))
        self.label_2.setText(_translate("DialogEx", "Contact Manageing System"))
        self.label_5.setText(_translate("DialogEx", "Numbers:"))
        self.pushButton.setText(_translate("DialogEx", "Extract"))
        self.textBrowser_2.setPlaceholderText(_translate("DialogEx", "Results ..."))
        self.textBrowser_3.setPlaceholderText(_translate("DialogEx", "Results ..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DialogEx = QtWidgets.QDialog()
    ui = Ui_DialogEx()
    ui.setupUi(DialogEx)
    DialogEx.show()
    sys.exit(app.exec_())