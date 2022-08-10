# PyQt5 modules
from PyQt5.QtWidgets import QMainWindow, QListWidgetItem, QMessageBox
from PyQt5.QtCore import Qt

import sympy as sp

# Project modules
from src.ui.mainwindow import Ui_MainWindow
from InputFunction import InputFunction


class MyWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)

        # Configuración de las pestañas y clicks
        self.addTermButton.clicked.connect(self.addTermToPolinomial)
        self.addPolinomialButton.clicked.connect(self.addPolinomialToFunction)
        self.erasePolinomialButton.clicked.connect(self.erasePolinomial)
        self.eraseEquationButton.clicked.connect(self.eraseEquation)
        self.addFunctionButton.clicked.connect(self.addFunction)

        # Lista de la funciones agregadas
        self.functions = []
        self.currentFunction = InputFunction()
        self.currentPolinomial = sp.sympify('0')


    # Funciones de las pestañas y clicks


    # Agrega término a la ecuación de transferencia de la función actual
    def addTermToPolinomial(self):
        s = sp.symbols('s')
        coef = self.coefDoubleBox.value() * (10 ** self.coefMultiplier.value())
        order = self.ordenSpinbox.value()

        polinomio = coef * s**order

        self.currentPolinomial += polinomio

        self.currentPolLabel.setText(str(self.currentPolinomial))

    def addPolinomialToFunction(self):
        if self.numButton.isChecked() and self.currentPolinomial:
            self.currentFunction.num *= self.currentPolinomial
            self.currentPolinomial = sp.sympify('0')
            self.numLabel.setText(str(self.currentFunction.num))
            self.currentPolLabel.setText('0')

        elif self.denButton.isChecked() and self.currentPolinomial != sp.sympify('0'):
            self.currentFunction.den *= self.currentPolinomial
            self.currentPolinomial = sp.sympify('0')
            self.denLabel.setText(str(self.currentFunction.den))
            self.currentPolLabel.setText('0')

    def erasePolinomial(self):
        self.currentPolinomial = sp.sympify('0')
        self.currentPolLabel.setText('0')

    def eraseEquation(self):
        self.currentFunction.num = sp.sympify('1')
        self.currentFunction.den = sp.sympify('1')
        self.numLabel.setText('1')
        self.denLabel.setText('1')

    # Agrega la función introducida como función transferencia
    def addFunction(self):
        if self.currentFunction.den == sp.sympify('0'):
            print('den = 0')
        else:
            self.currentFunction.setTransferFunction()
            self.currentFunction.origin = 'T'

            self.functions.append(self.currentFunction)
            self.currentFunction = InputFunction()
            self.numLabel.setText('1')
            self.denLabel.setText('1')

            item = QListWidgetItem('Función')
            item.setCheckState(Qt.Unchecked)

            self.functionsList.addItem(item)






