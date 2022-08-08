import numpy as np
import scipy.signal as ss

class InputFunction:
    def __init__(self):
        self.numPolinomial = True
        self.denPolinomial = True
        self.num = []
        self.den = []

        self.abs = []
        self.phase = []
        self.freq = []

        self.transferFunction = None

