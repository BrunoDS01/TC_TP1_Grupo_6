# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1230, 624)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.deleteFunctionsButton = QtWidgets.QPushButton(self.centralwidget)
        self.deleteFunctionsButton.setObjectName("deleteFunctionsButton")
        self.gridLayout_2.addWidget(self.deleteFunctionsButton, 3, 2, 1, 1)
        self.functionsList = QtWidgets.QListWidget(self.centralwidget)
        self.functionsList.setMinimumSize(QtCore.QSize(150, 0))
        self.functionsList.setMaximumSize(QtCore.QSize(150, 600))
        self.functionsList.setObjectName("functionsList")
        self.gridLayout_2.addWidget(self.functionsList, 2, 2, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_2.setMaximumSize(QtCore.QSize(250, 9999999))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.widget = QtWidgets.QWidget(self.frame_2)
        self.widget.setMaximumSize(QtCore.QSize(16777215, 9999))
        self.widget.setObjectName("widget")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.erasePolinomialButton = QtWidgets.QPushButton(self.widget)
        self.erasePolinomialButton.setObjectName("erasePolinomialButton")
        self.gridLayout_7.addWidget(self.erasePolinomialButton, 11, 0, 1, 3)
        self.currentPolLabel = QtWidgets.QLabel(self.widget)
        self.currentPolLabel.setMinimumSize(QtCore.QSize(0, 25))
        self.currentPolLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.currentPolLabel.setObjectName("currentPolLabel")
        self.gridLayout_7.addWidget(self.currentPolLabel, 6, 0, 1, 3)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.gridLayout_7.addWidget(self.label_4, 3, 0, 1, 1)
        self.addTermButton = QtWidgets.QPushButton(self.widget)
        self.addTermButton.setObjectName("addTermButton")
        self.gridLayout_7.addWidget(self.addTermButton, 5, 0, 1, 3)
        self.addPolinomialButton = QtWidgets.QPushButton(self.widget)
        self.addPolinomialButton.setObjectName("addPolinomialButton")
        self.gridLayout_7.addWidget(self.addPolinomialButton, 10, 0, 1, 3)
        self.ordenSpinbox = QtWidgets.QSpinBox(self.widget)
        self.ordenSpinbox.setMinimumSize(QtCore.QSize(0, 30))
        self.ordenSpinbox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.ordenSpinbox.setMaximum(1000000000)
        self.ordenSpinbox.setObjectName("ordenSpinbox")
        self.gridLayout_7.addWidget(self.ordenSpinbox, 4, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.gridLayout_7.addWidget(self.label_3, 4, 0, 1, 1)
        self.coefMultiplier = QtWidgets.QSpinBox(self.widget)
        self.coefMultiplier.setMinimumSize(QtCore.QSize(0, 30))
        self.coefMultiplier.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.coefMultiplier.setMinimum(-12)
        self.coefMultiplier.setMaximum(12)
        self.coefMultiplier.setSingleStep(3)
        self.coefMultiplier.setObjectName("coefMultiplier")
        self.gridLayout_7.addWidget(self.coefMultiplier, 3, 2, 1, 1)
        self.coefDoubleBox = QtWidgets.QDoubleSpinBox(self.widget)
        self.coefDoubleBox.setMinimumSize(QtCore.QSize(0, 30))
        self.coefDoubleBox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.coefDoubleBox.setMaximum(1000000000000.0)
        self.coefDoubleBox.setObjectName("coefDoubleBox")
        self.gridLayout_7.addWidget(self.coefDoubleBox, 3, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setMinimumSize(QtCore.QSize(0, 0))
        self.label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label.setStyleSheet("font: 75 15pt \"MS Sans Serif\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_7.addWidget(self.label, 2, 0, 1, 3)
        self.currentPolLatex = QtWidgets.QVBoxLayout()
        self.currentPolLatex.setObjectName("currentPolLatex")
        self.gridLayout_7.addLayout(self.currentPolLatex, 7, 1, 2, 1)
        self.gridLayout_6.addWidget(self.widget, 2, 1, 3, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.numLabel = QtWidgets.QLabel(self.frame_2)
        self.numLabel.setMinimumSize(QtCore.QSize(0, 50))
        self.numLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.numLabel.setObjectName("numLabel")
        self.verticalLayout_2.addWidget(self.numLabel)
        self.denLabel = QtWidgets.QLabel(self.frame_2)
        self.denLabel.setMinimumSize(QtCore.QSize(0, 50))
        self.denLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.denLabel.setObjectName("denLabel")
        self.verticalLayout_2.addWidget(self.denLabel)
        self.addFunctionButton = QtWidgets.QPushButton(self.frame_2)
        self.addFunctionButton.setObjectName("addFunctionButton")
        self.verticalLayout_2.addWidget(self.addFunctionButton)
        self.eraseEquationButton = QtWidgets.QPushButton(self.frame_2)
        self.eraseEquationButton.setObjectName("eraseEquationButton")
        self.verticalLayout_2.addWidget(self.eraseEquationButton)
        self.gridLayout_6.addLayout(self.verticalLayout_2, 6, 1, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.numButton = QtWidgets.QRadioButton(self.frame_2)
        self.numButton.setChecked(True)
        self.numButton.setObjectName("numButton")
        self.buttonGroup_2 = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup_2.setObjectName("buttonGroup_2")
        self.buttonGroup_2.addButton(self.numButton)
        self.verticalLayout.addWidget(self.numButton)
        self.denButton = QtWidgets.QRadioButton(self.frame_2)
        self.denButton.setObjectName("denButton")
        self.buttonGroup_2.addButton(self.denButton)
        self.verticalLayout.addWidget(self.denButton)
        self.gridLayout_6.addLayout(self.verticalLayout, 5, 1, 1, 1)
        self.gridLayout_15 = QtWidgets.QGridLayout()
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.csvFreqModeComboBox = QtWidgets.QComboBox(self.frame_2)
        self.csvFreqModeComboBox.setObjectName("csvFreqModeComboBox")
        self.csvFreqModeComboBox.addItem("")
        self.csvFreqModeComboBox.addItem("")
        self.gridLayout_15.addWidget(self.csvFreqModeComboBox, 7, 1, 1, 1)
        self.csvButton = QtWidgets.QPushButton(self.frame_2)
        self.csvButton.setObjectName("csvButton")
        self.gridLayout_15.addWidget(self.csvButton, 5, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.frame_2)
        self.label_10.setMaximumSize(QtCore.QSize(16777215, 50))
        self.label_10.setStyleSheet("font: 75 15pt \"MS Sans Serif\";")
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout_15.addWidget(self.label_10, 0, 0, 1, 2)
        self.spiceButton = QtWidgets.QPushButton(self.frame_2)
        self.spiceButton.setObjectName("spiceButton")
        self.gridLayout_15.addWidget(self.spiceButton, 3, 1, 1, 1)
        self.frequencyButton = QtWidgets.QRadioButton(self.frame_2)
        self.frequencyButton.setChecked(True)
        self.frequencyButton.setObjectName("frequencyButton")
        self.buttonGroup_4 = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup_4.setObjectName("buttonGroup_4")
        self.buttonGroup_4.addButton(self.frequencyButton)
        self.gridLayout_15.addWidget(self.frequencyButton, 7, 0, 1, 1)
        self.temporalButton = QtWidgets.QRadioButton(self.frame_2)
        self.temporalButton.setObjectName("temporalButton")
        self.buttonGroup_4.addButton(self.temporalButton)
        self.gridLayout_15.addWidget(self.temporalButton, 3, 0, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_15, 0, 1, 1, 1)
        self.gridLayout_2.addWidget(self.frame_2, 1, 0, 4, 1)
        self.plotWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.plotWidget.setMinimumSize(QtCore.QSize(800, 0))
        self.plotWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.plotWidget.setObjectName("plotWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.amplitudeBodePlot = QtWidgets.QVBoxLayout()
        self.amplitudeBodePlot.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.amplitudeBodePlot.setObjectName("amplitudeBodePlot")
        self.gridLayout_3.addLayout(self.amplitudeBodePlot, 0, 0, 1, 1)
        self.visualConfWidget = QtWidgets.QWidget(self.tab)
        self.visualConfWidget.setMinimumSize(QtCore.QSize(200, 0))
        self.visualConfWidget.setMaximumSize(QtCore.QSize(300, 16777215))
        self.visualConfWidget.setObjectName("visualConfWidget")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.visualConfWidget)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.eraseBodePlotsButton = QtWidgets.QPushButton(self.visualConfWidget)
        self.eraseBodePlotsButton.setObjectName("eraseBodePlotsButton")
        self.gridLayout_11.addWidget(self.eraseBodePlotsButton, 7, 0, 1, 1)
        self.plotBodeButton = QtWidgets.QPushButton(self.visualConfWidget)
        self.plotBodeButton.setObjectName("plotBodeButton")
        self.gridLayout_11.addWidget(self.plotBodeButton, 6, 0, 1, 1)
        self.gridLayout_19 = QtWidgets.QGridLayout()
        self.gridLayout_19.setObjectName("gridLayout_19")
        self.label_21 = QtWidgets.QLabel(self.visualConfWidget)
        self.label_21.setMaximumSize(QtCore.QSize(16777215, 15))
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName("label_21")
        self.gridLayout_19.addWidget(self.label_21, 2, 2, 1, 1)
        self.minFreqValue = QtWidgets.QDoubleSpinBox(self.visualConfWidget)
        self.minFreqValue.setMinimumSize(QtCore.QSize(0, 30))
        self.minFreqValue.setMinimum(0.01)
        self.minFreqValue.setMaximum(100000.0)
        self.minFreqValue.setProperty("value", 1.0)
        self.minFreqValue.setObjectName("minFreqValue")
        self.gridLayout_19.addWidget(self.minFreqValue, 3, 0, 1, 1)
        self.maxFreqValue = QtWidgets.QDoubleSpinBox(self.visualConfWidget)
        self.maxFreqValue.setMinimumSize(QtCore.QSize(0, 30))
        self.maxFreqValue.setMinimum(0.01)
        self.maxFreqValue.setMaximum(100000.0)
        self.maxFreqValue.setProperty("value", 1.0)
        self.maxFreqValue.setObjectName("maxFreqValue")
        self.gridLayout_19.addWidget(self.maxFreqValue, 3, 2, 1, 1)
        self.minFreqMultiplier = QtWidgets.QSpinBox(self.visualConfWidget)
        self.minFreqMultiplier.setMinimumSize(QtCore.QSize(0, 30))
        self.minFreqMultiplier.setMinimum(-12)
        self.minFreqMultiplier.setMaximum(12)
        self.minFreqMultiplier.setSingleStep(3)
        self.minFreqMultiplier.setObjectName("minFreqMultiplier")
        self.gridLayout_19.addWidget(self.minFreqMultiplier, 3, 1, 1, 1)
        self.maxFreqMultiplier = QtWidgets.QSpinBox(self.visualConfWidget)
        self.maxFreqMultiplier.setMinimumSize(QtCore.QSize(0, 30))
        self.maxFreqMultiplier.setMinimum(-12)
        self.maxFreqMultiplier.setMaximum(12)
        self.maxFreqMultiplier.setSingleStep(3)
        self.maxFreqMultiplier.setProperty("value", 0)
        self.maxFreqMultiplier.setObjectName("maxFreqMultiplier")
        self.gridLayout_19.addWidget(self.maxFreqMultiplier, 3, 3, 1, 1)
        self.freqAxisLogButton = QtWidgets.QRadioButton(self.visualConfWidget)
        self.freqAxisLogButton.setChecked(True)
        self.freqAxisLogButton.setObjectName("freqAxisLogButton")
        self.buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.freqAxisLogButton)
        self.gridLayout_19.addWidget(self.freqAxisLogButton, 1, 0, 1, 2)
        self.label_20 = QtWidgets.QLabel(self.visualConfWidget)
        self.label_20.setMaximumSize(QtCore.QSize(16777215, 15))
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.gridLayout_19.addWidget(self.label_20, 2, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.visualConfWidget)
        self.label_8.setMaximumSize(QtCore.QSize(16777215, 15))
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout_19.addWidget(self.label_8, 0, 0, 1, 3)
        self.freqMode = QtWidgets.QComboBox(self.visualConfWidget)
        self.freqMode.setObjectName("freqMode")
        self.freqMode.addItem("")
        self.freqMode.addItem("")
        self.gridLayout_19.addWidget(self.freqMode, 0, 3, 1, 1)
        self.freqAxisLinealButton = QtWidgets.QRadioButton(self.visualConfWidget)
        self.freqAxisLinealButton.setObjectName("freqAxisLinealButton")
        self.buttonGroup.addButton(self.freqAxisLinealButton)
        self.gridLayout_19.addWidget(self.freqAxisLinealButton, 1, 2, 1, 1)
        self.gridLayout_11.addLayout(self.gridLayout_19, 3, 0, 1, 1)
        self.gridLayout_12 = QtWidgets.QGridLayout()
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.label_11 = QtWidgets.QLabel(self.visualConfWidget)
        self.label_11.setObjectName("label_11")
        self.gridLayout_12.addWidget(self.label_11, 0, 0, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.visualConfWidget)
        self.label_18.setObjectName("label_18")
        self.gridLayout_12.addWidget(self.label_18, 1, 0, 1, 1)
        self.phaseTitle = QtWidgets.QLineEdit(self.visualConfWidget)
        self.phaseTitle.setObjectName("phaseTitle")
        self.gridLayout_12.addWidget(self.phaseTitle, 0, 1, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.visualConfWidget)
        self.label_19.setObjectName("label_19")
        self.gridLayout_12.addWidget(self.label_19, 2, 0, 1, 1)
        self.phaseXLabel = QtWidgets.QLineEdit(self.visualConfWidget)
        self.phaseXLabel.setObjectName("phaseXLabel")
        self.gridLayout_12.addWidget(self.phaseXLabel, 1, 1, 1, 1)
        self.phaseYLabel = QtWidgets.QLineEdit(self.visualConfWidget)
        self.phaseYLabel.setObjectName("phaseYLabel")
        self.gridLayout_12.addWidget(self.phaseYLabel, 2, 1, 1, 1)
        self.gridLayout_11.addLayout(self.gridLayout_12, 5, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setVerticalSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.yAxisLinealButton = QtWidgets.QRadioButton(self.visualConfWidget)
        self.yAxisLinealButton.setChecked(False)
        self.yAxisLinealButton.setObjectName("yAxisLinealButton")
        self.buttonGroup_3 = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup_3.setObjectName("buttonGroup_3")
        self.buttonGroup_3.addButton(self.yAxisLinealButton)
        self.gridLayout.addWidget(self.yAxisLinealButton, 5, 1, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.visualConfWidget)
        self.label_17.setObjectName("label_17")
        self.gridLayout.addWidget(self.label_17, 4, 0, 1, 2)
        self.yAxisDBButton = QtWidgets.QRadioButton(self.visualConfWidget)
        self.yAxisDBButton.setChecked(True)
        self.yAxisDBButton.setObjectName("yAxisDBButton")
        self.buttonGroup_3.addButton(self.yAxisDBButton)
        self.gridLayout.addWidget(self.yAxisDBButton, 5, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.visualConfWidget)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 3, 0, 1, 2)
        self.ampYLabel = QtWidgets.QLineEdit(self.visualConfWidget)
        self.ampYLabel.setObjectName("ampYLabel")
        self.gridLayout.addWidget(self.ampYLabel, 4, 2, 1, 1)
        self.ampXLabel = QtWidgets.QLineEdit(self.visualConfWidget)
        self.ampXLabel.setObjectName("ampXLabel")
        self.gridLayout.addWidget(self.ampXLabel, 3, 2, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.visualConfWidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 0, 0, 1, 2)
        self.ampTitle = QtWidgets.QLineEdit(self.visualConfWidget)
        self.ampTitle.setObjectName("ampTitle")
        self.gridLayout.addWidget(self.ampTitle, 0, 2, 1, 1)
        self.gridLayout_11.addLayout(self.gridLayout, 4, 0, 1, 1)
        self.gridLayout_3.addWidget(self.visualConfWidget, 0, 1, 2, 1)
        self.phaseBodePlot = QtWidgets.QVBoxLayout()
        self.phaseBodePlot.setObjectName("phaseBodePlot")
        self.gridLayout_3.addLayout(self.phaseBodePlot, 1, 0, 1, 1)
        self.plotWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.visualConfWidget_2 = QtWidgets.QWidget(self.tab_2)
        self.visualConfWidget_2.setMinimumSize(QtCore.QSize(200, 0))
        self.visualConfWidget_2.setObjectName("visualConfWidget_2")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.visualConfWidget_2)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.widget_3 = QtWidgets.QWidget(self.visualConfWidget_2)
        self.widget_3.setMinimumSize(QtCore.QSize(250, 200))
        self.widget_3.setMaximumSize(QtCore.QSize(300, 16777215))
        self.widget_3.setObjectName("widget_3")
        self.gridLayout_16 = QtWidgets.QGridLayout(self.widget_3)
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.maxTimeValue = QtWidgets.QDoubleSpinBox(self.widget_3)
        self.maxTimeValue.setMinimum(-10000000000000.0)
        self.maxTimeValue.setMaximum(1000000000.0)
        self.maxTimeValue.setObjectName("maxTimeValue")
        self.horizontalLayout_5.addWidget(self.maxTimeValue)
        self.maxTimeMultiplier = QtWidgets.QSpinBox(self.widget_3)
        self.maxTimeMultiplier.setMinimum(-12)
        self.maxTimeMultiplier.setMaximum(12)
        self.maxTimeMultiplier.setSingleStep(3)
        self.maxTimeMultiplier.setObjectName("maxTimeMultiplier")
        self.horizontalLayout_5.addWidget(self.maxTimeMultiplier)
        self.gridLayout_16.addLayout(self.horizontalLayout_5, 5, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_16.addWidget(self.label_2, 0, 0, 1, 4)
        self.entradaComboBox = QtWidgets.QComboBox(self.widget_3)
        self.entradaComboBox.setObjectName("entradaComboBox")
        self.entradaComboBox.addItem("")
        self.entradaComboBox.addItem("")
        self.entradaComboBox.addItem("")
        self.gridLayout_16.addWidget(self.entradaComboBox, 1, 0, 1, 4)
        self.addTemporalFunctionButton = QtWidgets.QPushButton(self.widget_3)
        self.addTemporalFunctionButton.setObjectName("addTemporalFunctionButton")
        self.gridLayout_16.addWidget(self.addTemporalFunctionButton, 8, 0, 1, 4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.minTimeValue = QtWidgets.QDoubleSpinBox(self.widget_3)
        self.minTimeValue.setMinimum(-1000000000.0)
        self.minTimeValue.setMaximum(1000000000.0)
        self.minTimeValue.setObjectName("minTimeValue")
        self.horizontalLayout_3.addWidget(self.minTimeValue)
        self.minTimeMultiplier = QtWidgets.QSpinBox(self.widget_3)
        self.minTimeMultiplier.setMinimum(-12)
        self.minTimeMultiplier.setMaximum(12)
        self.minTimeMultiplier.setSingleStep(3)
        self.minTimeMultiplier.setObjectName("minTimeMultiplier")
        self.horizontalLayout_3.addWidget(self.minTimeMultiplier)
        self.gridLayout_16.addLayout(self.horizontalLayout_3, 5, 0, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.widget_3)
        self.label_23.setAlignment(QtCore.Qt.AlignCenter)
        self.label_23.setObjectName("label_23")
        self.gridLayout_16.addWidget(self.label_23, 4, 1, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.widget_3)
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_22.setObjectName("label_22")
        self.gridLayout_16.addWidget(self.label_22, 4, 0, 1, 1)
        self.entradaConfStacked = QtWidgets.QStackedWidget(self.widget_3)
        self.entradaConfStacked.setMaximumSize(QtCore.QSize(16777215, 200))
        self.entradaConfStacked.setObjectName("entradaConfStacked")
        self.ampFrecPage = QtWidgets.QWidget()
        self.ampFrecPage.setObjectName("ampFrecPage")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.ampFrecPage)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.label_5 = QtWidgets.QLabel(self.ampFrecPage)
        self.label_5.setObjectName("label_5")
        self.gridLayout_10.addWidget(self.label_5, 2, 0, 1, 1)
        self.offsetMultiplier = QtWidgets.QSpinBox(self.ampFrecPage)
        self.offsetMultiplier.setMinimum(-12)
        self.offsetMultiplier.setMaximum(12)
        self.offsetMultiplier.setSingleStep(3)
        self.offsetMultiplier.setObjectName("offsetMultiplier")
        self.gridLayout_10.addWidget(self.offsetMultiplier, 2, 2, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.ampFrecPage)
        self.label_7.setObjectName("label_7")
        self.gridLayout_10.addWidget(self.label_7, 0, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.ampFrecPage)
        self.label_13.setObjectName("label_13")
        self.gridLayout_10.addWidget(self.label_13, 3, 0, 1, 1)
        self.amplitudeDoubleBox = QtWidgets.QDoubleSpinBox(self.ampFrecPage)
        self.amplitudeDoubleBox.setMinimum(0.01)
        self.amplitudeDoubleBox.setMaximum(10000000000.0)
        self.amplitudeDoubleBox.setProperty("value", 1.0)
        self.amplitudeDoubleBox.setObjectName("amplitudeDoubleBox")
        self.gridLayout_10.addWidget(self.amplitudeDoubleBox, 1, 1, 1, 1)
        self.freqDoubleBox = QtWidgets.QDoubleSpinBox(self.ampFrecPage)
        self.freqDoubleBox.setMinimum(0.01)
        self.freqDoubleBox.setMaximum(10000000000.0)
        self.freqDoubleBox.setProperty("value", 1.0)
        self.freqDoubleBox.setObjectName("freqDoubleBox")
        self.gridLayout_10.addWidget(self.freqDoubleBox, 0, 1, 1, 1)
        self.freqMultiplicador = QtWidgets.QSpinBox(self.ampFrecPage)
        self.freqMultiplicador.setMinimum(-12)
        self.freqMultiplicador.setMaximum(12)
        self.freqMultiplicador.setSingleStep(3)
        self.freqMultiplicador.setObjectName("freqMultiplicador")
        self.gridLayout_10.addWidget(self.freqMultiplicador, 0, 2, 1, 1)
        self.offsetDoubleBox = QtWidgets.QDoubleSpinBox(self.ampFrecPage)
        self.offsetDoubleBox.setObjectName("offsetDoubleBox")
        self.gridLayout_10.addWidget(self.offsetDoubleBox, 2, 1, 1, 1)
        self.amplitudeMultiplicador = QtWidgets.QSpinBox(self.ampFrecPage)
        self.amplitudeMultiplicador.setMinimum(-12)
        self.amplitudeMultiplicador.setMaximum(12)
        self.amplitudeMultiplicador.setSingleStep(3)
        self.amplitudeMultiplicador.setObjectName("amplitudeMultiplicador")
        self.gridLayout_10.addWidget(self.amplitudeMultiplicador, 1, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.ampFrecPage)
        self.label_6.setObjectName("label_6")
        self.gridLayout_10.addWidget(self.label_6, 1, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.ampFrecPage)
        self.label_14.setObjectName("label_14")
        self.gridLayout_10.addWidget(self.label_14, 4, 0, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.ampFrecPage)
        self.label_15.setObjectName("label_15")
        self.gridLayout_10.addWidget(self.label_15, 5, 0, 1, 1)
        self.phaseSpinBox = QtWidgets.QDoubleSpinBox(self.ampFrecPage)
        self.phaseSpinBox.setMinimum(-360.0)
        self.phaseSpinBox.setMaximum(360.0)
        self.phaseSpinBox.setObjectName("phaseSpinBox")
        self.gridLayout_10.addWidget(self.phaseSpinBox, 3, 1, 1, 1)
        self.dutyCycleDoubleBox = QtWidgets.QDoubleSpinBox(self.ampFrecPage)
        self.dutyCycleDoubleBox.setMaximum(100.0)
        self.dutyCycleDoubleBox.setObjectName("dutyCycleDoubleBox")
        self.gridLayout_10.addWidget(self.dutyCycleDoubleBox, 4, 1, 1, 1)
        self.simetryDoubleBox = QtWidgets.QDoubleSpinBox(self.ampFrecPage)
        self.simetryDoubleBox.setMaximum(100.0)
        self.simetryDoubleBox.setObjectName("simetryDoubleBox")
        self.gridLayout_10.addWidget(self.simetryDoubleBox, 5, 1, 1, 1)
        self.entradaConfStacked.addWidget(self.ampFrecPage)
        self.gridLayout_16.addWidget(self.entradaConfStacked, 2, 0, 1, 4)
        self.label_16 = QtWidgets.QLabel(self.widget_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.gridLayout_16.addWidget(self.label_16, 3, 0, 1, 3)
        self.gridLayout_22 = QtWidgets.QGridLayout()
        self.gridLayout_22.setObjectName("gridLayout_22")
        self.label_25 = QtWidgets.QLabel(self.widget_3)
        self.label_25.setObjectName("label_25")
        self.gridLayout_22.addWidget(self.label_25, 2, 0, 1, 1)
        self.temporalYLabel = QtWidgets.QLineEdit(self.widget_3)
        self.temporalYLabel.setObjectName("temporalYLabel")
        self.gridLayout_22.addWidget(self.temporalYLabel, 2, 1, 1, 1)
        self.temporalXLabel = QtWidgets.QLineEdit(self.widget_3)
        self.temporalXLabel.setObjectName("temporalXLabel")
        self.gridLayout_22.addWidget(self.temporalXLabel, 1, 1, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.widget_3)
        self.label_24.setObjectName("label_24")
        self.gridLayout_22.addWidget(self.label_24, 1, 0, 1, 1)
        self.temporalTitle = QtWidgets.QLineEdit(self.widget_3)
        self.temporalTitle.setObjectName("temporalTitle")
        self.gridLayout_22.addWidget(self.temporalTitle, 0, 1, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.widget_3)
        self.label_26.setObjectName("label_26")
        self.gridLayout_22.addWidget(self.label_26, 0, 0, 1, 1)
        self.gridLayout_16.addLayout(self.gridLayout_22, 9, 0, 1, 2)
        self.gridLayout_13.addWidget(self.widget_3, 0, 1, 1, 1)
        self.eraseTemporalPlotsButton = QtWidgets.QPushButton(self.visualConfWidget_2)
        self.eraseTemporalPlotsButton.setObjectName("eraseTemporalPlotsButton")
        self.gridLayout_13.addWidget(self.eraseTemporalPlotsButton, 2, 1, 1, 1)
        self.plotTemporalButton = QtWidgets.QPushButton(self.visualConfWidget_2)
        self.plotTemporalButton.setObjectName("plotTemporalButton")
        self.gridLayout_13.addWidget(self.plotTemporalButton, 1, 1, 1, 1)
        self.temporalResponsePlot = QtWidgets.QVBoxLayout()
        self.temporalResponsePlot.setObjectName("temporalResponsePlot")
        self.gridLayout_13.addLayout(self.temporalResponsePlot, 0, 0, 3, 1)
        self.gridLayout_4.addWidget(self.visualConfWidget_2, 0, 0, 2, 1)
        self.plotWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.zerosPolesPlot = QtWidgets.QWidget(self.tab_3)
        self.zerosPolesPlot.setObjectName("zerosPolesPlot")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.zerosPolesPlot)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.gridLayout_23 = QtWidgets.QGridLayout()
        self.gridLayout_23.setObjectName("gridLayout_23")
        self.polesTitle = QtWidgets.QLineEdit(self.zerosPolesPlot)
        self.polesTitle.setObjectName("polesTitle")
        self.gridLayout_23.addWidget(self.polesTitle, 0, 1, 1, 1)
        self.label_28 = QtWidgets.QLabel(self.zerosPolesPlot)
        self.label_28.setObjectName("label_28")
        self.gridLayout_23.addWidget(self.label_28, 1, 0, 1, 1)
        self.label_29 = QtWidgets.QLabel(self.zerosPolesPlot)
        self.label_29.setObjectName("label_29")
        self.gridLayout_23.addWidget(self.label_29, 2, 0, 1, 1)
        self.label_27 = QtWidgets.QLabel(self.zerosPolesPlot)
        self.label_27.setObjectName("label_27")
        self.gridLayout_23.addWidget(self.label_27, 0, 0, 1, 1)
        self.polesXLabel = QtWidgets.QLineEdit(self.zerosPolesPlot)
        self.polesXLabel.setObjectName("polesXLabel")
        self.gridLayout_23.addWidget(self.polesXLabel, 1, 1, 1, 1)
        self.polesYLabel = QtWidgets.QLineEdit(self.zerosPolesPlot)
        self.polesYLabel.setObjectName("polesYLabel")
        self.gridLayout_23.addWidget(self.polesYLabel, 2, 1, 1, 1)
        self.verticalLayout_9.addLayout(self.gridLayout_23)
        self.addPolesZeros = QtWidgets.QPushButton(self.zerosPolesPlot)
        self.addPolesZeros.setObjectName("addPolesZeros")
        self.verticalLayout_9.addWidget(self.addPolesZeros)
        self.erasePolesPlotButton = QtWidgets.QPushButton(self.zerosPolesPlot)
        self.erasePolesPlotButton.setObjectName("erasePolesPlotButton")
        self.verticalLayout_9.addWidget(self.erasePolesPlotButton)
        self.gridLayout_9.addLayout(self.verticalLayout_9, 0, 1, 2, 1)
        self.polesZerosPlot = QtWidgets.QVBoxLayout()
        self.polesZerosPlot.setObjectName("polesZerosPlot")
        self.gridLayout_9.addLayout(self.polesZerosPlot, 0, 0, 2, 1)
        self.gridLayout_5.addWidget(self.zerosPolesPlot, 0, 0, 1, 1)
        self.plotWidget.addTab(self.tab_3, "")
        self.gridLayout_2.addWidget(self.plotWidget, 1, 1, 4, 1)
        self.deleteAllFunctionsButton = QtWidgets.QPushButton(self.centralwidget)
        self.deleteAllFunctionsButton.setObjectName("deleteAllFunctionsButton")
        self.gridLayout_2.addWidget(self.deleteAllFunctionsButton, 4, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.plotWidget.setCurrentIndex(0)
        self.entradaConfStacked.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.deleteFunctionsButton.setText(_translate("MainWindow", "Borrar Funciones"))
        self.erasePolinomialButton.setText(_translate("MainWindow", "Borrar Polinomio"))
        self.currentPolLabel.setText(_translate("MainWindow", "1"))
        self.label_4.setText(_translate("MainWindow", "Coeficiente"))
        self.addTermButton.setText(_translate("MainWindow", "Agregar Término"))
        self.addPolinomialButton.setText(_translate("MainWindow", "Agregar polinomio"))
        self.label_3.setText(_translate("MainWindow", "Orden (s^)"))
        self.label.setText(_translate("MainWindow", "Función Transferencia"))
        self.numLabel.setText(_translate("MainWindow", "1"))
        self.denLabel.setText(_translate("MainWindow", "1"))
        self.addFunctionButton.setText(_translate("MainWindow", "Agregar Función"))
        self.eraseEquationButton.setText(_translate("MainWindow", "Borrar Ecuación"))
        self.numButton.setText(_translate("MainWindow", "Numerador"))
        self.denButton.setText(_translate("MainWindow", "Denominador"))
        self.csvFreqModeComboBox.setItemText(0, _translate("MainWindow", "dB"))
        self.csvFreqModeComboBox.setItemText(1, _translate("MainWindow", "Lineal"))
        self.csvButton.setText(_translate("MainWindow", "CSV"))
        self.label_10.setText(_translate("MainWindow", "Importar de archivo"))
        self.spiceButton.setText(_translate("MainWindow", "Spice"))
        self.frequencyButton.setText(_translate("MainWindow", "Frecuencia/Bode"))
        self.temporalButton.setText(_translate("MainWindow", "Temporal"))
        self.eraseBodePlotsButton.setText(_translate("MainWindow", "Borrar gráficos Bode"))
        self.plotBodeButton.setText(_translate("MainWindow", "Graficar Bode"))
        self.label_21.setText(_translate("MainWindow", "Max"))
        self.freqAxisLogButton.setText(_translate("MainWindow", "Logarítmico"))
        self.label_20.setText(_translate("MainWindow", "Min"))
        self.label_8.setText(_translate("MainWindow", "Rango frecuencias"))
        self.freqMode.setItemText(0, _translate("MainWindow", "Hz"))
        self.freqMode.setItemText(1, _translate("MainWindow", "Rad/s"))
        self.freqAxisLinealButton.setText(_translate("MainWindow", "Lineal"))
        self.label_11.setText(_translate("MainWindow", "Fase Título"))
        self.label_18.setText(_translate("MainWindow", "Fase X Label"))
        self.label_19.setText(_translate("MainWindow", "Fase Y Label"))
        self.yAxisLinealButton.setText(_translate("MainWindow", "Lineal"))
        self.label_17.setText(_translate("MainWindow", "Amplitud Y Label"))
        self.yAxisDBButton.setText(_translate("MainWindow", "dB"))
        self.label_12.setText(_translate("MainWindow", "Amplitud X Label"))
        self.label_9.setText(_translate("MainWindow", "Amplitud Título"))
        self.plotWidget.setTabText(self.plotWidget.indexOf(self.tab), _translate("MainWindow", "Bode"))
        self.label_2.setText(_translate("MainWindow", "Configuración función"))
        self.entradaComboBox.setItemText(0, _translate("MainWindow", "Senoide"))
        self.entradaComboBox.setItemText(1, _translate("MainWindow", "Cuadrada"))
        self.entradaComboBox.setItemText(2, _translate("MainWindow", "Rampa"))
        self.addTemporalFunctionButton.setText(_translate("MainWindow", "Agregar señal temporal"))
        self.label_23.setText(_translate("MainWindow", "Max"))
        self.label_22.setText(_translate("MainWindow", "Min"))
        self.label_5.setText(_translate("MainWindow", "Offset [V]"))
        self.label_7.setText(_translate("MainWindow", "Frecuencia [Hz]"))
        self.label_13.setText(_translate("MainWindow", "Fase [°]"))
        self.label_6.setText(_translate("MainWindow", "Amplitud [V]"))
        self.label_14.setText(_translate("MainWindow", "Duty Cycle [%]"))
        self.label_15.setText(_translate("MainWindow", "Simetría [%] (rampa)"))
        self.label_16.setText(_translate("MainWindow", "Rango de tiempo [s]"))
        self.label_25.setText(_translate("MainWindow", "Y Label"))
        self.label_24.setText(_translate("MainWindow", "X Label"))
        self.label_26.setText(_translate("MainWindow", "Título"))
        self.eraseTemporalPlotsButton.setText(_translate("MainWindow", "Borrar gráficos de señales temporales"))
        self.plotTemporalButton.setText(_translate("MainWindow", "Graficar señales temporales"))
        self.plotWidget.setTabText(self.plotWidget.indexOf(self.tab_2), _translate("MainWindow", "Respuesta Temporal"))
        self.label_28.setText(_translate("MainWindow", "X Label"))
        self.label_29.setText(_translate("MainWindow", "Y Label"))
        self.label_27.setText(_translate("MainWindow", "Título"))
        self.addPolesZeros.setText(_translate("MainWindow", "Graficar Polos y Ceros"))
        self.erasePolesPlotButton.setText(_translate("MainWindow", "Borrar gráfico de polos y ceros"))
        self.plotWidget.setTabText(self.plotWidget.indexOf(self.tab_3), _translate("MainWindow", "Polos y Ceros"))
        self.deleteAllFunctionsButton.setText(_translate("MainWindow", "Borrar todas las funciones"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
