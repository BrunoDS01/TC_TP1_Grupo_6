# PyQt5 modules
from PyQt5.QtWidgets import QMainWindow, QListWidgetItem, QMessageBox, QInputDialog, QFileDialog
from PyQt5.QtCore import Qt

from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

import numpy as np
import sympy as sp

# Project modules
from src.ui.mainwindow import Ui_MainWindow
from InputFunction import InputFunction
from ImportData import readSpiceBode, readSpiceTime, readCSVBode, readCSVTime


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
        self.figureAmplitude.set_tight_layout(True)
        self.canvasAmplitude = FigureCanvas(self.figureAmplitude)
        self.axesAmplitude = self.figureAmplitude.subplots()
        self.amplitudeBodePlot.addWidget(NavigationToolbar(self.canvasAmplitude, self))
        self.amplitudeBodePlot.addWidget(self.canvasAmplitude)

        # Gráfico de fase
        self.figurePhase = Figure()
        self.figurePhase.set_tight_layout(True)
        self.canvasPhase = FigureCanvas(self.figurePhase)
        self.axesPhase = self.figurePhase.subplots()
        self.phaseBodePlot.addWidget(NavigationToolbar(self.canvasPhase, self))
        self.phaseBodePlot.addWidget(self.canvasPhase)

        # Gráfico de polos y ceros
        self.figurePolesZeros = Figure()
        self.figurePolesZeros.set_tight_layout(True)
        self.canvasPolesZeros = FigureCanvas(self.figurePolesZeros)
        self.axesPolesZeros = self.figurePolesZeros.subplots()
        self.polesZerosPlot.addWidget(NavigationToolbar(self.canvasPolesZeros, self))
        self.polesZerosPlot.addWidget(self.canvasPolesZeros)

        # Gráfico de respuesta temporal
        self.figureTemporal = Figure()
        self.figureTemporal.set_tight_layout(True)
        self.canvasTemporal = FigureCanvas(self.figureTemporal)
        self.axesTemporal = self.figureTemporal.subplots()
        self.temporalResponsePlot.addWidget(NavigationToolbar(self.canvasTemporal, self))
        self.temporalResponsePlot.addWidget(self.canvasTemporal)

        # Configuración de las pestañas y clicks
        self.addTermButton.clicked.connect(self.addTermToPolinomial)
        self.addPolinomialButton.clicked.connect(self.addPolinomialToFunction)
        self.erasePolinomialButton.clicked.connect(self.erasePolinomial)
        self.eraseEquationButton.clicked.connect(self.eraseEquation)
        self.addFunctionButton.clicked.connect(self.addFunction)
        self.plotBodeButton.clicked.connect(self.updateBodePlot)
        self.spiceButton.clicked.connect(self.importSpice)
        self.csvButton.clicked.connect(self.importCSV)
        self.plotTemporalButton.clicked.connect(self.plotTemporalSignals)
        self.addPolesZeros.clicked.connect(self.plotPolesZeros)

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
            self.currentFunction.origin = 'Transfer'

            functionName = QInputDialog.getText(self, 'Agregar función', 'Nombre de la función:')[0]
            if len(functionName) < 1:
                functionName = "Función " + str(len(self.functions))

            self.currentFunction.name = functionName

            self.functions.append(self.currentFunction)
            self.currentFunction = InputFunction()
            self.numLabel.setText('1')
            self.denLabel.setText('1')

            item = QListWidgetItem(functionName)
            item.setCheckState(Qt.Checked)

            self.functionsList.addItem(item)

    def importSpice(self):
        filepath = QFileDialog.getOpenFileName(self, 'Open file', 'c:\\', "Text files (*.txt)")[0]

        try:
            if self.frequencyButton.isChecked():

                freq, mag, phase = readSpiceBode(filepath)
                functionName = QInputDialog.getText(self, 'LTSpice', 'Nombre de la función:')[0]
                if len(functionName) < 1:
                    functionName = "Función " + str(len(self.functions))

                newFunction = InputFunction(origin='Spice', name = functionName)
                newFunction.setBode(freq, mag, phase)
                newFunction.plotType = 'Frequency'

                self.functions.append(newFunction)

                item = QListWidgetItem(functionName)
                item.setCheckState(Qt.Checked)

                self.functionsList.addItem(item)

            elif self.temporalButton.isChecked():
                data = readSpiceTime(filepath)

                for i in range(1, len(data)):
                    functionName = QInputDialog.getText(self, 'LTSpice', 'Nombre la función: ' + str(i))[0]
                    if len(functionName) < 1:
                        functionName = "Función " + str(len(self.functions))

                    newFunction = InputFunction(origin='Spice', name=functionName)
                    newFunction.setTemporal(data[0], data[i])
                    newFunction.plotType = 'Temporal'

                    self.functions.append(newFunction)

                    item = QListWidgetItem(functionName)
                    item.setCheckState(Qt.Checked)

                    self.functionsList.addItem(item)

        except:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setText("Error al importar datos")
            msgBox.setWindowTitle("Advertencia")
            msgBox.exec()

    def importCSV(self):
        filepath = QFileDialog.getOpenFileName(self, 'Abrir archivo', 'c:\\', "CSV files (*.csv)")[0]

        try:
            if self.frequencyButton.isChecked():

                freq, mag, phase = readCSVBode(filepath)
                functionName = QInputDialog.getText(self, 'CSV', 'Nombre de la función:')[0]
                if len(functionName) < 1:
                    functionName = "Función " + str(len(self.functions))

                newFunction = InputFunction(origin='CSV', name=functionName)
                newFunction.setBode(freq, mag, phase)
                newFunction.plotType = 'Frequency'

                self.functions.append(newFunction)

                item = QListWidgetItem(functionName)
                item.setCheckState(Qt.Checked)

                self.functionsList.addItem(item)

            elif self.temporalButton.isChecked():
                data = readCSVTime(filepath)

                for i in range(1, len(data)):
                    functionName = QInputDialog.getText(self, 'CSV', 'Nombre de la función:' + str(i))[0]
                    if len(functionName) < 1:
                        functionName = "Función " + str(len(self.functions))

                    newFunction = InputFunction(origin='CSV', name=functionName)
                    newFunction.setTemporal(data[0], data[i])
                    newFunction.plotType = 'Temporal'

                    self.functions.append(newFunction)

                    item = QListWidgetItem(functionName)
                    item.setCheckState(Qt.Checked)

                    self.functionsList.addItem(item)

        except:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setText("Error al importar datos")
            msgBox.setWindowTitle("Advertencia")
            msgBox.exec()


    # Grafica Bode en función de las funciones seleccionadas y su origen
    def updateBodePlot(self):
        self.axesAmplitude.clear()
        self.axesPhase.clear()

        minFrequency = self.minFreqValue.value() * (10 ** self.minFreqMultiplier.value())
        maxFrequency = self.maxFreqValue.value() * (10 ** self.maxFreqMultiplier.value())

        for i in range(len(self.functions)):
            if self.functionsList.item(i).checkState() == 2:

                # Caso de ingresar función transferencia
                if self.functions[i].origin == 'Transfer':
                    if self.freqMode.currentText() == 'Hz':
                        minFreq = minFrequency * 2 * np.pi
                        maxFreq = maxFrequency * 2 * np.pi

                    w = np.logspace((np.log10(minFreq)), (np.log10(maxFreq)), num=5000)

                    freq, mag, phase = self.functions[i].calculateBode(w = w)

                    if self.freqMode.currentText() == 'Hz':
                        freq = freq / (2 * np.pi)

                    self.axesAmplitude.semilogx(freq, mag, label=self.functions[i].name)
                    self.axesPhase.semilogx(freq, phase, label=self.functions[i].name)

                # Caso LTSpice o CSV
                elif self.functions[i].origin == 'Spice' or self.functions[i].origin == 'CSV' \
                        and self.functions[i].plotType == 'Frequency':
                    freq, mag, phase = self.functions[i].freq, self.functions[i].mag, self.functions[i].phase

                    if self.freqMode.currentText() == 'Rad/s':
                        freq = [fr * 2 * np.pi for fr in freq]

                    self.axesAmplitude.semilogx(freq, mag, label=self.functions[i].name)
                    self.axesPhase.semilogx(freq, phase, label = self.functions[i].name)

        self.axesAmplitude.set_xlim(minFrequency, maxFrequency)
        self.axesPhase.set_xlim(minFrequency, maxFrequency)

        self.axesAmplitude.grid(True, which='both')
        self.axesPhase.grid(True, which='both')

        self.axesAmplitude.legend(loc=0)
        self.axesPhase.legend(loc=0)

        self.canvasAmplitude.draw()
        self.canvasPhase.draw()

    # Grafica las respuestas temporales en función de las funciones seleccionadas y su origen
    def plotTemporalSignals(self):
        self.axesTemporal.clear()

        for i in range(len(self.functions)):
            if self.functionsList.item(i).checkState() == 2:

                # Caso de ingresar función transferencia
                '''if self.functions[i].origin == 'Transfer':
                    if self.freqMode.currentText() == 'Hz':
                        minFreq = minFrequency * 2 * np.pi
                        maxFreq = maxFrequency * 2 * np.pi

                    w = np.logspace((np.log10(minFreq)), (np.log10(maxFreq)), num=5000)

                    freq, mag, phase = self.functions[i].calculateBode(w=w)

                    if self.freqMode.currentText() == 'Hz':
                        freq = freq / (2 * np.pi)

                    self.axesAmplitude.semilogx(freq, mag, label=self.functions[i].name)
                    self.axesPhase.semilogx(freq, phase, label=self.functions[i].name)'''

                # Caso LTSpice o CSV
                if (self.functions[i].origin == 'Spice' or self.functions[i].origin == 'CSV') \
                        and self.functions[i].plotType == 'Temporal':
                    time, signal = self.functions[i].time, self.functions[i].signal

                    self.axesTemporal.plot(time, signal, label=self.functions[i].name)

        self.axesTemporal.grid(visible=True)
        self.axesTemporal.axhline(0, color='black', linewidth=1)
        self.axesTemporal.axvline(0, color='black', linewidth=1)

        self.axesTemporal.legend(loc=0)

        self.figureTemporal.canvas.draw()


    # Grafica polos y ceros de aquellas funciones ingresadas por función transferencia

    def plotPolesZeros(self):
        self.axesPolesZeros.clear()

        for i in range(len(self.functions)):
            if self.functionsList.item(i).checkState() == 2 and self.functions[i].origin == 'Transfer':
                poles, zeros = self.functions[i].calculatePolesZeros()

                if len(poles) != 0:
                    polesLine = self.axesPolesZeros.scatter(np.real(poles), np.imag(poles),
                                                            marker='x', label='Polos' + self.functions[i].name)

                if len(zeros) != 0:
                    self.zerosLine = self.axesPolesZeros.scatter(np.real(zeros), np.imag(zeros),
                                                                 marker='o', label='Ceros' + self.functions[i].name)

        self.axesPolesZeros.grid(visible=True)
        self.axesPolesZeros.axhline(0, color='black', linewidth=1)
        self.axesPolesZeros.axvline(0, color='black', linewidth=1)  # marcamos los ejes

        self.axesPolesZeros.set_ylabel('jω')
        self.axesPolesZeros.set_xlabel('σ')
        self.axesPolesZeros.legend(loc=0)

        self.figurePolesZeros.canvas.draw()