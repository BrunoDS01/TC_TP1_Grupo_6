# PyQt5 modules
from PyQt5 import QtWidgets

# Python modules
import sys

# Main window ui import
from src.MyWindow import MyWindow


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
