# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Zane Rammal
#
# This is an exercise where I have the basics of Keras
# configurable through a PyQT5 GUI
#
# Licensed Under GNU GPL Version 3
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import ctypes
import os
import random
import sys
import threading
import time
from pathlib import Path
from tkinter import Tk
from tkinter import filedialog

import cv2
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import (QApplication)
from PyQt5.QtWidgets import (QMainWindow)

import Ui_MainWindow


class MainWindow(QMainWindow):
    # QT Signals so actions can be triggered in other threads but
    # still run in the main thread
    done_test = pyqtSignal()
    update_test = pyqtSignal(int)
    done_train = pyqtSignal()
    update_train = pyqtSignal(int)
    done_data = pyqtSignal()
    done_model = pyqtSignal()
    display_sig = pyqtSignal(tf.keras.callbacks.History)

    train_path = " "
    test_path = " "
    training_data = []
    testing_data = []
    x_train = []
    y_train = []
    x_test = []
    y_test = []
    num_epochs = ""
    opt = "Adam"
    is_training_loaded = False
    is_test_loaded = False
    model_exists = False
    layer1_neurons = 99
    layer2_neurons = 99
    layer3_neurons = 10
    img_size = 120

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow.Ui_MainWindow()
        self.ui.setupUi(self)

        self.update_test.connect(self.ui.test_data_progress.setValue)
        self.update_train.connect(self.ui.training_data_progress.setValue)
        self.done_model.connect(self.ui.spinner.stop)
        self.done_data.connect(self.allow_model_creation)
        self.display_sig.connect(self.display_plot)
        self.done_train.connect(self.train_load_done)
        self.done_test.connect(self.test_load_done)

        self.ui.load_test_btn.clicked.connect(self.test_check)
        self.ui.load_train_btn.clicked.connect(self.training_check)
        self.ui.test_browse_btn.clicked.connect(self.test_browse)
        self.ui.train_browse_button.clicked.connect(self.training_browse)
        self.ui.create_btn.clicked.connect(self.create_model_thread)
        self.ui.create_btn.setEnabled(False)

    # Plot training results
    def display_plot(self, history):
        plt.plot(history.history['loss'])
        plt.plot(history.history['acc'])
        plt.title('Error vs Accuracy')
        plt.ylabel('loss')
        plt.xlabel('accuracy')
        plt.show()

    # Enable the buttons to create the model
    # or change the data after loading is
    # complete
    def train_load_done(self):
        self.ui.load_train_btn.setEnabled(True)
        self.ui.train_browse_button.setEnabled(True)
        self.ui.training_data_progress.setValue(100)

    def test_load_done(self):
        self.ui.load_test_btn.setEnabled(True)
        self.ui.test_browse_btn.setEnabled(True)
        self.ui.test_data_progress.setValue(100)

    def allow_model_creation(self):
        self.ui.create_btn.setEnabled(True)

    # Use Tkinter to select the data folders
    # and store the path in the text box
    def training_browse(self):
        root = Tk()
        root.withdraw()
        dir_path = filedialog.askdirectory()
        self.ui.training_path.setText(dir_path)

    def test_browse(self):
        root = Tk()
        root.withdraw()
        dir_path = filedialog.askdirectory()
        self.ui.test_path.setText(dir_path)

    # Check validity of selected folders.
    # If valid, start fetching the data in
    # different threads
    def training_check(self):
        self.ui.load_train_btn.setEnabled(False)
        self.ui.train_browse_button.setEnabled(False)
        self.train_path = self.ui.training_path.text()
        path = Path(self.train_path)

        if path.exists() and self.train_path != '':
            self.thread = threading.Thread(target=self.load_training_data)
            self.thread.start()
        else:
            self.ui.train_browse_button.setEnabled(True)
            self.ui.load_train_btn.setEnabled(True)
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage('The folder you chose does not exist!')
            error_dialog.exec_()

    def test_check(self):
        self.ui.load_test_btn.setEnabled(False)
        self.ui.test_browse_btn.setEnabled(False)
        self.test_path = self.ui.test_path.text()
        path = Path(self.test_path)

        if path.exists() and self.test_path != '':
            self.thread2 = threading.Thread(target=self.get_test_data)
            self.thread2.start()
        else:
            self.ui.test_browse_btn.setEnabled(True)
            self.ui.load_test_btn.setEnabled(True)
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage('The folder you chose does not exist!')
            error_dialog.exec_()

    def get_test_data(self):
        count = 0
        sub_dirs = [d for d in os.listdir(self.test_path) if os.path.isdir(os.path.join(self.test_path, d))]
        class_labels = sub_dirs

        for category in class_labels:
            path = os.path.join(self.test_path, category)
            class_num = class_labels.index(category)
            for img in os.listdir(path):
                try:
                    img_array = cv2.resize(cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE),
                                           (self.img_size, self.img_size))
                    self.testing_data.append([img_array, class_num])
                except:
                    pass

                # Update the progress bar with the current percentage of images added
                count = count + 1 / (len(class_labels))
                percent = ((count / (len(os.listdir(path)))) * 100)
                self.update_test.emit(percent)

        self.done_test.emit()
        self.is_test_loaded = True
        if self.is_training_loaded is True & self.is_test_loaded is True:
            self.done_data.emit()

    def load_training_data(self):
        count = 0
        sub_dirs = [d for d in os.listdir(self.train_path) if os.path.isdir(os.path.join(self.train_path, d))]
        class_labels = sub_dirs

        for category in class_labels:
            path = os.path.join(self.train_path, category)
            class_num = class_labels.index(category)
            for img in os.listdir(path):
                try:
                    img_array = cv2.resize(cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE),
                                           (self.img_size, self.img_size))
                    self.training_data.append([img_array, class_num])
                except:
                    pass

                # Update the progress bar with the current percentage of images added
                count = count + 1 / (len(class_labels))
                percent = ((count / (len(os.listdir(path)))) * 100)
                self.update_train.emit(percent)

        self.done_train.emit()
        self.is_training_loaded = True
        if self.is_training_loaded is True & self.is_test_loaded is True:
            self.done_data.emit()

    # Gathers user customizable model parameters and
    # starts the thread that trains it
    def create_model_thread(self):

        self.ui.create_btn.setEnabled(True)

        # Get epochs, neurons, and optimizer from GUI
        self.num_epochs = self.ui.epoch_edit.text()
        if 'Adam' in self.ui.comboBox.currentText():
            self.opt = 'Adam'
        if 'SGD' in self.ui.comboBox.currentText():
            self.opt = 'sgd'

        self.layer1_neurons = self.ui.layer1_txt.text()
        self.layer2_neurons = self.ui.layer2_txt.text()
        self.layer3_neurons = self.ui.layer3_txt.text()

        # Start the spinner
        self.ui.spinner.start()

        # Run the training in a different thread
        self.thread3 = threading.Thread(target=self.create_model)
        self.thread3.start()

    def create_model(self):

        if self.model_exists is False:
            for features1, label1 in self.training_data:
                self.x_train.append(features1)
                self.y_train.append(label1)
            for features2, label2 in self.testing_data:
                self.x_test.append(features2)
                self.y_test.append(label2)

            # Shape data
            self.x_train = np.array(self.x_train).reshape(-1, self.img_size, self.img_size, 1)
            self.x_test = np.array(self.x_test).reshape(-1, self.img_size, self.img_size, 1)
            self.y_train = np.array(self.y_train)
            self.y_test = np.array(self.y_test)

            # Randomize data
            random.shuffle(self.x_train)
            random.shuffle(self.x_test)

            # Normalize the data
            self.x_train = tf.keras.utils.normalize(self.x_train, axis=1)
            self.x_test = tf.keras.utils.normalize(self.x_test, axis=1)
            self.model_exists = True

        # Create neural network
        model = tf.keras.models.Sequential()
        model.add(tf.keras.layers.Flatten())
        model.add(tf.keras.layers.Dense(self.layer1_neurons, activation=tf.nn.relu))
        model.add(tf.keras.layers.Dense(self.layer2_neurons, activation=tf.nn.relu))
        model.add(tf.keras.layers.Dense(self.layer3_neurons, activation=tf.nn.softmax))

        # Train neural network
        optimizer = self.opt
        epochs = int(self.num_epochs)
        model.compile(optimizer=optimizer, loss='sparse_categorical_crossentropy', metrics=['accuracy'])
        history = model.fit(self.x_train, self.y_train, epochs=epochs)

        # Evaluate performance
        val_loss, val_acc = model.evaluate(self.x_test, self.y_test)

        # Send a signal to stop the waitingspinnerwidget
        self.done_model.emit()
        self.display_sig.emit(history)

        # Save model with timestamp
        time1 = time.strftime('%a%H%M%S')
        file_name = str(self.opt) + time1
        model.save(file_name)

        # Display notice with results
        message = "Model saved as: " + str(file_name) + " \n" + "Model.evaluate results: | " + str(
            history.history.keys()) + " | " + str(val_loss) + " | " + str(val_acc) + " | "
        ctypes.windll.user32.MessageBoxW(0, message, "Results", 1)


def main():
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
