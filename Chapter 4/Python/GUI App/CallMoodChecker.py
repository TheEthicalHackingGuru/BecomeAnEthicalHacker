from MoodChecker import *
import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QMessageBox, QPlainTextEdit


class NewMoodCheckerForm(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(NewMoodCheckerForm, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.buttonBox.clicked.connect(self.CheckMoodUponClick)
        self.show()

    def CheckMoodUponClick(self):
        if self.ui.lineEdit.text() == "sad":
            QtWidgets.QMessageBox.information(self, 'answered sad','you answered %s! cheer up mate!' % self.ui.lineEdit.text())
        elif self.ui.lineEdit.text() == "happy":
            QtWidgets.QMessageBox.information(self, 'answered happy','you answered %s! cheers mate!' % self.ui.lineEdit.text())
        else:
            QtWidgets.QMessageBox.information(self, 'unknown answer','you answered something like %s! anyway cheers mate!' %self.ui.lineEdit.text())



if __name__ == '__main__':


   app = QtWidgets.QApplication(sys.argv)
   window = NewMoodCheckerForm()
   window.show()
   sys.exit(app.exec_())
