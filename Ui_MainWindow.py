# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# The user interface, modified from what was originally created in QT designer
# Form implementation generated from reading ui file 'mainui.ui'
#
#
# waitingspinnerwidget' is copyrighted by Alexander Turkin, William Hallatt, Jacob Dawid,
# and Luca Weiss, and is licensed under The MIT License(MIT).
# See the attached license file in the 'waitingspinnerwidget' folder
#
# Created by: PyQt5 UI code generator 5.12.1
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import QColor, QFont

from waitingspinnerwidget.waitingspinnerwidget import QtWaitingSpinner


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 480)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.instr_lbl = QtWidgets.QLabel(self.centralwidget)
        self.instr_lbl.setGeometry(QtCore.QRect(135, 12, 400, 40))
        self.instr_lbl.setObjectName("instr_lbl")
        self.training_lbl = QtWidgets.QLabel(self.centralwidget)
        self.training_lbl.setGeometry(QtCore.QRect(70, 70, 190, 16))
        self.training_lbl.setObjectName("training_lbl")
        self.test_lbl = QtWidgets.QLabel(self.centralwidget)
        self.test_lbl.setGeometry(QtCore.QRect(70, 130, 190, 21))
        self.test_lbl.setObjectName("test_lbl")
        self.epoch_lbl = QtWidgets.QLabel(self.centralwidget)
        self.epoch_lbl.setGeometry(QtCore.QRect(70, 200, 190, 16))
        self.epoch_lbl.setObjectName("epoch_lbl")
        self.optimizer_lbl = QtWidgets.QLabel(self.centralwidget)
        self.optimizer_lbl.setGeometry(QtCore.QRect(70, 240, 190, 16))
        self.optimizer_lbl.setObjectName("optimizer_lbl")
        self.layer1_lbl = QtWidgets.QLabel(self.centralwidget)
        self.layer1_lbl.setGeometry(70, 270, 190, 16)
        self.layer1_lbl.setObjectName("layer1_lbl")
        self.layer2_lbl = QtWidgets.QLabel(self.centralwidget)
        self.layer2_lbl.setGeometry(70, 290, 190, 16)
        self.layer2_lbl.setObjectName("layer2_lbl")
        self.layer3_lbl = QtWidgets.QLabel(self.centralwidget)
        self.layer3_lbl.setGeometry(70, 310, 190, 16)
        self.layer3_lbl.setObjectName("layer3_lbl")

        self.test_browse_btn = QtWidgets.QPushButton(self.centralwidget)
        self.test_browse_btn.setGeometry(QtCore.QRect(260, 130, 75, 23))
        self.test_browse_btn.setObjectName("test_btn")
        self.load_test_btn = QtWidgets.QPushButton(self.centralwidget)
        self.load_test_btn.setGeometry(QtCore.QRect(260, 160, 75, 23))
        self.load_test_btn.setObjectName("load_test_btn")

        self.load_train_btn = QtWidgets.QPushButton(self.centralwidget)
        self.load_train_btn.setGeometry(QtCore.QRect(260, 100, 75, 23))
        self.load_train_btn.setObjectName("load_train_btn")
        self.train_browse_button = QtWidgets.QPushButton(self.centralwidget)
        self.train_browse_button.setGeometry(QtCore.QRect(260, 70, 75, 23))
        self.train_browse_button.setObjectName("training_btn")

        self.test_path = QtWidgets.QLineEdit(self.centralwidget)
        self.test_path.setGeometry(QtCore.QRect(350, 130, 113, 23))
        self.test_path.setObjectName("test_path")
        self.test_data_progress = QtWidgets.QProgressBar(self.centralwidget)
        self.test_data_progress.setGeometry(QtCore.QRect(350, 160, 150, 23))
        self.test_data_progress.setObjectName("test_data_progress")

        self.training_path = QtWidgets.QLineEdit(self.centralwidget)
        self.training_path.setGeometry(QtCore.QRect(350, 70, 113, 23))
        self.training_path.setObjectName("training_path")
        self.training_data_progress = QtWidgets.QProgressBar(self.centralwidget)
        self.training_data_progress.setGeometry(QtCore.QRect(350, 100, 150, 23))
        self.training_data_progress.setObjectName("training_data_progress")

        self.epoch_edit = QtWidgets.QSpinBox(self.centralwidget)
        self.epoch_edit.setGeometry(QtCore.QRect(280, 200, 190, 22))
        self.epoch_edit.setObjectName("epoch_edit")
        self.epoch_edit.setValue(1)
        self.epoch_edit.setMaximum(10000)
        self.epoch_edit.setMinimum(1)

        self.layer1_txt = QtWidgets.QSpinBox(self.centralwidget)
        self.layer1_txt.setGeometry(QtCore.QRect(280, 270, 190, 22))
        self.layer1_txt.setValue(90)
        self.layer1_txt.setMaximum(10000)
        self.layer1_txt.setMinimum(1)
        self.layer2_txt = QtWidgets.QSpinBox(self.centralwidget)
        self.layer2_txt.setGeometry(QtCore.QRect(280, 290, 190, 22))
        self.layer2_txt.setValue(90)
        self.layer2_txt.setMaximum(10000)
        self.layer2_txt.setMinimum(1)
        self.layer3_txt = QtWidgets.QSpinBox(self.centralwidget)
        self.layer3_txt.setGeometry(QtCore.QRect(280, 310, 190, 22))
        self.layer3_txt.setValue(10)
        self.layer3_txt.setMaximum(10000)
        self.layer3_txt.setMinimum(1)

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(280, 240, 190, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.create_btn = QtWidgets.QPushButton(self.centralwidget)
        self.create_btn.setGeometry(QtCore.QRect(240, 340, 90, 23))
        self.create_btn.setObjectName("create_btn")

        self.spinner = QtWaitingSpinner(self.centralwidget, True, True, Qt.ApplicationModal)
        self.spinner.setRoundness(70.0)
        self.spinner.setMinimumTrailOpacity(15.0)
        self.spinner.setTrailFadePercentage(70.0)
        self.spinner.setNumberOfLines(12)
        self.spinner.setLineLength(10)
        self.spinner.setLineWidth(5)
        self.spinner.setInnerRadius(10)
        self.spinner.setRevolutionsPerSecond(1)
        self.spinner.setColor(QColor(81, 4, 71))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.training_lbl.setText(_translate("MainWindow", "Select training data folder"))
        self.test_lbl.setText(_translate("MainWindow", "Select test data folder"))
        self.optimizer_lbl.setText(_translate("MainWindow", "Select optimizer"))
        self.train_browse_button.setText(_translate("MainWindow", "Browse"))
        self.test_browse_btn.setText(_translate("MainWindow", "Browse"))
        self.create_btn.setText(_translate("MainWindow", "Create Model"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Adam"))
        self.comboBox.setItemText(1, _translate("MainWindow", "SGD"))
        self.load_test_btn.setText(_translate("MainWindow", "Load data"))
        self.load_train_btn.setText(_translate("MainWindow", "Load data"))
        self.instr_lbl.setText(_translate("MainWindow", "          Choose folders for "
                                                        "the test and training data. \n"
                                                        "They must each contain"
                                                        " subdirectories with "
                                                        "the class labels."
                                                        ""))
        self.epoch_lbl.setText(_translate("MainWindow", "Choose number of epochs"))
        self.layer1_lbl.setText(_translate("MainWindow", "Number of neurons for layer 1"))
        self.layer2_lbl.setText(_translate("MainWindow", "Number of neurons for layer 2"))
        self.layer3_lbl.setText(_translate("MainWindow", "Number of neurons for layer 3"))
