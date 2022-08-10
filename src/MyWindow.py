# PyQt5 modules
from PyQt5.QtWidgets import QMainWindow, QListWidgetItem, QMessageBox, QInputDialog
from PyQt5.QtCore import Qt

from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

import sympy as sp

# Project modules
from src.ui.mainwindow import Ui_MainWindow
from InputFunction import InputFunction


class MyWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)

        # Lista de la funciones agregadas
        self.functions = []
        self.currentFunction = InputFunction()
        self.currentPolinomial = sp.sympify('0')

        # Configuración gráfica
        # Gráfico de amplitud
        self.figureAmplitude = Figure()
        self.canvasAmplitude = FigureCanvas(self.figureAmplitude)
        self.axesAmplitude = self.figureAmplitude.subplots()
        self.amplitudeBodeBox.layout().addWidget(NavigationToolbar(self.canvasAmplitude, self))
        self.amplitudeBodeBox.layout().addWidget(self.canvasAmplitude)

        # Gráfico de fase
        self.figurePhase = Figure()
        self.canvasPhase = FigureCanvas(self.figurePhase)
        self.axesPhase = self.figurePhase.subplots()
        self.phasePlotBox.addWidget(NavigationToolbar(self.canvasPhase, self))
        self.phasePlotBox.addWidget(self.canvasPhase)

        # Configuración de las pestañas y clicks
        self.addTermButton.clicked.connect(self.addTermToPolinomial)
        self.addPolinomialButton.clicked.connect(self.addPolinomialToFunction)
        self.erasePolinomialButton.clicked.connect(self.erasePolinomial)
        self.eraseEquationButton.clicked.connect(self.eraseEquation)
        self.addFunctionButton.clicked.connect(self.addFunction)
        self.plotBodeButton.clicked.connect(self.updateBodePlot)

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
        if self.numButton.isChecked():
            self.currentFunction.num *= self.currentPolinomial
            self.currentPolinomial = sp.sympify('0')
            self.numLabel.setText(str(self.currentFunction.num))
            self.currentPolLabel.setText('0')

        elif self.denButton.isChecked():
            if self.currentPolinomial == sp.sympify('0'):
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Warning)
                msgBox.setText("El denominador debe ser distinto de cero")
                msgBox.setWindowTitle("Advertencia")
                msgBox.exec()

            else:
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
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setText("El denominador debe ser distinto de cero")
            msgBox.setWindowTitle("Advertencia")
            msgBox.exec()

        else:
            self.currentFunction.setTransferFunction()
            self.currentFunction.origin = 'T'

            self.functions.append(self.currentFunction)
            self.currentFunction = InputFunction()
            self.numLabel.setText('1')
            self.denLabel.setText('1')

            functionName = QInputDialog.getText(self, 'Agregar función', 'Nombre de la función:')[0]
            if len(functionName) < 1:
                functionName = "Función " + str(len(self.functions))

            item = QListWidgetItem(functionName)
            item.setCheckState(Qt.Checked)

            self.functionsList.addItem(item)

    def updateBodePlot(self):
        for i in range(len(self.functions)):
            if self.functionsList.item(i).checkState() == 2:
                if self.functions[i].origin == 'T':
                    w, mag, phase = self.functions[i].calculateBode()

                    self.axesAmplitude.semilogx(w, mag, label='T', marker= 'D')
                    self.figureAmplitude.tight_layout()
                    self.canvasAmplitude.draw()



