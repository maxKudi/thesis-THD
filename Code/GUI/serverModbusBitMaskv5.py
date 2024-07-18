import threading
import serial
import time
import can
import socket
import sys
import logging
import os
import cv2
import pickle
import struct
import numpy as np

from bitarray import *
from pyModbusTCP.server import ModbusServer
from pyModbusTCP.client import ModbusClient

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtGui import QImage, QPixmap
from Controller import *
from LedIndicator import *

class App(QtWidgets.QMainWindow):   
    def __init__(self):
        super(App, self).__init__()
        self.ui = Ui_Controller()
        self.ui.setupUi(self)

        # Variables declaration for the GUI
        self.connectionStatus = False
        self.sStatus = None
        self.falseSignal = False

        #Initialize the LEDs
        self.led_E = LedIndicator(self)
        self.led_E.setDisabled(True)
        self.ui.Light_E.addWidget(self.led_E)
        
        self.led_B = LedIndicator(self)
        self.led_B.setDisabled(True)
        self.ui.Light_B.addWidget(self.led_B)
        
        self.led_MU = LedIndicator(self)
        self.led_MU.setDisabled(True)
        self.ui.Move_Up.addWidget(self.led_MU)
        
        self.led_P = LedIndicator(self)
        self.led_P.setDisabled(True)
        self.ui.Press.addWidget(self.led_P)
        
        self.led_MD = LedIndicator(self)
        self.led_MD.setDisabled(True)
        self.ui.Move_Down.addWidget(self.led_MD)
        
        self.led_MR = LedIndicator(self)
        self.led_MR.setDisabled(True)
        self.ui.Move_Right.addWidget(self.led_MR)
        
        self.led_ML = LedIndicator(self)
        self.led_ML.setDisabled(True)
        self.ui.Move_Left.addWidget(self.led_ML)
        
        self.led_DUL = LedIndicator(self)
        self.led_DUL.setDisabled(True)
        self.ui.Diagonal_UpLeft.addWidget(self.led_DUL)
        
        self.led_DUR = LedIndicator(self)
        self.led_DUR.setDisabled(True)
        self.ui.Diagonal_UpRight.addWidget(self.led_DUR)
        
        self.led_DDL = LedIndicator(self)
        self.led_DDL.setDisabled(True)
        self.ui.Diagonal_DownLeft.addWidget(self.led_DDL)
        
        self.led_DDR = LedIndicator(self)
        self.led_DDR.setDisabled(True)
        self.ui.Diagonal_DownRight.addWidget(self.led_DDR)
        
        self.led_RL = LedIndicator(self)
        self.led_RL.setDisabled(True)
        self.ui.Rotate_Left.addWidget(self.led_RL)
        
        self.led_RR = LedIndicator(self)
        self.led_RR.setDisabled(True)
        self.ui.Rotate_Right.addWidget(self.led_RR)
        
        self.led_A = LedIndicator(self)
        self.led_A.setDisabled(True)
        self.ui.Light_A.addWidget(self.led_A)
        
        self.led_F = LedIndicator(self)
        self.led_F.setDisabled(True)
        self.ui.Light_F.addWidget(self.led_F)
        
        self.led_D = LedIndicator(self)
        self.led_D.setDisabled(True)
        self.ui.Light_D.addWidget(self.led_D)
        
        self.led_C = LedIndicator(self)
        self.led_C.setDisabled(True)
        self.ui.Light_C.addWidget(self.led_C)

        #Initialize LED for motor 
        self.led_BM1 = NewLedIndicator(self)
        self.led_BM1.setDisabled(True)
        self.ui.BM1.addWidget(self.led_BM1)

        self.led_BM2 = NewLedIndicator(self)
        self.led_BM2.setDisabled(True)
        self.ui.BM2.addWidget(self.led_BM2)

        self.led_BM3 = NewLedIndicator(self)
        self.led_BM3.setDisabled(True)
        self.ui.BM3.addWidget(self.led_BM3)

        self.led_BM4 = NewLedIndicator(self)
        self.led_BM4.setDisabled(True)
        self.ui.BM4.addWidget(self.led_BM4)

        self.led_BM5 = NewLedIndicator(self)
        self.led_BM5.setDisabled(True)
        self.ui.BM5.addWidget(self.led_BM5)

        self.led_BM6 = NewLedIndicator(self)
        self.led_BM6.setDisabled(True)
        self.ui.BM6.addWidget(self.led_BM6)

        self.led_BM7 = NewLedIndicator(self)
        self.led_BM7.setDisabled(True)
        self.ui.BM7.addWidget(self.led_BM7)

        self.led_BM8 = NewLedIndicator(self)
        self.led_BM8.setDisabled(True)
        self.ui.BM8.addWidget(self.led_BM8)

        self.led_SM1 = NewLedIndicator(self)
        self.led_SM1.setDisabled(True)
        self.ui.SM1.addWidget(self.led_SM1)

        self.led_SM2 = NewLedIndicator(self)
        self.led_SM2.setDisabled(True)
        self.ui.SM2.addWidget(self.led_SM2)

        self.led_SM3 = NewLedIndicator(self)
        self.led_SM3.setDisabled(True)
        self.ui.SM3.addWidget(self.led_SM3)

        self.led_SM4 = NewLedIndicator(self)
        self.led_SM4.setDisabled(True)
        self.ui.SM4.addWidget(self.led_SM4)

        self.led_AM1 = NewLedIndicator(self)
        self.led_AM1.setDisabled(True)
        self.ui.AM1.addWidget(self.led_AM1)

        self.led_PV1 = NewLedIndicator(self)
        self.led_PV1.setDisabled(True)
        self.ui.PV1.addWidget(self.led_PV1)

        #Initialize LED for sensors
        self.led_DS1 = NewLedIndicator(self)
        self.led_DS1.setDisabled(True)
        self.ui.DS1.addWidget(self.led_DS1)

        self.led_DS2 = NewLedIndicator(self)
        self.led_DS2.setDisabled(True)
        self.ui.DS2.addWidget(self.led_DS2)

        self.led_DS3 = NewLedIndicator(self)
        self.led_DS3.setDisabled(True)
        self.ui.DS3.addWidget(self.led_DS3)

        self.led_DS4 = NewLedIndicator(self)
        self.led_DS4.setDisabled(True)
        self.ui.DS4.addWidget(self.led_DS4)

        self.led_DS5 = NewLedIndicator(self)
        self.led_DS5.setDisabled(True)
        self.ui.DS5.addWidget(self.led_DS5)

        self.led_DS6 = NewLedIndicator(self)
        self.led_DS6.setDisabled(True)
        self.ui.DS6.addWidget(self.led_DS6)

        self.led_DS7 = NewLedIndicator(self)
        self.led_DS7.setDisabled(True)
        self.ui.DS7.addWidget(self.led_DS7)

        self.led_DS8 = NewLedIndicator(self)
        self.led_DS8.setDisabled(True)
        self.ui.DS8.addWidget(self.led_DS8)

        self.led_DS9 = NewLedIndicator(self)
        self.led_DS9.setDisabled(True)
        self.ui.DS9.addWidget(self.led_DS9)

        self.led_DS10 = NewLedIndicator(self)
        self.led_DS10.setDisabled(True)
        self.ui.DS10.addWidget(self.led_DS10)

        self.led_DS11 = NewLedIndicator(self)
        self.led_DS11.setDisabled(True)
        self.ui.DS11.addWidget(self.led_DS11)

        self.led_DS12 = NewLedIndicator(self)
        self.led_DS12.setDisabled(True)
        self.ui.DS12.addWidget(self.led_DS12)

        self.led_AS1 = NewLedIndicator(self)
        self.led_AS1.setDisabled(True)
        self.ui.AS1.addWidget(self.led_AS1)

        self.led_AS2 = NewLedIndicator(self)
        self.led_AS2.setDisabled(True)
        self.ui.AS2.addWidget(self.led_AS2)

        self.led_AS3 = NewLedIndicator(self)
        self.led_AS3.setDisabled(True)
        self.ui.AS3.addWidget(self.led_AS3)

        self.led_AS4 = NewLedIndicator(self)
        self.led_AS4.setDisabled(True)
        self.ui.AS4.addWidget(self.led_AS4)

        self.led_AS5 = NewLedIndicator(self)
        self.led_AS5.setDisabled(True)
        self.ui.AS5.addWidget(self.led_AS5)

        self.led_CAN1 = CANLedIndicator(self)
        self.led_CAN1.setDisabled(True)
        self.ui.CAN1.addWidget(self.led_CAN1)
        

        self.led_CAN2 = CANLedIndicator(self)
        self.led_CAN2.setDisabled(True)
        self.ui.CAN2.addWidget(self.led_CAN2)

        self.led_CAN3 = CANLedIndicator(self)
        self.led_CAN3.setDisabled(True)
        self.ui.CAN3.addWidget(self.led_CAN3)

        self.led_CAN4 = CANLedIndicator(self)
        self.led_CAN4.setDisabled(True)
        self.ui.CAN4.addWidget(self.led_CAN4)

        self.led_CAN5 = CANLedIndicator(self)
        self.led_CAN5.setDisabled(True)
        self.ui.CAN5.addWidget(self.led_CAN5)

        self.led_CAN6 = CANLedIndicator(self)
        self.led_CAN6.setDisabled(True)
        self.ui.CAN6.addWidget(self.led_CAN6)

        self.led_CAN7 = CANLedIndicator(self)
        self.led_CAN7.setDisabled(True)
        self.ui.CAN7.addWidget(self.led_CAN7)

        self.led_CAN8 = CANLedIndicator(self)
        self.led_CAN8.setDisabled(True)
        self.ui.CAN8.addWidget(self.led_CAN8)
        
        # Logging Error in the raspberry pi
        self.logger = logging.getLogger(__name__)
        self.setupLogging()

        # Create a thread for running the can communication and video communication
        self.canThread = CanThread()
        self.cameraThread = CameraThread()

        # Set up the Signal and Slots Connections
        self.ui.actionDisplay.triggered.connect(self.displayPressed)
        self.ui.actionSensors.triggered.connect(self.sensorPressed)
        self.ui.actionCamera.triggered.connect(self.cameraPressed)
        self.ui.actionController.triggered.connect(self.controllerPressed)
        self.ui.actionShutdown.triggered.connect(self.closeApp)
        self.ui.actionSpeed.triggered.connect(self.loadSettings)
        self.ui.actionConnect.triggered.connect(self.loadConnect)
        self.ui.actionAbout.triggered.connect(self.ui.showAbout)
        
        # Connect the signal from the thread to the LED
        self.canThread.ledA_Signal.connect(self.led_A.setChecked)
        self.canThread.ledB_Signal.connect(self.led_B.setChecked)
        self.canThread.ledC_Signal.connect(self.led_C.setChecked)
        self.canThread.ledD_Signal.connect(self.led_D.setChecked)
        self.canThread.ledE_Signal.connect(self.led_E.setChecked)
        self.canThread.ledF_Signal.connect(self.led_F.setChecked)
        self.canThread.ledP_Signal.connect(self.led_P.setChecked)
        self.canThread.ledMU_Signal.connect(self.led_MU.setChecked)
        self.canThread.ledMD_Signal.connect(self.led_MD.setChecked)
        self.canThread.ledMR_Signal.connect(self.led_MR.setChecked)
        self.canThread.ledML_Signal.connect(self.led_ML.setChecked)
        self.canThread.ledDUR_Signal.connect(self.led_DUR.setChecked)
        self.canThread.ledDDR_Signal.connect(self.led_DDR.setChecked)
        self.canThread.ledDUL_Signal.connect(self.led_DUL.setChecked)
        self.canThread.ledDDL_Signal.connect(self.led_DDL.setChecked)
        self.canThread.ledRR_Signal.connect(self.led_RR.setChecked)
        self.canThread.ledRL_Signal.connect(self.led_RL.setChecked)
        self.canThread.speed_Signal.connect(self.ui.speedLCD.display)
        self.canThread.connection_Signal.connect(self.ui.connectionLabel.setText)

        # Connect the signal from the thread to the LED for motors and sensors
        self.canThread.ledBM1_Signal.connect(self.led_BM1.setChecked)
        self.canThread.ledBM2_Signal.connect(self.led_BM2.setChecked)
        self.canThread.ledBM3_Signal.connect(self.led_BM3.setChecked)
        self.canThread.ledBM4_Signal.connect(self.led_BM4.setChecked)
        self.canThread.ledBM5_Signal.connect(self.led_BM5.setChecked)
        self.canThread.ledBM6_Signal.connect(self.led_BM6.setChecked)
        self.canThread.ledBM7_Signal.connect(self.led_BM7.setChecked)
        self.canThread.ledBM8_Signal.connect(self.led_BM8.setChecked)

        self.canThread.ledSM1_Signal.connect(self.led_SM1.setChecked)
        self.canThread.ledSM2_Signal.connect(self.led_SM2.setChecked)
        self.canThread.ledSM3_Signal.connect(self.led_SM3.setChecked)
        self.canThread.ledSM4_Signal.connect(self.led_SM4.setChecked)

        self.canThread.ledAM1_Signal.connect(self.led_AM1.setChecked)
        self.canThread.ledPV1_Signal.connect(self.led_PV1.setChecked)

        self.canThread.ledDS1_Signal.connect(self.led_DS1.setChecked)
        self.canThread.ledDS2_Signal.connect(self.led_DS2.setChecked)
        self.canThread.ledDS3_Signal.connect(self.led_DS3.setChecked)
        self.canThread.ledDS4_Signal.connect(self.led_DS4.setChecked)
        self.canThread.ledDS5_Signal.connect(self.led_DS5.setChecked)
        self.canThread.ledDS6_Signal.connect(self.led_DS6.setChecked)
        self.canThread.ledDS7_Signal.connect(self.led_DS7.setChecked)
        self.canThread.ledDS8_Signal.connect(self.led_DS8.setChecked)
        self.canThread.ledDS9_Signal.connect(self.led_DS9.setChecked)
        self.canThread.ledDS10_Signal.connect(self.led_DS10.setChecked)
        self.canThread.ledDS11_Signal.connect(self.led_DS11.setChecked)
        self.canThread.ledDS12_Signal.connect(self.led_DS12.setChecked)

        self.canThread.ledAS1_Signal.connect(self.led_AS1.setChecked)
        self.canThread.ledAS2_Signal.connect(self.led_AS2.setChecked)
        self.canThread.ledAS3_Signal.connect(self.led_AS3.setChecked)
        self.canThread.ledAS4_Signal.connect(self.led_AS4.setChecked)
        self.canThread.ledAS5_Signal.connect(self.led_AS5.setChecked)

        self.canThread.ledCAN1_Signal.connect(self.led_CAN1.setChecked)
        self.canThread.ledCAN2_Signal.connect(self.led_CAN2.setChecked)
        self.canThread.ledCAN3_Signal.connect(self.led_CAN3.setChecked)
        self.canThread.ledCAN4_Signal.connect(self.led_CAN4.setChecked)
        self.canThread.ledCAN5_Signal.connect(self.led_CAN5.setChecked)
        self.canThread.ledCAN6_Signal.connect(self.led_CAN6.setChecked)
        self.canThread.ledCAN7_Signal.connect(self.led_CAN7.setChecked)
        self.canThread.ledCAN8_Signal.connect(self.led_CAN8.setChecked)



    def displayError(self):
        self.ui.showError()
             
    def closeApp(self):
        print("Closing application")
        reply = QMessageBox()
        reply.setText('Controller v1.0')
        reply.setWindowTitle('Shutdown')
        reply.setIcon(QMessageBox.Question)
        reply.setInformativeText('Are you sure you want to shutdown?')
        reply.setStandardButtons(QMessageBox.Yes|QMessageBox.No)
        reply.setDefaultButton(QMessageBox.No)
        user_choice = reply.exec_()

        if user_choice == QMessageBox.Yes:
            # Execute shutdown action here
            ui.canThread.stop()
            self.close()
            os.system("sudo shutdown -h now")
        else:
            # User chose not to shut down, perform any other desired actions
            pass
               
    def controllerPressed(self):
        self.ui.stackedWidget.setCurrentIndex(0)
        self.cameraThread.disarm()
        
    def displayPressed(self):
        self.ui.stackedWidget.setCurrentIndex(1)
        self.cameraThread.disarm()

    def sensorPressed(self):
        self.ui.stackedWidget.setCurrentIndex(2)
        self.cameraThread.disarm()

    def cameraPressed(self):
        self.ui.stackedWidget.setCurrentIndex(3)
        self.cameraThread.start()
        print("Camera armed.")
        self.cameraThread.frame_signal.connect(self.ui.c1Label.setPixmap)
        self.cameraThread.fixed_frame_signal.connect(self.ui.c2Label.setPixmap)
             
    def loadSettings(self):
        settings = Settings(self.canThread.speedValue)
        settings.setWindowIcon(QIcon('/home/grips/canBus/Icon/speed.png'))
    
        if settings.exec_() == QDialog.Accepted:
            self.canThread.speedValue = settings.sValue    
            settings.horizontalSlider.setValue(self.canThread.speedValue)
            self.canThread.speedValue = settings.sValue 
            
    def loadConnect(self):
        connect = Connection(self.connectionStatus , self.sStatus)
        connect.setWindowIcon(QIcon('/home/grips/canBus/Icon/connect.png'))

        if connect.exec_() == QDialog.Accepted:
            self.connectionStatus = connect.connectionStatus
            self.sStatus = connect.sStatus
            connect.status.setText(QCoreApplication.translate("Connection", self.sStatus , None)) 
            connect.led_Connection.setChecked(self.connectionStatus)

    def setupLogging(self):
            logging.basicConfig(filename='/home/grips/canBus/Log/appLog.txt', level=logging.ERROR,
                                format='%(asctime)s - %(levelname)s - %(message)s')

