# PyQt5 modules
from PyQt5.QtWidgets import QMainWindow, QListWidgetItem, QMessageBox, QInputDialog, QFileDialog
from PyQt5.QtCore import Qt
import os

from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

import numpy as np
import sympy as sp
import scipy.signal as ss

# Project modules
from src.ui.mainwindow import Ui_MainWindow
from src.InputFunction import InputFunction
from src.ImportData import readSpiceBode, readSpiceTime, readCSVBode, readCSVTime


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
        self.addTemporalFunctionButton.clicked.connect(self.addTemporalFunction)
        self.deleteFunctionsButton.clicked.connect(self.deleteFunctions)
        self.eraseBodePlotsButton.clicked.connect(self.eraseBodePlots)
        self.eraseTemporalPlotsButton.clicked.connect(self.eraseTemporalPlots)
        self.erasePolesPlotButton.clicked.connect(self.erasePolesPlot)
        self.deleteAllFunctionsButton.clicked.connect(self.deleteAllFunctions)
        self.changeNameButton.clicked.connect(self.changeFunctionsNames)

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
            self.currentFunction.plotType = 'Frequency'

            functionName, ok = QInputDialog.getText(self, 'Agregar función', 'Nombre de la función:')
            if not ok:
                return

            if len(functionName) < 1:
                functionName = "Función " + str(len(self.functions))

            self.currentFunction.name = functionName

            self.functions.append(self.currentFunction)

            item = QListWidgetItem(functionName)
            item.setCheckState(Qt.Checked)

            self.functionsList.addItem(item)

            for i in range(len(self.functions)):
                if self.functions[i].origin == 'Input':
                    name = functionName + '-' + self.functions[i].name + '-Output'
                    newFunction = InputFunction(origin='Output', name=name)

                    tout, yout = self.currentFunction.calculateOutput(self.functions[i].time, self.functions[i].signal)

                    newFunction.setTemporal(tout, yout)
                    newFunction.plotType = 'Temporal'

                    self.functions.append(newFunction)

                    item = QListWidgetItem(name)
                    item.setCheckState(Qt.Checked)

                    self.functionsList.addItem(item)
            self.currentFunction = InputFunction()
            self.numLabel.setText('1')
            self.denLabel.setText('1')

    def importSpice(self):
        filepath = QFileDialog.getOpenFileName(self, 'Open file', 'c:\\', "Text files (*.txt)")[0]
        if os.path.exists(filepath):
            try:
                if self.frequencyButton.isChecked():

                    freq, mag, phase = readSpiceBode(filepath)
                    functionName, ok = QInputDialog.getText(self, 'LTSpice', 'Nombre de la función:')

                    if not ok:
                        return

                    if len(functionName) < 1:
                        functionName = "Función " + str(len(self.functions))

                    newFunction = InputFunction(origin='Spice', name = functionName)
                    newFunction.setBode(freq, mag, phase)
                    newFunction.plotType = 'Frequency'
                    newFunction.magType = 'dB'

                    self.functions.append(newFunction)

                    item = QListWidgetItem(functionName)
                    item.setCheckState(Qt.Checked)

                    self.functionsList.addItem(item)

                elif self.temporalButton.isChecked():
                    data = readSpiceTime(filepath)

                    for i in range(1, len(data)):
                        functionName,ok = QInputDialog.getText(self, 'LTSpice', 'Nombre la función: ' + str(i))
                        if not ok:
                            return
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
                msgBox.setText("Error al importar datos Spice.\n Asegúrese de haber seleccionado"
                               "correctamente si es una respuesta en frecuencia o temporal")
                msgBox.setWindowTitle("Advertencia")
                msgBox.exec()

    def importCSV(self):
        filepath = QFileDialog.getOpenFileName(self, 'Abrir archivo', 'c:\\', "CSV files (*.csv)")[0]
        if os.path.exists(filepath):
            try:
                if self.frequencyButton.isChecked():

                    freq, mag, phase = readCSVBode(filepath)
                    functionName, ok = QInputDialog.getText(self, 'CSV', 'Nombre de la función:')
                    if not ok:
                        return
                    if len(functionName) < 1:
                        functionName = "Función " + str(len(self.functions))

                    newFunction = InputFunction(origin='CSV', name=functionName)
                    newFunction.setBode(freq, mag, phase)
                    newFunction.plotType = 'Frequency'
                    if self.csvFreqModeComboBox.currentText() == "dB":
                        newFunction.magType = 'dB'
                    else:
                        newFunction.magType = 'Lineal'

                    self.functions.append(newFunction)

                    item = QListWidgetItem(functionName)
                    item.setCheckState(Qt.Checked)

                    self.functionsList.addItem(item)

                elif self.temporalButton.isChecked():
                    data = readCSVTime(filepath)

                    for i in range(1, len(data)):
                        functionName, ok = QInputDialog.getText(self, 'CSV', 'Nombre de la función:' + str(i))
                        if not ok:
                            return
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
                msgBox.setText("Error al importar datos CSV. "
                               "Asegúrese de no ingresar números al comienzo de cada línea antes de los datos"
                               "y de haber seleccionado correctamente respuesta en frecuencia o temporal")
                msgBox.setWindowTitle("Advertencia")
                msgBox.exec()

    # Agrega una función periódica ingresada por el usuario y crea las salidas correspondientes
    # para las funciones ingresadas por función transferencia
    def addTemporalFunction(self):
        freq = self.freqDoubleBox.value() * (10 ** self.freqMultiplicador.value())
        amp = self.amplitudeDoubleBox.value() * (10 ** self.amplitudeMultiplicador.value())
        offset = self.offsetDoubleBox.value() * (10 ** self.offsetMultiplier.value())
        phase = self.phaseSpinBox.value()
        dutycycle = self.dutyCycleDoubleBox.value()
        simetry = self.simetryDoubleBox.value()

        mintime = self.minTimeValue.value() * (10 ** self.minTimeMultiplier.value())
        maxtime = self.maxTimeValue.value() * (10 ** self.maxTimeMultiplier.value())

        if mintime >= maxtime:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setText("El tiempo mínimo es mayor o igual al tiempo máximo!")
            msgBox.setWindowTitle("Advertencia")
            msgBox.exec()
            return

        points = np.linspace(mintime, maxtime, 5000, endpoint=True)
        inputPoints = None

        if self.entradaComboBox.currentText() == 'Senoide':
            inputPoints = amp * np.sin(2 * np.pi * freq * points + phase*np.pi/180) + offset

        elif self.entradaComboBox.currentText() == 'Cuadrada':
            inputPoints = amp * ss.square(2 * np.pi * freq * points + phase*np.pi/180, dutycycle/100) + offset

        elif self.entradaComboBox.currentText() == 'Rampa':
            inputPoints = amp * ss.sawtooth(2 * np.pi * freq * points + phase*np.pi/180, simetry/100) + offset

        # Agregamos la función
        functionName, ok = QInputDialog.getText(self, 'Señal de entrada', 'Nombre la función: ')
        if not ok:
            return
        if len(functionName) < 1:
            functionName = "Función " + str(len(self.functions))

        newFunction = InputFunction(origin='Input', name=functionName)
        newFunction.setTemporal(points, inputPoints)
        newFunction.plotType = 'Temporal'

        self.functions.append(newFunction)

        item = QListWidgetItem(functionName)
        item.setCheckState(Qt.Checked)

        self.functionsList.addItem(item)

        for i in range(len(self.functions)):
                if self.functions[i].origin == 'Transfer':
                    name = self.functions[i].name + '-' + functionName + '-Output'
                    newFunction = InputFunction(origin='Output', name=name)

                    tout, yout = self.functions[i].calculateOutput(points, inputPoints)

                    newFunction.setTemporal(tout, yout)
                    newFunction.plotType = 'Temporal'

                    self.functions.append(newFunction)

                    item = QListWidgetItem(name)
                    item.setCheckState(Qt.Checked)

                    self.functionsList.addItem(item)


    # Grafica Bode en función de las funciones seleccionadas y su origen
    def updateBodePlot(self):
        self.axesAmplitude.clear()
        self.axesPhase.clear()

        minFrequency = self.minFreqValue.value() * (10 ** self.minFreqMultiplier.value())
        maxFrequency = self.maxFreqValue.value() * (10 ** self.maxFreqMultiplier.value())

        if minFrequency >= maxFrequency:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setText("La frecuencia mínima es mayor o igual a la frecuencia máxima!")
            msgBox.setWindowTitle("Advertencia")
            msgBox.exec()
            return

        for i in range(len(self.functions)):
            if self.functionsList.item(i).checkState() == 2:

                # Caso de ingresar función transferencia
                if self.functions[i].origin == 'Transfer':
                    minFreq = minFrequency  # varibales auxiliares
                    maxFreq = maxFrequency  # variables auxiliares
                    if self.freqMode.currentText() == 'Hz':
                        minFreq = minFrequency * 2 * np.pi
                        maxFreq = maxFrequency * 2 * np.pi

                    if self.freqAxisLinealButton.isChecked():
                        w = np.linspace(minFreq, maxFreq, num = 5000)
                    else:
                        w = np.logspace((np.log10(minFreq)), (np.log10(maxFreq)), num=5000)

                    if self.yAxisDBButton.isChecked():
                        freq, mag, phase = self.functions[i].calculateBode(w=w, n=5000)
                    else:
                        freq, mag, phase = self.functions[i].calculateFrequencyResponse(w=w, n = 5000)

                    if self.freqMode.currentText() == 'Hz':
                        freq = freq / (2 * np.pi)

                    if self.freqAxisLinealButton.isChecked():
                        self.axesAmplitude.plot(freq, mag, label=self.functions[i].name)
                        self.axesPhase.plot(freq, phase, label=self.functions[i].name)
                    else:
                        self.axesAmplitude.semilogx(freq, mag, label=self.functions[i].name)
                        self.axesPhase.semilogx(freq, phase, label=self.functions[i].name)

                # Caso LTSpice o CSV
                elif (self.functions[i].origin == 'Spice' or self.functions[i].origin == 'CSV') \
                        and self.functions[i].plotType == 'Frequency':
                    freq, mag, phase = self.functions[i].freq, self.functions[i].mag, self.functions[i].phase

                    if self.freqMode.currentText() == 'Rad/s':
                        freq = [fr * 2 * np.pi for fr in freq]

                    if self.yAxisLinealButton.isChecked() and self.functions[i].magType == 'dB':
                        mag = [np.exp(m/20) for m in mag]

                    elif self.yAxisDBButton.isChecked() and self.functions[i].magType == 'Lineal':
                        mag = [20 * np.log10(m) for m in mag]

                    if self.freqAxisLinealButton.isChecked():
                        if self.functions[i].origin == 'CSV':
                            self.axesAmplitude.scatter(freq, mag, label=self.functions[i].name, marker = '.')
                            self.axesPhase.scatter(freq, phase, label=self.functions[i].name, marker = '.')
                        else:
                            self.axesAmplitude.plot(freq, mag, label=self.functions[i].name)
                            self.axesPhase.plot(freq, phase, label=self.functions[i].name)
                    else:
                        if self.functions[i].origin == 'CSV':
                            self.axesAmplitude.set_xscale('log')
                            self.axesPhase.set_xscale('log')
                            self.axesAmplitude.scatter(freq, mag, label=self.functions[i].name, marker = '.')
                            self.axesPhase.scatter(freq, phase, label=self.functions[i].name, marker = '.')
                        else:
                            self.axesAmplitude.semilogx(freq, mag, label=self.functions[i].name)
                            self.axesPhase.semilogx(freq, phase, label = self.functions[i].name)

        self.axesAmplitude.set_xlim(minFrequency, maxFrequency)
        self.axesPhase.set_xlim(minFrequency, maxFrequency)

        self.axesAmplitude.grid(False, which='both')
        self.axesPhase.grid(False, which='both')

        if self.gridSimpleButton.isChecked():
            self.axesAmplitude.grid(True, which='major')
            self.axesPhase.grid(True, which='major')
        if self.gridCompleteButton.isChecked():
            self.axesAmplitude.grid(True, which='both')
            self.axesPhase.grid(True, which='both')

        self.axesAmplitude.axhline(0, color='black', linewidth=1)
        self.axesPhase.axhline(0, color='black', linewidth=1)

        self.axesAmplitude.legend(loc=0)
        self.axesPhase.legend(loc=0)

        self.axesAmplitude.set_xlabel(self.ampXLabel.text())
        self.axesAmplitude.set_ylabel(self.ampYLabel.text())
        self.axesPhase.set_xlabel(self.phaseXLabel.text())
        self.axesPhase.set_ylabel(self.phaseYLabel.text())

        self.axesAmplitude.set_title(self.ampTitle.text())
        self.axesPhase.set_title(self.phaseTitle.text())

        self.canvasAmplitude.draw()
        self.canvasPhase.draw()

    # Grafica las respuestas temporales en función de las funciones seleccionadas y su origen
    def plotTemporalSignals(self):
        self.axesTemporal.clear()

        for i in range(len(self.functions)):
            if self.functionsList.item(i).checkState() == 2:
                if self.functions[i].plotType == 'Temporal':
                    time, signal = self.functions[i].time, self.functions[i].signal

                    if self.functions[i].origin == 'CSV':
                        self.axesTemporal.scatter(time, signal, label=self.functions[i].name, marker = '.')
                    else:
                        self.axesTemporal.plot(time, signal, label=self.functions[i].name)


        self.axesTemporal.grid(visible=True)
        self.axesTemporal.axhline(0, color='black', linewidth=1)
        self.axesTemporal.axvline(0, color='black', linewidth=1)

        self.axesTemporal.ticklabel_format(axis='both', style='sci')

        self.axesTemporal.set_xlabel(self.temporalXLabel.text())
        self.axesTemporal.set_ylabel(self.temporalYLabel.text())

        self.axesTemporal.set_title(self.temporalTitle.text())

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
                                                            marker='x', label='Polos ' + self.functions[i].name)

                if len(zeros) != 0:
                    self.zerosLine = self.axesPolesZeros.scatter(np.real(zeros), np.imag(zeros),
                                                                 marker='o', label='Ceros ' + self.functions[i].name)

        self.axesPolesZeros.ticklabel_format(axis='both', style='sci')
        self.axesPolesZeros.grid(visible=True)
        self.axesPolesZeros.axhline(0, color='black', linewidth=1)
        self.axesPolesZeros.axvline(0, color='black', linewidth=1)  # marcamos los ejes

        self.axesPolesZeros.set_ylabel(self.polesXLabel.text())
        self.axesPolesZeros.set_xlabel(self.polesYLabel.text())
        self.axesPolesZeros.set_title(self.polesTitle.text())
        self.axesPolesZeros.legend(loc=0)

        self.figurePolesZeros.canvas.draw()

    def deleteFunctions(self):
        numberOfFunctions = len(self.functions)
        for i in range(numberOfFunctions):
            if self.functionsList.item(numberOfFunctions-1-i).checkState() == 2:
                self.functionsList.takeItem(numberOfFunctions-1-i)
                self.functions.pop(numberOfFunctions-1-i)

    def deleteAllFunctions(self):
        numberOfFunctions = len(self.functions)
        for i in range(numberOfFunctions):
            self.functionsList.takeItem(numberOfFunctions - 1 - i)
            self.functions.pop(numberOfFunctions - 1 - i)

    def eraseBodePlots(self):
        self.axesAmplitude.clear()
        self.axesPhase.clear()

        self.canvasAmplitude.draw()
        self.canvasPhase.draw()

    def eraseTemporalPlots(self):
        self.axesTemporal.clear()
        self.canvasTemporal.draw()

    def erasePolesPlot(self):
        self.axesPolesZeros.clear()
        self.canvasPolesZeros.draw()

    def changeFunctionsNames(self):
        for i in range(len(self.functions)):
            if self.functionsList.item(i).checkState() == 2:
                functionName, ok = QInputDialog.getText(self, self.functions[i].name, 'Cambiar nombre: ')
                if not ok:
                    return
                self.functionsList.item(i).setText(functionName)
                self.functions[i].name = functionName
