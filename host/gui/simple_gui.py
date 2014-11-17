import sys, os, logging
from PyQt4 import QtCore
from PyQt4 import QtGui
from simple_gui_ui import Ui_MainWindow 
from serial_device import SerialDevice

DFLT_PORT = '/dev/tty.usbmodemfd111'
TIMER_INTERVAL_MS = 60000

class SimpleGuiMainWindow(QtGui.QMainWindow,Ui_MainWindow):

    def __init__(self,parent=None):
        super(SimpleGuiMainWindow,self).__init__(parent)
        self.setupUi(self)
        self.setupTimer()
        self.connectActions()
        self.initialize()

    def setupTimer(self):
        """
        Setup timer object
        """
        self.timer = QtCore.QTimer()
        self.timer.setInterval(TIMER_INTERVAL_MS)
        try:
            self.timer.timeout.connect(self.timer_Callback)
        except AttributeError:
            self.connect(self.timer,QtCore.SIGNAL("timeout()"),self.timer_Callback)        

    def connectActions(self):
        self.portLineEdit.editingFinished.connect(self.portChanged_Callback)
        self.connectPushButton.pressed.connect(self.connectPressed_Callback)
        self.connectPushButton.clicked.connect(self.connectClicked_Callback)
        self.measurePushButton.clicked.connect(self.measureClicked_Callback)

    def initialize(self):
        self.port = DFLT_PORT
        self.portLineEdit.setText(self.port) 
        self.setWidgetEnableOnDisconnect()
        self.dev = None
        self.isLogging = False
        self.logPath = '/Users/x1sc0/datalog.txt';
        self.createLogFile()

    def portChanged_Callback(self):
        self.port = str(self.portLineEdit.text())

    def connectPressed_Callback(self):
        if self.dev == None:
            self.connectPushButton.setText('Disconnect')
            self.portLineEdit.setEnabled(False)

    def connectClicked_Callback(self):
        if self.dev == None:
            self.dev = SerialDevice(self.port)
            self.setWidgetEnableOnConnect()
        else:
            self.connectPushButton.setText('Connect')
            self.dev.close()
            self.dev = None
            self.setWidgetEnableOnDisconnect()

    def measureClicked_Callback(self):
        if self.isLogging:
            self.timer.stop()
            self.isLogging = False
            self.pwrTextEdit.setText("")
            self.ldrTextEdit.setText("")
        else:
            self.timer.start()
            self.isLogging = True

    def timer_Callback(self):
        data = self.dev.getMeasurement()
        pwr = str(data[0])
        ldr = str(data[1])
        self.pwrTextEdit.setText(pwr)
        self.ldrTextEdit.setText(ldr)
        self.logger.log(logging.DEBUG,data)

    def createLogFile(self):
        logging.basicConfig(filename=self.logPath,
                            level=logging.DEBUG,
                            format='%(asctime)s %(message)s', 
                            datefmt='%m/%d/%Y %I:%M:%S')

        self.logger = logging.getLogger(__name__)

    def setWidgetEnableOnConnect(self):
        self.pwrTextEdit.setEnabled(True)
        self.ldrTextEdit.setEnabled(True)
        self.measurePushButton.setEnabled(True)
        self.portLineEdit.setEnabled(False)

    def setWidgetEnableOnDisconnect(self):
        self.pwrTextEdit.setEnabled(False)
        self.ldrTextEdit.setEnabled(False)
        self.measurePushButton.setEnabled(False)
        self.portLineEdit.setEnabled(True)

    def main(self):
        self.show()

# -----------------------------------------------------------------------------
if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    mainWindow = SimpleGuiMainWindow()
    mainWindow.main()
    app.exec_()
