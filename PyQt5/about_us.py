# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\about_us.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AboutUS(object):

    def setupUi(self, AboutUS):
        AboutUS.setObjectName("AboutUS")
        AboutUS.resize(661, 521)
        self.centralwidget = QtWidgets.QWidget(AboutUS)
        self.centralwidget.setObjectName("centralwidget")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(190, 260, 321, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(290, 220, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_0 = QtWidgets.QLabel(self.centralwidget)
        self.label_0.setGeometry(QtCore.QRect(160, 30, 341, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_0.setFont(font)
        self.label_0.setObjectName("label_0")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(220, 170, 231, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(80, 90, 551, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_1.setFont(font)
        self.label_1.setObjectName("label_1")
        AboutUS.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(AboutUS)
        self.statusbar.setObjectName("statusbar")
        AboutUS.setStatusBar(self.statusbar)

        self.retranslateUi(AboutUS)
        QtCore.QMetaObject.connectSlotsByName(AboutUS)

    def retranslateUi(self, AboutUS):
        _translate = QtCore.QCoreApplication.translate
        AboutUS.setWindowTitle(_translate("AboutUS", "MainWindow"))
        self.label_4.setText(_translate("AboutUS", "Andres Alejandro Duque Tauta 160003812\n"
"Fredy Segura 160003830"))
        self.label_3.setText(_translate("AboutUS", "Integrantes:"))
        self.label_0.setText(_translate("AboutUS", "CALCULADORA DE METODOS NUMERICOS"))
        self.label_2.setText(_translate("AboutUS", "Profesor: Camilo Torres Gomez"))
        self.label_1.setText(_translate("AboutUS", "Este proyecto implementa diversos metodos observados en el transcurso \n"
"de la materia Metodos Numericos"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AboutUS = QtWidgets.QMainWindow()
    ui = Ui_AboutUS()
    ui.setupUi(AboutUS)
    AboutUS.show()
    sys.exit(app.exec_())
