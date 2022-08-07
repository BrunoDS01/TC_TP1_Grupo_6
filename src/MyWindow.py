# PyQt5 modules
from PyQt5.QtWidgets import QMainWindow

# Project modules
from src.ui.mainwindow import Ui_Form


class MyWindow(QMainWindow, Ui_Form):

    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)

    def numeroAlCuadrad0(self, numero):
        num = numero*numero

        self.label.setText(str(num))


