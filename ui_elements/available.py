# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'available.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_available(object):
    def setupUi(self, available):
        available.setObjectName("available")
        available.resize(800, 480)
        available.setMinimumSize(QtCore.QSize(800, 480))
        available.setMaximumSize(QtCore.QSize(800, 480))
        available.setStyleSheet("QWidget\n"
"{\n"
"    color: rgb(0, 123, 255);    \n"
"    background-color: rgb(0, 0, 0);\n"
"\n"
"}\n"
"\n"
"QWidget:item:selected\n"
"{\n"
"    color: rgb(239, 151, 0);\n"
"    border: 1px solid rgb(239, 151, 0);\n"
"    /*color: rgb(255, 255, 255);    \n"
"    background-color: rgb(0, 123, 255);    */\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"    border: 1px solid  rgb(97, 97, 97);\n"
"    top: 1px;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    background-color: rgb(97, 97, 97);\n"
"    color: rgb(255, 255, 255);\n"
"    border-width: 1px;\n"
"    border-color: rgb(255, 255, 255);\n"
"    border-style: solid;\n"
"    border-top-left-radius: 10px;\n"
"    border-top-right-radius: 10px;\n"
"    padding: 5px;\n"
"    padding-left: 63px;\n"
"    padding-right:63px;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    color: rgb(255, 255, 255);    \n"
"    background-color: rgb(0, 123, 255);\n"
"}\n"
"\n"
".QMessageBox {font-size: 16pt}\n"
"\n"
".QSlider {\n"
"    min-height: 30px;\n"
"    max-height: 50px;\n"
"}\n"
"\n"
".QSlider::groove:horizontal {\n"
"    border: 1px solid;\n"
"    height: 5px;\n"
"    background: #393939;\n"
"    margin: 0 12px;\n"
"}\n"
"\n"
".QSlider::handle:horizontal {\n"
"    background: rgb(0, 123, 255);\n"
"    width: 30px;\n"
"    height: 30px;\n"
"    margin: -24px -12px;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: rgb(97, 97, 97);\n"
"    color: rgb(255, 255, 255);\n"
"    border-width: 1px;\n"
"    border-color: rgb(97, 97, 97);\n"
"    border-style: solid;\n"
"    border-radius: 7;\n"
"    padding: 3px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"}\n"
"\n"
"QPushButton:checked\n"
"{\n"
"    color: rgb(255, 255, 255);    \n"
"    background-color: rgb(0, 123, 255);\n"
"    border-color: rgb(0, 123, 255);\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    color: rgb(255, 255, 255);    \n"
"    background-color: rgb(0, 123, 255);\n"
"    border-color: rgb(0, 123, 255);\n"
"}\n"
"\n"
"QProgressBar\n"
"{\n"
"    background-color: rgb(166, 166, 166);\n"
"    color: rgb(0, 0, 0);\n"
"    border: 2px rgb(166, 166, 166);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    border: 2px rgb(166, 166, 166);\n"
"    border-top-left-radius: 5px;\n"
"    border-bottom-left-radius: 5px;\n"
"    border-top-right-radius: 5px;\n"
"    border-bottom-right-radius: 5px;\n"
"    background-color: rgb(0, 123, 255);\n"
"   /* width: 40px;\n"
"    margin: 0.5px;*/\n"
"}\n"
"\n"
"QComboBox {\n"
"    color: rgb(0, 123, 255);    \n"
"    border: 1px solid  rgb(97, 97, 97);\n"
"    border-top-left-radius: 7px;\n"
"    border-bottom-left-radius: 7px;\n"
"    padding: 1px 18px 1px 5px;\n"
"    min-width: 6em;\n"
"}\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    border: 1px solid  rgb(97, 97, 97);\n"
"    border-top-left-radius: 7px;\n"
"    border-bottom-left-radius: 0px;\n"
"    color: rgb(239, 151, 0);\n"
"}\n"
"\n"
"/* QComboBox:hover\n"
"{\n"
"    color: rgb(239, 151, 0);\n"
"}*/\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    border: 1px solid  rgb(97, 97, 97);\n"
"}\n"
"\n"
"/*QComboBox:item:checked {\n"
"    color: rgb(239, 151, 0);\n"
"    border: 1px solid rgb(239, 151, 0);\n"
"}\n"
"\n"
"QComboBox:item:selected {\n"
"    color: rgb(239, 151, 0);\n"
"    border: 1px solid rgb(239, 151, 0);\n"
"} */\n"
"\n"
"QLineEdit\n"
"{\n"
"    padding: 1px;\n"
"    border-style: solid;\n"
"    border: 1px solid rgb(97, 97, 97);\n"
"    border-radius: 5;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(available)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(330, 0))
        self.label.setMaximumSize(QtCore.QSize(330, 16777215))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setMinimumSize(QtCore.QSize(330, 0))
        self.label_2.setMaximumSize(QtCore.QSize(330, 16777215))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.LWVorhanden = QtWidgets.QListWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.LWVorhanden.setFont(font)
        self.LWVorhanden.setStyleSheet(" QScrollBar:vertical {\n"
"     border: 1px solid rgb(97, 97, 97);\n"
"     background: rgb(0, 0, 0);\n"
"     width: 30px;\n"
"     margin: 31px 0 31px 0;\n"
" }\n"
" QScrollBar::handle:vertical {\n"
"     background: rgb(0, 0, 0);\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: 1px solid rgb(97, 97, 97);\n"
"     background: rgb(0, 0, 0);\n"
"     height: 30px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::sub-line:vertical {\n"
"     border: 1px solid rgb(97, 97, 97);\n"
"     background: rgb(0, 0, 0);\n"
"     height: 30px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"        width: 10px;\n"
"     height: 10px;\n"
"     background: rgb(0, 123, 255);\n"
" }")
        self.LWVorhanden.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.LWVorhanden.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.LWVorhanden.setObjectName("LWVorhanden")
        self.horizontalLayout_2.addWidget(self.LWVorhanden)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.PBAdd = QtWidgets.QPushButton(self.centralwidget)
        self.PBAdd.setMinimumSize(QtCore.QSize(100, 160))
        self.PBAdd.setMaximumSize(QtCore.QSize(200, 200))
        font = QtGui.QFont()
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.PBAdd.setFont(font)
        self.PBAdd.setObjectName("PBAdd")
        self.verticalLayout.addWidget(self.PBAdd)
        self.PBRemove = QtWidgets.QPushButton(self.centralwidget)
        self.PBRemove.setMinimumSize(QtCore.QSize(100, 160))
        self.PBRemove.setMaximumSize(QtCore.QSize(200, 200))
        font = QtGui.QFont()
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.PBRemove.setFont(font)
        self.PBRemove.setObjectName("PBRemove")
        self.verticalLayout.addWidget(self.PBRemove)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.LWAlle = QtWidgets.QListWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.LWAlle.setFont(font)
        self.LWAlle.setStyleSheet(" QScrollBar:vertical {\n"
"     border: 1px solid rgb(97, 97, 97);\n"
"     background: rgb(0, 0, 0);\n"
"     width: 30px;\n"
"     margin: 31px 0 31px 0;\n"
" }\n"
" QScrollBar::handle:vertical {\n"
"     background: rgb(0, 0, 0);\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: 1px solid rgb(97, 97, 97);\n"
"     background: rgb(0, 0, 0);\n"
"     height: 30px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::sub-line:vertical {\n"
"     border: 1px solid rgb(97, 97, 97);\n"
"     background: rgb(0, 0, 0);\n"
"     height: 30px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"        width: 10px;\n"
"     height: 10px;\n"
"     background: rgb(0, 123, 255);\n"
" }")
        self.LWAlle.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.LWAlle.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.LWAlle.setObjectName("LWAlle")
        self.horizontalLayout_2.addWidget(self.LWAlle)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.PBOk_2 = QtWidgets.QPushButton(self.centralwidget)
        self.PBOk_2.setMinimumSize(QtCore.QSize(335, 50))
        self.PBOk_2.setMaximumSize(QtCore.QSize(340, 16777215))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.PBOk_2.setFont(font)
        self.PBOk_2.setObjectName("PBOk_2")
        self.horizontalLayout_4.addWidget(self.PBOk_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.PBAbbruch_2 = QtWidgets.QPushButton(self.centralwidget)
        self.PBAbbruch_2.setMinimumSize(QtCore.QSize(335, 50))
        self.PBAbbruch_2.setMaximumSize(QtCore.QSize(340, 16777215))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.PBAbbruch_2.setFont(font)
        self.PBAbbruch_2.setObjectName("PBAbbruch_2")
        self.horizontalLayout_4.addWidget(self.PBAbbruch_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        available.setCentralWidget(self.centralwidget)

        self.retranslateUi(available)
        QtCore.QMetaObject.connectSlotsByName(available)

    def retranslateUi(self, available):
        _translate = QtCore.QCoreApplication.translate
        available.setWindowTitle(_translate("available", "Verfügbare Zutaten auswählen"))
        self.label.setText(_translate("available", "<html><head/><body><p><span style=\" color:#ef9700;\">Vorhanden</span></p></body></html>"))
        self.label_2.setText(_translate("available", "<html><head/><body><p><span style=\" color:#ef9700;\">Möglich</span></p></body></html>"))
        self.LWVorhanden.setSortingEnabled(True)
        self.PBAdd.setText(_translate("available", "<-"))
        self.PBRemove.setText(_translate("available", "->"))
        self.LWAlle.setSortingEnabled(True)
        self.PBOk_2.setText(_translate("available", "OK"))
        self.PBAbbruch_2.setText(_translate("available", "Abbrechen"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    available = QtWidgets.QMainWindow()
    ui = Ui_available()
    ui.setupUi(available)
    available.show()
    sys.exit(app.exec_())

