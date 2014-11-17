# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'simple_gui.ui'
#
# Created: Mon Nov 17 00:02:27 2014
#      by: PyQt4 UI code generator 4.11.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(725, 370)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.widget_2 = QtGui.QWidget(self.centralwidget)
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.frame = QtGui.QFrame(self.widget_2)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.pwrGroupBox = QtGui.QGroupBox(self.frame)
        self.pwrGroupBox.setObjectName(_fromUtf8("pwrGroupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.pwrGroupBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.pwrTextEdit = QtGui.QTextEdit(self.pwrGroupBox)
        self.pwrTextEdit.setObjectName(_fromUtf8("pwrTextEdit"))
        self.verticalLayout.addWidget(self.pwrTextEdit)
        self.verticalLayout_2.addWidget(self.pwrGroupBox)
        self.horizontalLayout_2.addWidget(self.frame)
        self.frame_2 = QtGui.QFrame(self.widget_2)
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.ldrGroupBox = QtGui.QGroupBox(self.frame_2)
        self.ldrGroupBox.setObjectName(_fromUtf8("ldrGroupBox"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.ldrGroupBox)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.ldrTextEdit = QtGui.QTextEdit(self.ldrGroupBox)
        self.ldrTextEdit.setObjectName(_fromUtf8("ldrTextEdit"))
        self.verticalLayout_3.addWidget(self.ldrTextEdit)
        self.verticalLayout_4.addWidget(self.ldrGroupBox)
        self.horizontalLayout_2.addWidget(self.frame_2)
        self.verticalLayout_5.addWidget(self.widget_2)
        self.widget = QtGui.QWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.portLineEdit = QtGui.QLineEdit(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.portLineEdit.sizePolicy().hasHeightForWidth())
        self.portLineEdit.setSizePolicy(sizePolicy)
        self.portLineEdit.setObjectName(_fromUtf8("portLineEdit"))
        self.horizontalLayout.addWidget(self.portLineEdit)
        self.connectPushButton = QtGui.QPushButton(self.widget)
        self.connectPushButton.setObjectName(_fromUtf8("connectPushButton"))
        self.horizontalLayout.addWidget(self.connectPushButton)
        spacerItem = QtGui.QSpacerItem(322, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.measurePushButton = QtGui.QPushButton(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.measurePushButton.sizePolicy().hasHeightForWidth())
        self.measurePushButton.setSizePolicy(sizePolicy)
        self.measurePushButton.setObjectName(_fromUtf8("measurePushButton"))
        self.horizontalLayout.addWidget(self.measurePushButton)
        self.verticalLayout_5.addWidget(self.widget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 725, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "A.I. Simple Gui", None))
        self.pwrGroupBox.setTitle(_translate("MainWindow", "Battery Power", None))
        self.ldrGroupBox.setTitle(_translate("MainWindow", "Photoresistor", None))
        self.label.setText(_translate("MainWindow", "Port", None))
        self.connectPushButton.setText(_translate("MainWindow", "Connect", None))
        self.measurePushButton.setText(_translate("MainWindow", "Measure", None))

