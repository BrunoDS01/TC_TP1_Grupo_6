# PyQt5 modules
from PyQt5.QtWidgets import QMainWindow

# Project modules
from src.ui.mainwindow import Ui_MainWindow
from InputFunction import InputFunction


class MyWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)

        # Configuración de las pestañas y clicks
        self.polinomialButton.clicked.connect(self.changeTranferStackedToPolinomial)
        self.polesButton.clicked.connect(self.changeTranferStackedToPoles)
        self.firstOrderButton.clicked.connect(self.changePolesOrderStackedToFirst)
        self.secondOrderButton.clicked.connect(self.changePolesOrderStackedToSecond)

        self.addTermButton.clicked.connect(self.addTermToTranferFunction)

        # Lista de la funciones agregadas
        self.functions = []
        self.currentFunction = InputFunction()


    # Funciones de las pestañas y clicks
    def changeTranferStackedToPoles(self):
        self.transferStacked.setCurrentIndex(1)

    def changeTranferStackedToPolinomial(self):
        self.transferStacked.setCurrentIndex(0)

    def changePolesOrderStackedToFirst(self):
        self.polesStacked.setCurrentIndex(0)

    def changePolesOrderStackedToSecond(self):
        self.polesStacked.setCurrentIndex(1)


    # Agrega término a la ecuación de transferencia de la función actual
    def addTermToTranferFunction(self):
        if self.polinomialButton.isChecked():
            coef = self.coefDoubleBox.value() * (10 ** self.coefMultiplier.value())
            order = self.ordenSpinbox.value()

            if self.numButton.isChecked():
                if self.currentFunction.numPolinomial is False:
                    self.currentFunction.num = []

                self.currentFunction.num[order] = coef
            else:
                if self.currentFunction.denPolinomial is False:
                    self.currentFunction.den = []

                self.currentFunction.den[order] = coef

        elif self.polesButton.isChecked():
            if self.firstOrderButton.isChecked():
                w0 = self.w0FirstOrderDoubleBox * (10 ** self.w0FirstOrderMultiplier)
                multplier = self.poleFirstOrderMultiplicidad


