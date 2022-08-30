import numpy as np
import scipy.signal as ss
import sympy as sp

class InputFunction:
    def __init__(self, origin = 'Transfer', name = 'Función'):
        self.origin = origin
        self.name = name

        self.plotType = None
        self.magType = None
        self.plotMarker = None

        self.transferFunction = None

        self.s = sp.symbols('s')
        self.num = sp.sympify('1')
        self.den = sp.sympify('1')

        self.freq = []
        self.mag = []
        self.phase = []

        self.time = []
        self.signal = []


    def setTransferFunction(self):
        self.num = sp.Poly(self.num, self.s)
        self.den = sp.poly(self.den, self.s)

        num = np.array(self.num.all_coeffs()).astype(float)
        den = np.array(self.den.all_coeffs()).astype(float)

        self.transferFunction = ss.TransferFunction(num, den)

    def calculateBode(self, w=None, n = 1000):
        self.freq, self.mag, self.phase = ss.bode(self.transferFunction, w, n=n)
        return self.freq, self.mag, self.phase

    def calculateFrequencyResponse(self, w=None, n = 1000):
        w, y = ss.freqresp(self.transferFunction, w=w, n=n)
        self.freq = w
        self.mag = abs(y)
        self.phase = np.unwrap(np.arctan2(y.imag, y.real)) * 180.0 / np.pi

        return self.freq, self.mag, self.phase

    def calculatePolesZeros(self):
        return self.transferFunction.poles, self.transferFunction.zeros

    def calculateOutput(self, tiempo = None, entrada = None):
        t, y, x = ss.lsim(self.transferFunction, U = entrada, T = tiempo)

        return t, y

    def setBode(self, f, m, p):
        self.freq = f
        self.mag = m
        self.phase = p

    def setTemporal(self, t, s):
        self.time = t
        self.signal = s