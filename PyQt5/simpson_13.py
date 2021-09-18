# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\simpson_13.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


# from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets, QtPrintSupport


import numpy as np
from numpy import log as ln
import matplotlib.pyplot as plt
from matplotlib.pyplot import text

from funciones import *


class Ui_simpson_13(object):

    def press_it(self, f, a, b, n):
        f = f.text()
        a = a.text()
        b = b.text()
        n = n.text()
        print(f)
        print(a)
        print(b)
        print(n)

        if( len(f) and len(a) and len(b) and len(n)):
            print("podemos calcular")
            a = float(a)
            b = float(b)
            n = int(float(n))

           
            print( str(simpson_13_cal(f,a,b,n)))
            self.result_lbl.setText(str(simpson_13_cal(f,a,b,n)))
            

        else:
            print("no podemos calcular")

    
    def string2func(self, string):
        ''' evalua el string y retorna una funcion de x '''
        replacements = {
            'sin' : 'np.sin',
            'cos' : 'np.cos',
            'exp': 'np.exp',
            '^': '**',
            'pi': 'np.pi'
        }

        for old, new in replacements.items():
            string = string.replace(old, new)
        # print(string)
        # return string

        def func(x):
            return eval(string)

        return func

        
    def graph(self, f, a, b, n):   
        f = f.text()
        a = a.text()
        b = b.text()
        n = n.text()
        # x = np.linspace(a, b, n)

        print(f)
        print(a)
        print(b)
        print(n)

        if( len(f) and len(a) and len(b) and len(n)):
            print("podemos graficar")
            a = float(a)
            b = float(b)
            n = float(n)

            # x = np.linspace(a, b, n)
            x = np.linspace(a, b)
            func = self.string2func(f)
            plt.plot(x, func(x))
            plt.xlim(a, b)
            plt.show()
        else:
            print("no podemos graficar")

    def setupUi(self, simpson_13):
        simpson_13.setObjectName("simpson_13")
        simpson_13.resize(780, 724)
        self.centralwidget = QtWidgets.QWidget(simpson_13)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, -632, 743, 1336))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName("gridLayout")
        self.lbl_0 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_0.setFont(font)
        self.lbl_0.setObjectName("lbl_0")
        self.gridLayout.addWidget(self.lbl_0, 1, 0, 1, 1)
        self.result_lbl = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.result_lbl.setFont(font)
        self.result_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.result_lbl.setObjectName("result_lbl")
        self.gridLayout.addWidget(self.result_lbl, 21, 0, 1, 1)
        self.title_lbl = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.title_lbl.setFont(font)
        self.title_lbl.setTextFormat(QtCore.Qt.AutoText)
        self.title_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.title_lbl.setObjectName("title_lbl")
        self.gridLayout.addWidget(self.title_lbl, 0, 0, 1, 1)
        self.b_input = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.b_input.setFont(font)
        self.b_input.setText("")
        self.b_input.setObjectName("b_input")
        self.gridLayout.addWidget(self.b_input, 15, 0, 1, 1)
        self.n_input = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.n_input.setFont(font)
        self.n_input.setText("")
        self.n_input.setObjectName("n_input")
        self.gridLayout.addWidget(self.n_input, 18, 0, 1, 1)
        self.img_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.img_2.setFont(font)
        self.img_2.setStyleSheet("brackground-image: url(:/img_3/images/simpson_13/3.png)")
        self.img_2.setText("")
        self.img_2.setPixmap(QtGui.QPixmap(":/img_3/images/simpson_13/3.png"))
        self.img_2.setScaledContents(True)
        self.img_2.setObjectName("img_2")
        self.gridLayout.addWidget(self.img_2, 6, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.lbl_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_5.setFont(font)
        self.lbl_5.setObjectName("lbl_5")
        self.gridLayout.addWidget(self.lbl_5, 10, 0, 1, 1)
        self.img_1 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.img_1.setFont(font)
        self.img_1.setStyleSheet("brackground-image: url(:/img_2/images/simpson_13/2.png)")
        self.img_1.setText("")
        self.img_1.setPixmap(QtGui.QPixmap(":/img_2/images/simpson_13/2.png"))
        self.img_1.setScaledContents(True)
        self.img_1.setObjectName("img_1")
        self.gridLayout.addWidget(self.img_1, 4, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.lbl_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_4.setFont(font)
        self.lbl_4.setObjectName("lbl_4")
        self.gridLayout.addWidget(self.lbl_4, 8, 0, 1, 1)
        self.lbl_7 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_7.setFont(font)
        self.lbl_7.setObjectName("lbl_7")
        self.gridLayout.addWidget(self.lbl_7, 14, 0, 1, 1)
        self.lbl_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_2.setFont(font)
        self.lbl_2.setObjectName("lbl_2")
        self.gridLayout.addWidget(self.lbl_2, 5, 0, 1, 1)
        self.lbl_1 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_1.setFont(font)
        self.lbl_1.setObjectName("lbl_1")
        self.gridLayout.addWidget(self.lbl_1, 3, 0, 1, 1)
        self.img_0 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.img_0.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.img_0.setFont(font)
        self.img_0.setFocusPolicy(QtCore.Qt.NoFocus)
        self.img_0.setStyleSheet("image: url(:/img_1/images/simpson_13/1.png)")
        self.img_0.setText("")
        self.img_0.setPixmap(QtGui.QPixmap(":/img_1/images/simpson_13/1.png"))
        self.img_0.setScaledContents(True)
        self.img_0.setWordWrap(False)
        self.img_0.setObjectName("img_0")
        self.gridLayout.addWidget(self.img_0, 2, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.lbl_6 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_6.setFont(font)
        self.lbl_6.setObjectName("lbl_6")
        self.gridLayout.addWidget(self.lbl_6, 11, 0, 1, 1)
        self.lbl_8 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_8.setFont(font)
        self.lbl_8.setObjectName("lbl_8")
        self.gridLayout.addWidget(self.lbl_8, 17, 0, 1, 1)
        self.f_input = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.f_input.setFont(font)
        self.f_input.setText("")
        self.f_input.setObjectName("f_input")
        self.gridLayout.addWidget(self.f_input, 9, 0, 1, 1)
        self.a_input = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.a_input.setFont(font)
        self.a_input.setText("")
        self.a_input.setObjectName("a_input")
        self.gridLayout.addWidget(self.a_input, 12, 0, 1, 1)
        self.submit_btn = QtWidgets.QPushButton(self.scrollAreaWidgetContents, clicked = lambda: self.press_it(self.f_input, self.a_input, self.b_input, self.n_input))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.submit_btn.setFont(font)
        self.submit_btn.setObjectName("submit_btn")
        self.gridLayout.addWidget(self.submit_btn, 19, 0, 1, 1)
        self.lbl_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_3.setFont(font)
        self.lbl_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_3.setObjectName("lbl_3")
        self.gridLayout.addWidget(self.lbl_3, 7, 0, 1, 1)
        self.graph_btn = QtWidgets.QPushButton(self.scrollAreaWidgetContents, clicked = lambda: self.graph(self.f_input, self.a_input, self.b_input, self.n_input))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.graph_btn.setFont(font)
        self.graph_btn.setObjectName("graph_btn")
        self.gridLayout.addWidget(self.graph_btn, 20, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        simpson_13.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(simpson_13)
        self.statusbar.setObjectName("statusbar")
        simpson_13.setStatusBar(self.statusbar)

        self.retranslateUi(simpson_13)
        QtCore.QMetaObject.connectSlotsByName(simpson_13)

    def retranslateUi(self, simpson_13):
        _translate = QtCore.QCoreApplication.translate
        simpson_13.setWindowTitle(_translate("simpson_13", "MainWindow"))
        self.lbl_0.setText(_translate("simpson_13", "La regla de Simpson es un método de integración numérica.En otras palabras, es la aproximación \n"
"numérica de integrales definidas.\n"
"La regla de Simpson es la siguiente:\n"
"\n"
"En ella:\n"
"f(x) es llamado el integrand\n"
"a = es el límite inferior de integración\n"
"b = es el límite superior de integración\n"
""))
        self.result_lbl.setText(_translate("simpson_13", "..."))
        self.title_lbl.setText(_translate("simpson_13", "Metodo Simpson 1/3"))
        self.lbl_5.setText(_translate("simpson_13", "Ingresar parametros"))
        self.lbl_4.setText(_translate("simpson_13", "Funcion: ejemplo: x^2 + sin(x)"))
        self.lbl_7.setText(_translate("simpson_13", "b:  ejemplo: 1.4 o 5"))
        self.lbl_2.setText(_translate("simpson_13", "Reemplazando (b-a)/2 como h, obtenemos"))
        self.lbl_1.setText(_translate("simpson_13", "Como se muestra en el diagrama anterior, el integrando f(x) es aproximado por un polinomiode \n"
"segundo orden, el interpolante cuadrático es P(x).\n"
"sigue la aproximación:\n"
""))
        self.lbl_6.setText(_translate("simpson_13", "a: ejemplo: 1.4 o 5"))
        self.lbl_8.setText(_translate("simpson_13", "n:  ejemplo: 1.4 o 5"))
        self.submit_btn.setText(_translate("simpson_13", "Calcular"))
        self.lbl_3.setText(_translate("simpson_13", "Calcular funcion:"))
        self.graph_btn.setText(_translate("simpson_13", "Graficar"))
import simpson_13_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    simpson_13 = QtWidgets.QMainWindow()
    ui = Ui_simpson_13()
    ui.setupUi(simpson_13)
    simpson_13.show()
    sys.exit(app.exec_())