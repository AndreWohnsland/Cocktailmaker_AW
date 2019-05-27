import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import *

from loggerconfig import logfunction, logerror


@logerror
def standartbox(textstring):
    """ The default messagebox for the Maker. Uses a QMessageBox with OK-Button """
    # print(textstring)
    msgBox = QMessageBox()
    msgBox.setStandardButtons(QMessageBox.Ok)
    buttonok = msgBox.button(QMessageBox.Ok)
    buttonok.setText("     OK     ")
    fillstring = "-" * 70
    msgBox.setText("{0}\n{1}\n{0}".format(fillstring, textstring))
    msgBox.setStyleSheet(
        "QMessageBox QPushButton{background-color: rgb(0, 123, 255); color: rgb(0, 0, 0); font-size: 30pt;} QMessageBox{background-color: rgb(10, 10, 10); font-size: 16pt;} QMessageBox QLabel{color: rgb(0, 123, 255);}")
    msgBox.showFullScreen()
    msgBox.exec_()
