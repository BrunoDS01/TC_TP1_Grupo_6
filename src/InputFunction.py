import numpy as np
import scipy.signal as ss
import sympy as sp

class InputFunction:
    def __init__(self, origin = 'T', name = 'Función'):
        self.origin = origin
        self.name = name

        self.transferFunction = None

        self.s = sp.symbols('s')
        self.num = sp.sympify('1')
        self.den = sp.sympify('1')

        self.freq = []
        self.mag = []
        self.phase = []

        self.time = []
        self.input = []
        self.output = []


    def setTransferFunction(self):
        self.num = sp.Poly(self.num, self.s)
        self.den = sp.poly(self.den, self.s)

        num = np.array(self.num.all_coeffs()).astype(float)
        den = np.array(self.den.all_coeffs()).astype(float)

        self.transferFunction = ss.TransferFunction(num, den)

    def calculateBode(self, w=None):
        return ss.bode(self.transferFunction, w, n=10000)

    def calculatePolesZeros(self):
        return self.transferFunction.poles, self.transferFunction.zeros

    def setBode(self, f, m, p):
        self.freq = f
        self.mag = m
        self.phase = p