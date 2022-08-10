import numpy as np
import scipy.signal as ss
import sympy as sp

class InputFunction:
    def __init__(self):
        self.s = sp.symbols('s')
        self.num = sp.sympify('1')
        self.den = sp.sympify('1')

        self.origin = 'T'

        self.abs = []
        self.phase = []
        self.freq = []

        self.transferFunction = None


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