class Connection(QtWidgets.QDialog, Ui_Connection_Server):
    def __init__(self, connectionStatus, sStatus):
        super(Connection, self).__init__()
        
        self.setupUi(self)
        self.connectionStatus = connectionStatus
        self.sStatus = sStatus
    
        self.led_Connection = LedIndicator(self)
        self.led_Connection.setDisabled(True)
        self.led_Connection.off_color_1 = QColor(255,0,0)
        self.led_Connection.on_color_1 = QColor(0,255,0)
        self.led_Connection.off_color_2 = QColor(255,0,0)
        self.led_Connection.on_color_2 = QColor(0,255,0)
        self.ConnectionLayout.addWidget(self.led_Connection)        
        
        if self.sStatus is not None:
            self.status.setText(QCoreApplication.translate("Connection", self.sStatus , None))

        if self.connectionStatus is not None:
            self.led_Connection.setChecked(self.connectionStatus)
        
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        
        self.connect.clicked.connect(self.serverConnect)
        self.disconnect.clicked.connect(self.serverDisconnect)

    def serverConnect(self):
        ui.canThread.start()
        time.sleep(0.2)
        if ui.canThread.keep_running:
            self.status.setText(QCoreApplication.translate("Connection", u"<html><head/><body><p><span style=\" color:#00aa00;\">Connected</span></p></body></html>", None))    
            self.connectionStatus = True
            self.led_Connection.setChecked(True)
            self.sStatus = "<html><head/><body><p><span style=\" color:#00aa00;\">Connected</span></p></body></html>"
            ui.canThread.speedValue = 25
            ui.canThread.signal = self.sStatus
            ui.canThread.speed_Signal.emit(ui.canThread.speedValue)
            ui.canThread.connection_Signal.emit(ui.canThread.signal)
        else:
            self.status.setText(QCoreApplication.translate("Connection", u"<html><head/><body><p><span style=\" color:#aa0000;\">Disconnected</span></p></body></html>", None))
            self.connectionStatus = False
            self.led_Connection.setChecked(False)
            self.sStatus = "<html><head/><body><p><span style=\" color:#aa0000;\">Disconnected</span></p></body></html>"
            ui.canThread.speedValue = 0
            ui.canThread.signal = self.sStatus
            ui.canThread.speed_Signal.emit(ui.canThread.speedValue)
            ui.canThread.connection_Signal.emit(ui.canThread.signal)
            ui.displayError()
    
    def serverDisconnect(self):
        self.status.setText(QCoreApplication.translate("Connection", u"<html><head/><body><p><span style=\" color:#aa0000;\">Disconnected</span></p></body></html>", None))
        self.connectionStatus = False
        self.led_Connection.setChecked(False)
        self.sStatus = "<html><head/><body><p><span style=\" color:#aa0000;\">Disconnected</span></p></body></html>"
        ui.canThread.speedValue = 0
        ui.canThread.signal = self.sStatus
        ui.canThread.speed_Signal.emit(ui.canThread.speedValue)
        ui.canThread.connection_Signal.emit(ui.canThread.signal)
        ui.canThread.stop()

    def setIP(self):
        self.ipAddress = self.comboBox.currentText()
        self.ipIndex = self.comboBox.findText(self.ipAddress)
        return self.ipAddress

class Settings(QtWidgets.QDialog, Ui_Settings): 
    def __init__(self, sValue):
        super(Settings, self).__init__()
        
        self.setupUi(self)
        self.sValue = sValue
        
        if self.sValue is not None:
            self.horizontalSlider.setValue(self.sValue)
            
        self.buttonBox.accepted.connect(self.acceptValue)
        self.buttonBox.rejected.connect(self.rejectValue)
        self.inButton.clicked.connect(self.increaseSlider)
        self.deButton.clicked.connect(self.decreaseSlider)
           
    def increaseSlider(self):
        self.horizontalSlider.setValue(self.horizontalSlider.value() + 25)
    
    def decreaseSlider(self):
        self.horizontalSlider.setValue(self.horizontalSlider.value() - 25)
        
    def acceptValue(self):
        self.sValue = self.horizontalSlider.value()
        self.accept()

    def rejectValue(self):
        self.reject()
        
    def speedValue(self):
        return self.horizontalSlider.value()

class CanThread(QtCore.QThread):
    """QThread class and signals to be emitted from the running thread."""

    # Signal with current led status
    ledA_Signal = QtCore.pyqtSignal(bool)
    ledB_Signal = QtCore.pyqtSignal(bool)
    ledC_Signal = QtCore.pyqtSignal(bool)
    ledD_Signal = QtCore.pyqtSignal(bool)
    ledE_Signal = QtCore.pyqtSignal(bool)
    ledF_Signal = QtCore.pyqtSignal(bool)
    ledP_Signal = QtCore.pyqtSignal(bool)
    ledMU_Signal = QtCore.pyqtSignal(bool)
    ledMD_Signal = QtCore.pyqtSignal(bool)
    ledMR_Signal = QtCore.pyqtSignal(bool)
    ledML_Signal = QtCore.pyqtSignal(bool)
    ledDUR_Signal = QtCore.pyqtSignal(bool)
    ledDDR_Signal = QtCore.pyqtSignal(bool)
    ledDUL_Signal = QtCore.pyqtSignal(bool)
    ledDDL_Signal = QtCore.pyqtSignal(bool)
    ledRR_Signal = QtCore.pyqtSignal(bool)
    ledRL_Signal = QtCore.pyqtSignal(bool)
    speed_Signal = QtCore.pyqtSignal(int)
    connection_Signal = QtCore.pyqtSignal(str)

    # Signal for motor and sensor Led status
    ledBM1_Signal = QtCore.pyqtSignal(bool)
    ledBM2_Signal = QtCore.pyqtSignal(bool)
    ledBM3_Signal = QtCore.pyqtSignal(bool)
    ledBM4_Signal = QtCore.pyqtSignal(bool)
    ledBM5_Signal = QtCore.pyqtSignal(bool)
    ledBM6_Signal = QtCore.pyqtSignal(bool)
    ledBM7_Signal = QtCore.pyqtSignal(bool)
    ledBM8_Signal = QtCore.pyqtSignal(bool)

    ledSM1_Signal = QtCore.pyqtSignal(bool)
    ledSM2_Signal = QtCore.pyqtSignal(bool)
    ledSM3_Signal = QtCore.pyqtSignal(bool)
    ledSM4_Signal = QtCore.pyqtSignal(bool)

    ledAM1_Signal = QtCore.pyqtSignal(bool)
    ledPV1_Signal = QtCore.pyqtSignal(bool)

    ledDS1_Signal = QtCore.pyqtSignal(bool)
    ledDS2_Signal = QtCore.pyqtSignal(bool)
    ledDS3_Signal = QtCore.pyqtSignal(bool)
    ledDS4_Signal = QtCore.pyqtSignal(bool)
    ledDS5_Signal = QtCore.pyqtSignal(bool)
    ledDS6_Signal = QtCore.pyqtSignal(bool)
    ledDS7_Signal = QtCore.pyqtSignal(bool)
    ledDS8_Signal = QtCore.pyqtSignal(bool)
    ledDS9_Signal = QtCore.pyqtSignal(bool)
    ledDS10_Signal = QtCore.pyqtSignal(bool)
    ledDS11_Signal = QtCore.pyqtSignal(bool)
    ledDS12_Signal = QtCore.pyqtSignal(bool)

    ledAS1_Signal = QtCore.pyqtSignal(bool)
    ledAS2_Signal = QtCore.pyqtSignal(bool)
    ledAS3_Signal = QtCore.pyqtSignal(bool)
    ledAS4_Signal = QtCore.pyqtSignal(bool)
    ledAS5_Signal = QtCore.pyqtSignal(bool)
    ledAS6_Signal = QtCore.pyqtSignal(bool)

    ledCAN1_Signal = QtCore.pyqtSignal(bool)
    ledCAN2_Signal = QtCore.pyqtSignal(bool)
    ledCAN3_Signal = QtCore.pyqtSignal(bool)
    ledCAN4_Signal = QtCore.pyqtSignal(bool)
    ledCAN5_Signal = QtCore.pyqtSignal(bool)
    ledCAN6_Signal = QtCore.pyqtSignal(bool)
    ledCAN7_Signal = QtCore.pyqtSignal(bool)
    ledCAN8_Signal = QtCore.pyqtSignal(bool)

    def __init__(self):
        super().__init__()

        self.modbusdataButton = bytearray([0x00,0x00,0x00])
        self.modbusdata = bitarray(7, 'little')
        self.modbusdata.setall(0) 
        self.speedValue = 25
        self.signal = "<html><head/><body><p><span style=\" color:#aa0000;\">Disconnected</span></p></body></html>"
        

        # "keep_running" controls the while loop in the running thread
        self.keep_running = False

    def stop(self):
        """ Stops the while loop in the running thread """
        self.keep_running = False

    def run(self):
        """Define the process to be run in the thread, emitting signals
        with current values from the simulation. The while loop is stopped gracefully by calling the stop method"""

        # Canbus button message as masks
        maskBtn0 = b'\xff\x00\xf0\x00\x00'
        maskBtn1 = b'\xff\x40\xf0\x00\x00'
        maskBtn2 = b'\xff\x00\xf1\x00\x00'    
        maskBtn3 = b'\xff\x00\xf4\x00\x00'    
        maskBtn4 = b'\xff\x01\xf0\x00\x00'    
        maskBtn5 = b'\xff\x04\xf0\x00\x00'    
        maskBtn6 = b'\xff\x10\xf0\x00\x00'    
        maskBtn7 = b'\xff\x00\xf0\x40\x00'
        maskBtn8 = b'\xff\x00\xf0\x00\x01'    
        maskBtn9 = b'\xff\x00\xf0\x00\x04'    
        maskBtn10 = b'\xff\x00\xf0\x00\x10'    
        maskBtn11 = b'\xff\x00\xf0\x00\x40'    
        maskBtn12 = b'\xff\x00\xf0\x00\x11'    
        maskBtn13 = b'\xff\x00\xf0\x00\x14'    
        maskBtn14 = b'\xff\x00\xf0\x00\x41'    
        maskBtn15 = b'\xff\x00\xf0\x00\x44'    
        maskBtn16 = b'\xff\x00\xf0\x01\x00'
        maskBtn17 = b'\xff\x00\xf0\x21\x00'
             
        try:
            self.TCP_IP = "10.1.3.111"
            self.TCP_PORT = 502

            print("Starting thread")
            bustype1 = 'socketcan'
            channel = 'can0'
            server = ModbusServer(self.TCP_IP, self.TCP_PORT, no_block=True)

            with can.interface.Bus(channel, bustype=bustype1, bitrate=250000) as bus: 
               
                server.start()
                print("Server is online ....")

                # keep_running should be True before starting the while loop
                self.keep_running = True
                
                while self.keep_running:
                    
                    # Emit speed signals
                    self.speed_Signal.emit(self.speedValue)

                    message = bus.recv()
                    #print(message)

                    if (message.arbitration_id == 0x10ff6487):
                        theCanMessage = message.data
                        canMessage = theCanMessage[:5]
                        #print(canMessage)
                            
                        # Bitwise and between the canMessage and masks
                        bitwiseIdle = (int.from_bytes(canMessage,'big') & int.from_bytes(maskBtn0,'big')).to_bytes(max(len(canMessage),len(maskBtn0)), 'big')
                        bitwiseBtn1 = (int.from_bytes(canMessage,'big') & int.from_bytes(maskBtn1,'big')).to_bytes(max(len(canMessage),len(maskBtn1)), 'big')
                        bitwiseBtn2 = (int.from_bytes(canMessage,'big') & int.from_bytes(maskBtn2,'big')).to_bytes(max(len(canMessage),len(maskBtn2)), 'big')
                        bitwiseBtn3 = (int.from_bytes(canMessage,'big') & int.from_bytes(maskBtn3,'big')).to_bytes(max(len(canMessage),len(maskBtn3)), 'big')
                        bitwiseBtn4 = (int.from_bytes(canMessage,'big') & int.from_bytes(maskBtn4,'big')).to_bytes(max(len(canMessage),len(maskBtn4)), 'big')
                        bitwiseBtn5 = (int.from_bytes(canMessage,'big') & int.from_bytes(maskBtn5,'big')).to_bytes(max(len(canMessage),len(maskBtn5)), 'big')
                        bitwiseBtn6 = (int.from_bytes(canMessage,'big') & int.from_bytes(maskBtn6,'big')).to_bytes(max(len(canMessage),len(maskBtn6)), 'big')
                        bitwiseBtn7 = (int.from_bytes(canMessage,'big') & int.from_bytes(maskBtn7,'big')).to_bytes(max(len(canMessage),len(maskBtn7)), 'big')
                        bitwiseBtn8 = (int.from_bytes(canMessage,'big') & int.from_bytes(maskBtn8,'big')).to_bytes(max(len(canMessage),len(maskBtn8)), 'big')
                        bitwiseBtn9 = (int.from_bytes(canMessage,'big') & int.from_bytes(maskBtn9,'big')).to_bytes(max(len(canMessage),len(maskBtn9)), 'big')
                        bitwiseBtn10 = (int.from_bytes(canMessage,'big') & int.from_bytes(maskBtn10,'big')).to_bytes(max(len(canMessage),len(maskBtn10)), 'big')
                        bitwiseBtn11 = (int.from_bytes(canMessage,'big') & int.from_bytes(maskBtn11,'big')).to_bytes(max(len(canMessage),len(maskBtn11)), 'big')                        
                        bitwiseBtn12 = (int.from_bytes(canMessage,'big') & int.from_bytes(maskBtn12,'big')).to_bytes(max(len(canMessage),len(maskBtn12)), 'big')
                        bitwiseBtn13 = (int.from_bytes(canMessage,'big') & int.from_bytes(maskBtn13,'big')).to_bytes(max(len(canMessage),len(maskBtn13)), 'big')
                        bitwiseBtn14 = (int.from_bytes(canMessage,'big') & int.from_bytes(maskBtn14,'big')).to_bytes(max(len(canMessage),len(maskBtn14)), 'big')
                        bitwiseBtn15 = (int.from_bytes(canMessage,'big') & int.from_bytes(maskBtn15,'big')).to_bytes(max(len(canMessage),len(maskBtn15)), 'big')
                        bitwiseBtn16 = (int.from_bytes(canMessage,'big') & int.from_bytes(maskBtn16,'big')).to_bytes(max(len(canMessage),len(maskBtn16)), 'big')
                        bitwiseBtn17 = (int.from_bytes(canMessage,'big') & int.from_bytes(maskBtn17,'big')).to_bytes(max(len(canMessage),len(maskBtn17)), 'big')
                            
                            
                        if (bitwiseIdle == maskBtn0):
                            self.modbusdata.setall(0)
                            self.modbusdataButton[0] = 0x00
                            #self.modbusdataButton[1] = 0x00
                            self.modbusdataButton[2] = self.speedValue
                        else:
                            pass

                            
                        if (bitwiseBtn1 == maskBtn1):
                            self.ledA_Signal.emit(True)
                            self.modbusdata[0] = True
                        #else:
                            #self.ledA_Signal.emit(False)  
                            
                        # Move the second button out from here
                                
                            
                        if (bitwiseBtn3 == maskBtn3):
                            self.ledC_Signal.emit(True)
                            self.modbusdata[2] = True

                            if ((bitwiseBtn16 == maskBtn16) and (bitwiseBtn17 != maskBtn17)):
                                self.ledRR_Signal.emit(True)
                                self.modbusdataButton[1] = self.incrementSpeed()
                                self.modbusdataButton[0] = 0x06
                                time.sleep(0.5)

                            else:
                                self.ledRR_Signal.emit(False)
                                
                            if (bitwiseBtn17 == maskBtn17):
                                self.ledRL_Signal.emit(True)
                                self.modbusdataButton[1] = self.decrementSpeed()
                                self.modbusdataButton[0] = 0x05
                                time.sleep(0.5)

                            else:
                                self.ledRL_Signal.emit(False)
                        else:
                            self.ledC_Signal.emit(False)
                                
                                
                        if (bitwiseBtn4 == maskBtn4):
                            self.ledD_Signal.emit(True)
                            self.modbusdata[3] = True
                            self.ledA_Signal.emit(False)
                        else:
                            self.ledD_Signal.emit(False)
                                
                                
                        if (bitwiseBtn5 == maskBtn5):
                            self.ledE_Signal.emit(True)
                            self.modbusdata[4] = True
                        else:
                            self.ledE_Signal.emit(False)
                                
                    
                        if (bitwiseBtn6 == maskBtn6):
                            self.ledF_Signal.emit(True)
                            self.modbusdata[5] = True
                        else:
                            self.ledF_Signal.emit(False)
                                    
                            
                        if ((bitwiseBtn8 == maskBtn8) and (bitwiseBtn12 != maskBtn12) and (bitwiseBtn14 != maskBtn14)):
                            self.ledMU_Signal.emit(True)
                            self.modbusdataButton[0] = 0x01
                        else:
                            self.ledMU_Signal.emit(False)
                                
                            
                        if ((bitwiseBtn9 == maskBtn9) and (bitwiseBtn13 != maskBtn13) and (bitwiseBtn15 != maskBtn15)):
                            self.ledMD_Signal.emit(True)
                            self.modbusdataButton[0] = 0x02
                        else:
                            self.ledMD_Signal.emit(False)
                                
                            
                        if ((bitwiseBtn10 == maskBtn10) and (bitwiseBtn12 != maskBtn12) and (bitwiseBtn13 != maskBtn13)):
                            self.ledMR_Signal.emit(True)
                            self.modbusdataButton[0] = 0x03
                        else:
                            self.ledMR_Signal.emit(False)
                                
                            
                        if ((bitwiseBtn11 == maskBtn11) and (bitwiseBtn14 != maskBtn14) and (bitwiseBtn15 != maskBtn15)):
                            self.ledML_Signal.emit(True)
                            self.modbusdataButton[0] = 0x04
                        else:   
                            self.ledML_Signal.emit(False)
                                
                            
                        if (bitwiseBtn12 == maskBtn12):
                            self.ledDUR_Signal.emit(True)
                            self.modbusdataButton[0] = 0x07
                        else:
                            self.ledDUR_Signal.emit(False)
                                
                            
                        if (bitwiseBtn13 == maskBtn13):
                            self.ledDDR_Signal.emit(True)
                            self.modbusdataButton[0] = 0x08
                        else:
                            self.ledDDR_Signal.emit(False)
                                
                            
                        if (bitwiseBtn14 == maskBtn14):
                            self.ledDUL_Signal.emit(True)
                            self.modbusdataButton[0] = 0x09
                        else:
                            self.ledDUL_Signal.emit(False)
                                
                            
                        if (bitwiseBtn15 == maskBtn15):
                            self.ledDDL_Signal.emit(True)
                            self.modbusdataButton[0] = 0x0A
                        else:
                            self.ledDDL_Signal.emit(False)

                        # Second button (Hold button for extra functionality) 
                        if (bitwiseBtn2 == maskBtn2):
                            self.ledB_Signal.emit(True)
                            self.modbusdata[1] = True

                            if ((bitwiseBtn8 == maskBtn8) and (bitwiseBtn12 != maskBtn12) and (bitwiseBtn14 != maskBtn14)):
                                self.ledMU_Signal.emit(True)
                                self.modbusdataButton[0] = 0x0D
                            else:
                                self.ledMU_Signal.emit(False)
                                    
                                
                            if ((bitwiseBtn9 == maskBtn9) and (bitwiseBtn13 != maskBtn13) and (bitwiseBtn15 != maskBtn15)):
                                self.ledMD_Signal.emit(True)
                                self.modbusdataButton[0] = 0x0E
                            else:
                                self.ledMD_Signal.emit(False)
                                    
                                
                            if ((bitwiseBtn10 == maskBtn10) and (bitwiseBtn12 != maskBtn12) and (bitwiseBtn13 != maskBtn13)):
                                self.ledMR_Signal.emit(True)
                                self.modbusdataButton[0] = 0x0B
                            else:
                                self.ledMR_Signal.emit(False)
                                    
                                
                            if ((bitwiseBtn11 == maskBtn11) and (bitwiseBtn14 != maskBtn14) and (bitwiseBtn15 != maskBtn15)):
                                self.ledML_Signal.emit(True)
                                self.modbusdataButton[0] = 0x0C
                            else:   
                                self.ledML_Signal.emit(False)
                                    
                        else:
                            self.ledB_Signal.emit(False)
                        
                        # Third Button (Hold button for extra functionality)                         
                        if (bitwiseBtn7 == maskBtn7):
                            self.ledP_Signal.emit(True)
                            self.modbusdata[6] = True
                            
                            if ((bitwiseBtn8 == maskBtn8) and (bitwiseBtn12 != maskBtn12) and (bitwiseBtn14 != maskBtn14)):
                                self.ledMU_Signal.emit(True)
                                self.modbusdataButton[0] = 0x0F
                            else:
                                self.ledMU_Signal.emit(False)
                                    
                                
                            if ((bitwiseBtn9 == maskBtn9) and (bitwiseBtn13 != maskBtn13) and (bitwiseBtn15 != maskBtn15)):
                                self.ledMD_Signal.emit(True)
                                self.modbusdataButton[0] = 0x10
                            else:
                                self.ledMD_Signal.emit(False)
                            
                        else:
                            self.ledP_Signal.emit(False)
                            
                        server.data_bank.set_holding_registers(0, [int.from_bytes(self.modbusdata.tobytes(),'little')])                 
                        server.data_bank.set_holding_registers(1, self.modbusdataButton) 

			# Life check code
                        HeartIN = server.data_bank.get_coils(1,1)
                        if (HeartIN == True):
                            server.data_bank.set_coils(0, [True])
                        else:
                            server.data_bank.set_coils(0,[False])
                        
            # Scada Inputs
                        motorData = server.data_bank.get_holding_registers(10, 1)
                        digitalSensorsData = server.data_bank.get_holding_registers(11, 1)
                        analogSensorsData = server.data_bank.get_holding_registers(12, 1)
                        canBusData = server.data_bank.get_holding_registers(13, 1)

                        motorData = self.decode_booleans(motorData[0], 15)
                        digitalSensorsData = self.decode_booleans(digitalSensorsData[0], 15)
                        analogSensorsData = self.decode_booleans(analogSensorsData[0], 8)
                        canBusData = self.decode_booleans(canBusData[0], 8)

                        if(motorData[0] == True):
                            self.ledBM1_Signal.emit(True)
                        else:
                            self.ledBM1_Signal.emit(False)

                        if(motorData[1] == True):
                            self.ledBM2_Signal.emit(True)
                        else:
                            self.ledBM2_Signal.emit(False)

                        if(motorData[2] == True):
                            self.ledBM3_Signal.emit(True)
                        else:
                            self.ledBM3_Signal.emit(False)

                        if(motorData[3] == True):
                            self.ledBM4_Signal.emit(True)
                        else:
                            self.ledBM4_Signal.emit(False)

                        if(motorData[4] == True):
                            self.ledBM5_Signal.emit(True)
                        else:
                            self.ledBM5_Signal.emit(False)

                        if(motorData[5] == True):
                            self.ledBM6_Signal.emit(True)
                        else:
                            self.ledBM6_Signal.emit(False)

                        if(motorData[6] == True):
                            self.ledBM7_Signal.emit(True)
                        else:
                            self.ledBM7_Signal.emit(False)

                        if(motorData[7] == True):
                            self.ledBM8_Signal.emit(True)
                        else:
                            self.ledBM8_Signal.emit(False)
                        
                        if(motorData[8] == True):
                            self.ledSM1_Signal.emit(True)
                        else:
                            self.ledSM1_Signal.emit(False)

                        if(motorData[9] == True):
                            self.ledSM2_Signal.emit(True)
                        else:
                            self.ledSM2_Signal.emit(False)

                        if(motorData[10] == True):
                            self.ledSM3_Signal.emit(True)
                        else:
                            self.ledSM3_Signal.emit(False)

                        if(motorData[11] == True):
                            self.ledSM4_Signal.emit(True)
                        else:
                            self.ledSM4_Signal.emit(False)

                        if(motorData[12] == True):
                            self.ledAM1_Signal.emit(True)
                        else:
                            self.ledAM1_Signal.emit(False)

                        if(motorData[13] == True):
                            self.ledPV1_Signal.emit(True)
                        else:
                            self.ledPV1_Signal.emit(False)


                        if(digitalSensorsData[0] == True):
                            self.ledDS1_Signal.emit(True)
                        else:
                            self.ledDS1_Signal.emit(False)

                        if(digitalSensorsData[1] == True):
                            self.ledDS2_Signal.emit(True)
                        else:
                            self.ledDS2_Signal.emit(False)

                        if(digitalSensorsData[2] == True):
                            self.ledDS3_Signal.emit(True)
                        else:
                            self.ledDS3_Signal.emit(False)

                        if(digitalSensorsData[3] == True):
                            self.ledDS4_Signal.emit(True)
                        else:
                            self.ledDS4_Signal.emit(False)

                        if(digitalSensorsData[4] == True):
                            self.ledDS5_Signal.emit(True)
                        else:
                            self.ledDS5_Signal.emit(False)

                        if(digitalSensorsData[5] == True):
                            self.ledDS6_Signal.emit(True)
                        else:
                            self.ledDS6_Signal.emit(False)

                        if(digitalSensorsData[6] == True):
                            self.ledDS7_Signal.emit(True)
                        else:
                            self.ledDS7_Signal.emit(False)

                        if(digitalSensorsData[7] == True):
                            self.ledDS8_Signal.emit(True)
                        else:
                            self.ledDS8_Signal.emit(False)

                        if(digitalSensorsData[8] == True):
                            self.ledDS9_Signal.emit(True)
                        else:
                            self.ledDS9_Signal.emit(False)

                        if(digitalSensorsData[9] == True):
                            self.ledDS10_Signal.emit(True)
                        else:
                            self.ledDS10_Signal.emit(False)

                        if(digitalSensorsData[10] == True):
                            self.ledDS11_Signal.emit(True)
                        else:
                            self.ledDS11_Signal.emit(False)

                        if(digitalSensorsData[11] == True):
                            self.ledDS12_Signal.emit(True)
                        else:
                            self.ledDS12_Signal.emit(False)


                        if(analogSensorsData[0] == True):
                            self.ledAS1_Signal.emit(True)
                        else:
                            self.ledAS1_Signal.emit(False)

                        if(analogSensorsData[1] == True):
                            self.ledAS2_Signal.emit(True)
                        else:
                            self.ledAS2_Signal.emit(False)

                        if(analogSensorsData[2] == True):
                            self.ledAS3_Signal.emit(True)
                        else:
                            self.ledAS3_Signal.emit(False)

                        if(analogSensorsData[3] == True):
                            self.ledAS4_Signal.emit(True)
                        else:
                            self.ledAS4_Signal.emit(False)

                        if(analogSensorsData[4] == True): 
                            self.ledAS5_Signal.emit(True)
                        else:
                            self.ledAS5_Signal.emit(False)

                        if(analogSensorsData[5] == True):
                            self.ledAS6_Signal.emit(True)
                        else:
                            self.ledAS6_Signal.emit(False)

                        if(canBusData[0] == True):
                            self.ledCAN1_Signal.emit(True)
                        else:
                            self.ledCAN1_Signal.emit(False)

                        if(canBusData[1] == True):
                            self.ledCAN2_Signal.emit(True)
                        else:
                            self.ledCAN2_Signal.emit(False)

                        if(canBusData[2] == True):
                            self.ledCAN3_Signal.emit(True)
                        else:
                            self.ledCAN3_Signal.emit(False)

                        if(canBusData[3] == True):
                            self.ledCAN4_Signal.emit(True)
                        else:
                            self.ledCAN4_Signal.emit(False)

                        if(canBusData[4] == True):
                            self.ledCAN5_Signal.emit(True)
                        else:
                            self.ledCAN5_Signal.emit(False)

                        if(canBusData[5] == True):
                            self.ledCAN6_Signal.emit(True)
                        else:
                            self.ledCAN6_Signal.emit(False)

                        if(canBusData[6] == True):
                            self.ledCAN7_Signal.emit(True)
                        else:
                            self.ledCAN7_Signal.emit(False)
                        
                        if(canBusData[7] == True):
                            self.ledCAN8_Signal.emit(True)
                        else:
                            self.ledCAN8_Signal.emit(False)

        # Exception handling to catch and print out any exceptions that may occur in the running thread
        except Exception as e:
            (type, value, traceback) = sys.exc_info()
            sys.excepthook(type, value, traceback)
            ui.logger.error("An error occurred: %s", str(e))
            print("Couldn't start the Server")

        finally:
            # Stop the Server when the thread is not running
            if (self.keep_running == False):
                print("Server is offline ....")

                self.falseSignal = False

                # Signal with current led status - Set all to false when the connection is off

                self.ledA_Signal.emit(self.falseSignal)
                self.ledB_Signal.emit(self.falseSignal)
                self.ledC_Signal.emit(self.falseSignal)
                self.ledD_Signal.emit(self.falseSignal)
                self.ledE_Signal.emit(self.falseSignal)
                self.ledF_Signal.emit(self.falseSignal)
                self.ledP_Signal.emit(self.falseSignal)
                self.ledMU_Signal.emit(self.falseSignal)
                self.ledMD_Signal.emit(self.falseSignal)
                self.ledMR_Signal.emit(self.falseSignal)
                self.ledML_Signal.emit(self.falseSignal)
                self.ledDUR_Signal.emit(self.falseSignal)
                self.ledDDR_Signal.emit(self.falseSignal)
                self.ledDUL_Signal.emit(self.falseSignal)
                self.ledDDL_Signal.emit(self.falseSignal)
                self.ledRR_Signal.emit(self.falseSignal)
                self.ledRL_Signal.emit(self.falseSignal)


                # Signal for motor and sensor Led status
                self.ledBM1_Signal.emit(self.falseSignal)
                self.ledBM2_Signal.emit(self.falseSignal)
                self.ledBM3_Signal.emit(self.falseSignal)
                self.ledBM4_Signal.emit(self.falseSignal)
                self.ledBM5_Signal.emit(self.falseSignal)
                self.ledBM6_Signal.emit(self.falseSignal)
                self.ledBM7_Signal.emit(self.falseSignal)
                self.ledBM8_Signal.emit(self.falseSignal)

                self.ledSM1_Signal.emit(self.falseSignal)
                self.ledSM2_Signal.emit(self.falseSignal)
                self.ledSM3_Signal.emit(self.falseSignal)
                self.ledSM4_Signal.emit(self.falseSignal)

                self.ledAM1_Signal.emit(self.falseSignal)
                self.ledPV1_Signal.emit(self.falseSignal)

                self.ledDS1_Signal.emit(self.falseSignal)
                self.ledDS2_Signal.emit(self.falseSignal)
                self.ledDS3_Signal.emit(self.falseSignal)
                self.ledDS4_Signal.emit(self.falseSignal)
                self.ledDS5_Signal.emit(self.falseSignal)
                self.ledDS6_Signal.emit(self.falseSignal)
                self.ledDS7_Signal.emit(self.falseSignal)
                self.ledDS8_Signal.emit(self.falseSignal)
                self.ledDS9_Signal.emit(self.falseSignal)
                self.ledDS10_Signal.emit(self.falseSignal)
                self.ledDS11_Signal.emit(self.falseSignal)
                self.ledDS12_Signal.emit(self.falseSignal)

                self.ledAS1_Signal.emit(self.falseSignal)
                self.ledAS2_Signal.emit(self.falseSignal)
                self.ledAS3_Signal.emit(self.falseSignal)
                self.ledAS4_Signal.emit(self.falseSignal)
                self.ledAS5_Signal.emit(self.falseSignal)
                self.ledAS6_Signal.emit(self.falseSignal)

                self.ledCAN1_Signal.emit(self.falseSignal)
                self.ledCAN2_Signal.emit(self.falseSignal)
                self.ledCAN3_Signal.emit(self.falseSignal)
                self.ledCAN4_Signal.emit(self.falseSignal)
                self.ledCAN5_Signal.emit(self.falseSignal)
                self.ledCAN6_Signal.emit(self.falseSignal)
                self.ledCAN7_Signal.emit(self.falseSignal)
                self.ledCAN8_Signal.emit(self.falseSignal)

                server.stop()

    def incrementSpeed(self):
        if self.speedValue < 100:
            self.speedValue += 25
        return self.speedValue
            
    def decrementSpeed(self):
        if self.speedValue > 0:
            self.speedValue -= 25
        return self.speedValue
    
    def decode_booleans(self, intval, bits):
        res = []
        for bit in range(bits):
            mask = 1 << bit
            res.append((intval & mask) == mask)
        return res

class CameraThread(QtCore.QThread):

    # Signal with the images 
    frame_signal = QtCore.pyqtSignal(QPixmap)
    fixed_frame_signal = QtCore.pyqtSignal(QPixmap)

    def __init__(self):
        super().__init__()

        self.armed = False
        self.display_width = 720
        self.display_height = 320

    def disarm(self):
        self.armed = False
        print("Camera disarmed.")

    def run(self):

            try:
                IP = '192.168.1.150'
                PORT = 8000

                self.armed = True

                # Set the no access camera frame
                self.fixed_pixmap = QtGui.QPixmap("/home/grips/canBus/Icon/NoAcess")
                self.fixed_pixmap  = self.fixed_pixmap .scaled(self.display_width, self.display_height, Qt.IgnoreAspectRatio)
                self.fixed_frame_signal.emit(self.fixed_pixmap)
                self.frame_signal.emit(self.fixed_pixmap)

                # Connect to the server
                client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                client_socket.connect((IP, PORT))

                while self.armed:

                    # Receive the frame size (8 bytes for 'L' Unsigned Long format)
                    msg_size = client_socket.recv(8)
                    if not msg_size:
                        break
                    
                    # Unpack the message size 'Q' (Unsigned Long Long) - 8 bytes
                    msg_size = struct.unpack("Q", msg_size)[0]  

                    # Receive the frame data
                    data = b''
                    while len(data) < msg_size:
                        packet = client_socket.recv(msg_size - len(data))
                        if not packet:
                            break
                        data += packet

                    # Unpickle the frame and display it
                    frame = pickle.loads(data)
                    self.display_frame(frame)

            except Exception  as e:
                ui.logger.error("An error occurred: %s", str(e))
                print("Couldn't start the Server")

            finally:
                self.fixed_pixmap = QtGui.QPixmap("/home/grips/canBus/Icon/NoAcess")
                self.fixed_pixmap  = self.fixed_pixmap .scaled(self.display_width, self.display_height, Qt.IgnoreAspectRatio)
                self.fixed_frame_signal.emit(self.fixed_pixmap)
                self.frame_signal.emit(self.fixed_pixmap)
                
                cv2.destroyAllWindows()
                client_socket.close()

    def display_frame(self, frame):
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        height, width, channel = rgb_frame.shape
        bytes_per_line = channel * width
        qt_format = QtGui.QImage(rgb_frame.data, width, height, bytes_per_line, QtGui.QImage.Format_RGB888)
        pixmap = qt_format.scaled(self.display_width, self.display_height, Qt.IgnoreAspectRatio)
        pixmap = QPixmap.fromImage(pixmap)

        # Emit the signal with the QPixmap
        self.frame_signal.emit(pixmap)
        

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ui = App()
    ui.setWindowTitle("Controller")
    ui.setWindowIcon(QIcon('/home/grips/canBus/Icon/controller.png'))
    ui.showMaximized()
    sys.exit(app.exec_())

        
