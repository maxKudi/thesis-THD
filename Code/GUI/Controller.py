# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DisplayBylFEF.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QImage
from PyQt5.QtWidgets import QMessageBox
from Settings import Ui_Dialog

class Ui_Controller(object):

    def setupUi(self, Controller):
        if not Controller.objectName():
            Controller.setObjectName(u"Controller")
        Controller.resize(800, 430)
        Controller.setWindowFlag (QtCore.Qt.WindowStaysOnTopHint, False)
        Controller.setWindowFlags(Qt.CustomizeWindowHint)
        Controller.setToolButtonStyle(Qt.ToolButtonIconOnly)
        Controller.setAnimated(True)
        sfont = QFont()
        sfont.setPointSize(14)
        self.actionController = QAction(QIcon('/home/grips/canBus/Icon/controller.png'), "actionController", Controller)
        self.actionController.setObjectName(u"actionController")
        self.actionController.setCheckable(False)
        self.actionController.setFont(sfont)
        self.actionCamera = QAction(QIcon('/home/grips/canBus/Icon/camera.png'), "actionCamera", Controller)
        self.actionCamera.setObjectName(u"actionCamera")
        self.actionCamera.setFont(sfont)
        self.actionDisplay = QAction(QIcon('/home/grips/canBus/Icon/display.png'), "actionDisplay", Controller)
        self.actionDisplay.setObjectName(u"actionDisplay")
        self.actionDisplay.setFont(sfont)
        self.actionSensors = QAction(QIcon('/home/grips/canBus/Icon/sensor.png'), "actionSensors", Controller)
        self.actionSensors.setObjectName(u"actionSensors")
        self.actionSensors.setFont(sfont)
        self.actionSpeed = QAction(QIcon('/home/grips/canBus/Icon/speed.png'), "actionSpeed", Controller)
        self.actionSpeed.setObjectName(u"actionSpeed")
        self.actionSpeed.setFont(sfont)
        self.actionConnect = QAction(QIcon('/home/grips/canBus/Icon/connect.png'),"actionConnect", Controller)
        self.actionConnect.setObjectName(u"actionConnect")
        self.actionConnect.setFont(sfont)
        self.actionAbout = QAction(QIcon('/home/grips/canBus/Icon/about.png'),"actionAbout", Controller)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionAbout.setFont(sfont)
        self.actionShutdown = QAction(QIcon('/home/grips/canBus/Icon/shutdown.png'), "actionShutdown", Controller)
        self.actionShutdown.setObjectName(u"actionShutdown")
        self.actionShutdown.setFont(sfont)
        self.centralwidget = QWidget(Controller)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.stackedWidget = QStackedWidget(self.frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.graphicsView_2 = QGraphicsView(self.page_1)
        self.graphicsView_2.setObjectName(u"graphicsView_2")
        self.graphicsView_2.setGeometry(QRect(600, 30, 158, 76))
        self.graphicsView_2.setStyleSheet(u"QFrame{\n"
"border-radius: 5px;\n"
"background-color: rgb(211, 211, 211);\n"
"}")
        self.graphicsView_4 = QGraphicsView(self.page_1)
        self.graphicsView_4.setObjectName(u"graphicsView_4")
        self.graphicsView_4.setGeometry(QRect(10, 250, 158, 76))
        self.graphicsView_4.setStyleSheet(u"QFrame{\n"
"border-radius: 5px;\n"
"background-color: rgb(211, 211, 211);\n"
"}")
        self.ControllerKnob_3 = QFrame(self.page_1)
        self.ControllerKnob_3.setObjectName(u"ControllerKnob_3")
        self.ControllerKnob_3.setGeometry(QRect(270, 60, 241, 241))
        self.ControllerKnob_3.setStyleSheet(u"QFrame{\n"
"border-radius: 120px;\n"
"background-color: rgb(211, 211, 211);\n"
"}")
        self.ControllerKnob_3.setFrameShape(QFrame.NoFrame)
        self.ControllerKnob_3.setFrameShadow(QFrame.Raised)
        self.ControllerKnob = QFrame(self.ControllerKnob_3)
        self.ControllerKnob.setObjectName(u"ControllerKnob")
        self.ControllerKnob.setGeometry(QRect(10, 10, 221, 221))
        self.ControllerKnob.setStyleSheet(u"QFrame{\n"
"\n"
"border-radius: 110px;\n"
"background-color: rgb(200, 200, 200);\n"
"}")
        self.ControllerKnob.setFrameShape(QFrame.NoFrame)
        self.ControllerKnob.setFrameShadow(QFrame.Raised)
        self.verticalLayoutWidget_7 = QWidget(self.ControllerKnob)
        self.verticalLayoutWidget_7.setObjectName(u"verticalLayoutWidget_7")
        self.verticalLayoutWidget_7.setGeometry(QRect(100, 10, 30, 30))
        self.Move_Up = QVBoxLayout(self.verticalLayoutWidget_7)
        self.Move_Up.setObjectName(u"Move_Up")
        self.Move_Up.setContentsMargins(0, 0, 0, 0)
        self.Move_Up1 = QWidget(self.verticalLayoutWidget_7)
        self.Move_Up1.setObjectName(u"Move_Up1")
        self.Move_Up1.setStyleSheet(u"QFrame{\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 0, 0);\n"
"}")

        self.Move_Up.addWidget(self.Move_Up1)

        self.verticalLayoutWidget_8 = QWidget(self.ControllerKnob)
        self.verticalLayoutWidget_8.setObjectName(u"verticalLayoutWidget_8")
        self.verticalLayoutWidget_8.setGeometry(QRect(100, 100, 30, 30))
        self.Press = QVBoxLayout(self.verticalLayoutWidget_8)
        self.Press.setObjectName(u"Press")
        self.Press.setContentsMargins(0, 0, 0, 0)
        self.Press1 = QWidget(self.verticalLayoutWidget_8)
        self.Press1.setObjectName(u"Press1")
        self.Press1.setStyleSheet(u"QFrame{\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 0, 0);\n"
"}")

        self.Press.addWidget(self.Press1)

        self.verticalLayoutWidget_9 = QWidget(self.ControllerKnob)
        self.verticalLayoutWidget_9.setObjectName(u"verticalLayoutWidget_9")
        self.verticalLayoutWidget_9.setGeometry(QRect(100, 180, 30, 30))
        self.Move_Down = QVBoxLayout(self.verticalLayoutWidget_9)
        self.Move_Down.setObjectName(u"Move_Down")
        self.Move_Down.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.Move_Down.setContentsMargins(0, 0, 0, 0)
        self.Move_Down1 = QWidget(self.verticalLayoutWidget_9)
        self.Move_Down1.setObjectName(u"Move_Down1")
        self.Move_Down1.setStyleSheet(u"QFrame{\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 0, 0);\n"
"}")

        self.Move_Down.addWidget(self.Move_Down1)

        self.verticalLayoutWidget_10 = QWidget(self.ControllerKnob)
        self.verticalLayoutWidget_10.setObjectName(u"verticalLayoutWidget_10")
        self.verticalLayoutWidget_10.setGeometry(QRect(10, 100, 30, 30))
        self.Move_Left = QVBoxLayout(self.verticalLayoutWidget_10)
        self.Move_Left.setObjectName(u"Move_Left")
        self.Move_Left.setContentsMargins(0, 0, 0, 0)
        self.Move_Left1 = QWidget(self.verticalLayoutWidget_10)
        self.Move_Left1.setObjectName(u"Move_Left1")
        self.Move_Left1.setStyleSheet(u"QFrame{\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 0, 0);\n"
"}")

        self.Move_Left.addWidget(self.Move_Left1)

        self.verticalLayoutWidget_11 = QWidget(self.ControllerKnob)
        self.verticalLayoutWidget_11.setObjectName(u"verticalLayoutWidget_11")
        self.verticalLayoutWidget_11.setGeometry(QRect(180, 100, 30, 30))
        self.Move_Right = QVBoxLayout(self.verticalLayoutWidget_11)
        self.Move_Right.setObjectName(u"Move_Right")
        self.Move_Right.setContentsMargins(0, 0, 0, 0)
        self.Move_Right1 = QWidget(self.verticalLayoutWidget_11)
        self.Move_Right1.setObjectName(u"Move_Right1")
        self.Move_Right1.setStyleSheet(u"QFrame{\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 0, 0);\n"
"}")

        self.Move_Right.addWidget(self.Move_Right1)

        self.verticalLayoutWidget_13 = QWidget(self.ControllerKnob)
        self.verticalLayoutWidget_13.setObjectName(u"verticalLayoutWidget_13")
        self.verticalLayoutWidget_13.setGeometry(QRect(190, -5, 30, 30))
        self.Rotate_Right = QVBoxLayout(self.verticalLayoutWidget_13)
        self.Rotate_Right.setObjectName(u"Rotate_Right")
        self.Rotate_Right.setContentsMargins(0, 0, 0, 0)
        self.Rotate_Right1 = QWidget(self.verticalLayoutWidget_13)
        self.Rotate_Right1.setObjectName(u"Rotate_Right1")
        self.Rotate_Right1.setStyleSheet(u"QFrame{\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 0, 0);\n"
"}")

        self.Rotate_Right.addWidget(self.Rotate_Right1)

        self.verticalLayoutWidget_14 = QWidget(self.ControllerKnob)
        self.verticalLayoutWidget_14.setObjectName(u"verticalLayoutWidget_14")
        self.verticalLayoutWidget_14.setGeometry(QRect(30, 40, 30, 30))
        self.Diagonal_UpLeft = QVBoxLayout(self.verticalLayoutWidget_14)
        self.Diagonal_UpLeft.setObjectName(u"Diagonal_UpLeft")
        self.Diagonal_UpLeft.setContentsMargins(0, 0, 0, 0)
        self.Diagonal_UpLeft1 = QWidget(self.verticalLayoutWidget_14)
        self.Diagonal_UpLeft1.setObjectName(u"Diagonal_UpLeft1")
        self.Diagonal_UpLeft1.setStyleSheet(u"QFrame{\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 0, 0);\n"
"}")

        self.Diagonal_UpLeft.addWidget(self.Diagonal_UpLeft1)

        self.verticalLayoutWidget_15 = QWidget(self.ControllerKnob)
        self.verticalLayoutWidget_15.setObjectName(u"verticalLayoutWidget_15")
        self.verticalLayoutWidget_15.setGeometry(QRect(170, 40, 30, 30))
        self.Diagonal_UpRight = QVBoxLayout(self.verticalLayoutWidget_15)
        self.Diagonal_UpRight.setObjectName(u"Diagonal_UpRight")
        self.Diagonal_UpRight.setContentsMargins(0, 0, 0, 0)
        self.Diagonal_UpRight1 = QWidget(self.verticalLayoutWidget_15)
        self.Diagonal_UpRight1.setObjectName(u"Diagonal_UpRight1")
        self.Diagonal_UpRight1.setStyleSheet(u"QFrame{\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 0, 0);\n"
"}")

        self.Diagonal_UpRight.addWidget(self.Diagonal_UpRight1)

        self.verticalLayoutWidget_16 = QWidget(self.ControllerKnob)
        self.verticalLayoutWidget_16.setObjectName(u"verticalLayoutWidget_16")
        self.verticalLayoutWidget_16.setGeometry(QRect(39, 161, 30, 30))
        self.Diagonal_DownLeft = QVBoxLayout(self.verticalLayoutWidget_16)
        self.Diagonal_DownLeft.setObjectName(u"Diagonal_DownLeft")
        self.Diagonal_DownLeft.setContentsMargins(0, 0, 0, 0)
        self.Diagonal_DownLeft1 = QWidget(self.verticalLayoutWidget_16)
        self.Diagonal_DownLeft1.setObjectName(u"Diagonal_DownLeft1")
        self.Diagonal_DownLeft1.setStyleSheet(u"QFrame{\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 0, 0);\n"
"}")

        self.Diagonal_DownLeft.addWidget(self.Diagonal_DownLeft1)

        self.verticalLayoutWidget_17 = QWidget(self.ControllerKnob)
        self.verticalLayoutWidget_17.setObjectName(u"verticalLayoutWidget_17")
        self.verticalLayoutWidget_17.setGeometry(QRect(160, 160, 30, 30))
        self.Diagonal_DownRight = QVBoxLayout(self.verticalLayoutWidget_17)
        self.Diagonal_DownRight.setObjectName(u"Diagonal_DownRight")
        self.Diagonal_DownRight.setContentsMargins(0, 0, 0, 0)
        self.Diagonal_DownRight1 = QWidget(self.verticalLayoutWidget_17)
        self.Diagonal_DownRight1.setObjectName(u"Diagonal_DownRight1")
        self.Diagonal_DownRight1.setStyleSheet(u"QFrame{\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 0, 0);\n"
"}")

        self.Diagonal_DownRight.addWidget(self.Diagonal_DownRight1)

        self.verticalLayoutWidget_12 = QWidget(self.ControllerKnob)
        self.verticalLayoutWidget_12.setObjectName(u"verticalLayoutWidget_12")
        self.verticalLayoutWidget_12.setGeometry(QRect(0, -5, 30, 30))
        self.Rotate_Left = QVBoxLayout(self.verticalLayoutWidget_12)
        self.Rotate_Left.setObjectName(u"Rotate_Left")
        self.Rotate_Left.setContentsMargins(0, 0, 0, 0)
        self.Rotate_Left1 = QWidget(self.verticalLayoutWidget_12)
        self.Rotate_Left1.setObjectName(u"Rotate_Left1")
        self.Rotate_Left1.setStyleSheet(u"QFrame{\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 0, 0);\n"
"}")

        self.Rotate_Left.addWidget(self.Rotate_Left1)

        self.graphicsView_1 = QGraphicsView(self.page_1)
        self.graphicsView_1.setObjectName(u"graphicsView_1")
        self.graphicsView_1.setGeometry(QRect(10, 30, 158, 76))
        self.graphicsView_1.setStyleSheet(u"QFrame{\n"
"border-radius: 5px;\n"
"background-color: rgb(211, 211, 211);\n"
"}")
        self.graphicsView_5 = QGraphicsView(self.page_1)
        self.graphicsView_5.setObjectName(u"graphicsView_5")
        self.graphicsView_5.setGeometry(QRect(600, 140, 158, 76))
        self.graphicsView_5.setStyleSheet(u"QFrame{\n"
"border-radius: 5px;\n"
"background-color: rgb(211, 211, 211);\n"
"}")
        self.graphicsView_3 = QGraphicsView(self.page_1)
        self.graphicsView_3.setObjectName(u"graphicsView_3")
        self.graphicsView_3.setGeometry(QRect(10, 140, 158, 76))
        self.graphicsView_3.setStyleSheet(u"QFrame{\n"
"border-radius: 5px;\n"
"background-color: rgb(211, 211, 211);\n"
"}")
        self.graphicsView_6 = QGraphicsView(self.page_1)
        self.graphicsView_6.setObjectName(u"graphicsView_6")
        self.graphicsView_6.setGeometry(QRect(600, 250, 158, 76))
        self.graphicsView_6.setStyleSheet(u"QFrame{\n"
"border-radius: 5px;\n"
"background-color: rgb(211, 211, 211);\n"
"}")
        self.graphicsView_7 = QGraphicsView(self.page_1)
        self.graphicsView_7.setObjectName(u"graphicsView_7")
        self.graphicsView_7.setGeometry(QRect(10, 350, 158, 31))
        self.graphicsView_7.setStyleSheet(u"QFrame{\n"
"border-radius: 5px;\n"
"background-color: rgb(211, 211, 211);\n"
"}")
        self.graphicsView_8 = QGraphicsView(self.page_1)
        self.graphicsView_8.setObjectName(u"graphicsView_8")
        self.graphicsView_8.setGeometry(QRect(600, 350, 158, 31))
        self.graphicsView_8.setStyleSheet(u"QFrame{\n"
"border-radius: 5px;\n"
"background-color: rgb(211, 211, 211);\n"
"}")
        self.connectionLabel = QLabel(self.page_1)
        self.connectionLabel.setObjectName(u"connectionLabel")
        self.connectionLabel.setGeometry(QRect(20, 350, 130, 31))
        font2 = QFont()
        font2.setPointSize(13)
        font2.setBold(True)
        font2.setWeight(75)
        self.connectionLabel.setFont(font2)

        self.speedLabel2 = QLabel(self.page_1)
        self.speedLabel2.setObjectName(u"speedLabel2")
        self.speedLabel2.setGeometry(QRect(610, 350, 61, 31))
        self.speedLabel2.setFont(font2)

        self.speedLCD = QLCDNumber(self.page_1)
        self.speedLCD.setObjectName(u"speedLCD")
        self.speedLCD.setGeometry(QRect(680, 350, 71, 31))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.speedLCD.setFont(font)

        self.systemONLabel = QLabel(self.page_1)
        self.systemONLabel.setObjectName(u"systemONLabel")
        self.systemONLabel.setGeometry(QRect(40, 80, 111, 21))
        self.systemONLabel.setFont(font2)

        self.systemOFFLabel = QLabel(self.page_1)
        self.systemOFFLabel.setObjectName(u"systemOFFLabel")
        self.systemOFFLabel.setGeometry(QRect(625, 80, 121, 21))
        self.systemOFFLabel.setFont(font2)
        
        self.startPickLabel = QLabel(self.page_1)
        self.startPickLabel.setObjectName(u"startPickLabel")
        self.startPickLabel.setGeometry(QRect(630, 190, 111, 21))
        self.startPickLabel.setFont(font2)

        self.startDropLabel = QLabel(self.page_1)
        self.startDropLabel.setObjectName(u"startDropLabel")
        self.startDropLabel.setGeometry(QRect(630, 300, 111, 21))
        self.startDropLabel.setFont(font2)

        self.speedLabel1 = QLabel(self.page_1)
        self.speedLabel1.setObjectName(u"speedLabel1")
        self.speedLabel1.setGeometry(QRect(55, 295, 61, 31))
        self.speedLabel1.setFont(font2)

        self.rotateLabel = QLabel(self.page_1)
        self.rotateLabel.setObjectName(u"rotateLabel")
        self.rotateLabel.setGeometry(QRect(55, 185, 65, 31))
        self.rotateLabel.setFont(font2)

        self.forward = QLabel(self.page_1)
        self.forward.setObjectName(u"forward")
        self.forward.setGeometry(QRect(360, 30, 90, 31))
        self.forward.setFont(font2)

        self.reverseLabel = QLabel(self.page_1)
        self.reverseLabel.setObjectName(u"reverseLabel")
        self.reverseLabel.setGeometry(QRect(360, 300, 90, 31))
        self.reverseLabel.setFont(font2)

        self.leftLabel = QLabel(self.page_1)
        self.leftLabel.setObjectName(u"leftLabel")
        self.leftLabel.setGeometry(QRect(220, 180, 41, 21))
        self.leftLabel.setFont(font2)

        self.rightLabel = QLabel(self.page_1)
        self.rightLabel.setObjectName(u"rightLabel")
        self.rightLabel.setGeometry(QRect(520, 180, 51, 21))
        self.rightLabel.setFont(font2)

        self.verticalLayoutWidget_18 = QWidget(self.page_1)
        self.verticalLayoutWidget_18.setObjectName(u"verticalLayoutWidget_18")
        self.verticalLayoutWidget_18.setGeometry(QRect(280, 30, 21, 21))
        self.Rotate_LeftIcon = QVBoxLayout(self.verticalLayoutWidget_18)
        self.Rotate_LeftIcon.setObjectName(u"Rotate_LeftIcon")
        self.Rotate_LeftIcon.setContentsMargins(0, 0, 0, 0)
        self.Rotate_LeftIcon1 = QWidget(self.verticalLayoutWidget_18)
        self.Rotate_LeftIcon1.setObjectName(u"Rotate_LeftIcon1")
        self.Rotate_LeftIcon1.setStyleSheet(u"QFrame{\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 0, 0);\n"
"}")
        # Create a QLabel for the icon
        icon_label_minus = QLabel()
        icon1 = QIcon('/home/grips/canBus/Icon/minus.png')  # Replace with the path to your icon
        icon_label_minus.setPixmap(icon1.pixmap(16, 16))  # Set the icon size

        self.Rotate_LeftIcon.addWidget(self.Rotate_LeftIcon1)
        self.Rotate_LeftIcon.addWidget(icon_label_minus)

        self.verticalLayoutWidget_19 = QWidget(self.page_1)
        self.verticalLayoutWidget_19.setObjectName(u"verticalLayoutWidget_19")
        self.verticalLayoutWidget_19.setGeometry(QRect(480, 30, 21, 21))
        self.Rotate_RightIcon = QVBoxLayout(self.verticalLayoutWidget_19)
        self.Rotate_RightIcon.setObjectName(u"Rotate_RightIcon")
        self.Rotate_RightIcon.setContentsMargins(0, 0, 0, 0)
        self.Rotate_RightIcon1 = QWidget(self.verticalLayoutWidget_19)
        self.Rotate_RightIcon1.setObjectName(u"Rotate_RightIcon1")
        self.Rotate_RightIcon1.setStyleSheet(u"QFrame{\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 0, 0);\n"
"}")
        # Create a QLabel for the icon
        icon_label_plus = QLabel()
        icon2 = QIcon('/home/grips/canBus/Icon/plus.png')  # Replace with the path to your icon
        icon_label_plus.setPixmap(icon2.pixmap(16, 16))  # Set the icon size

        self.Rotate_RightIcon.addWidget(self.Rotate_RightIcon1)
        self.Rotate_RightIcon.addWidget(icon_label_plus)  
               
        self.verticalLayoutWidget = QWidget(self.page_1)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(70, 50, 30, 30))
        self.Light_A = QVBoxLayout(self.verticalLayoutWidget)
        self.Light_A.setObjectName(u"Light_A")
        self.Light_A.setContentsMargins(0, 0, 0, 0)
        self.Light_A1 = QWidget(self.verticalLayoutWidget)
        self.Light_A1.setObjectName(u"Light_A1")
        self.Light_A1.setStyleSheet(u"QFrame{\n"
"border-radius: 5px;\n"
"background-color: rgb(255, 0, 0);\n"
"}")

        self.Light_A.addWidget(self.Light_A1)

        self.verticalLayoutWidget_2 = QWidget(self.page_1)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(70, 160, 30, 30))
        self.Light_B = QVBoxLayout(self.verticalLayoutWidget_2)
        self.Light_B.setObjectName(u"Light_B")
        self.Light_B.setContentsMargins(0, 0, 0, 0)
        self.Light_B1 = QWidget(self.verticalLayoutWidget_2)
        self.Light_B1.setObjectName(u"Light_B1")
        self.Light_B1.setStyleSheet(u"QFrame{\n"
"border-radius: 5px;\n"
"background-color: rgb(255, 0, 0);\n"
"}")

        self.Light_B.addWidget(self.Light_B1)

        self.verticalLayoutWidget_3 = QWidget(self.page_1)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(70, 270, 30, 30))
        self.Light_C = QVBoxLayout(self.verticalLayoutWidget_3)
        self.Light_C.setObjectName(u"Light_C")
        self.Light_C.setContentsMargins(0, 0, 0, 0)
        self.Light_C1 = QWidget(self.verticalLayoutWidget_3)
        self.Light_C1.setObjectName(u"Light_C1")
        self.Light_C1.setStyleSheet(u"QFrame{\n"
"border-radius: 5px;\n"
"background-color: rgb(255, 0, 0);\n"
"}")

        self.Light_C.addWidget(self.Light_C1)

        self.verticalLayoutWidget_4 = QWidget(self.page_1)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(670, 50, 30, 30))
        self.Light_D = QVBoxLayout(self.verticalLayoutWidget_4)
        self.Light_D.setObjectName(u"Light_D")
        self.Light_D.setContentsMargins(0, 0, 0, 0)
        self.Light_D1 = QWidget(self.verticalLayoutWidget_4)
        self.Light_D1.setObjectName(u"Light_D1")
        self.Light_D1.setStyleSheet(u"QFrame{\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 0, 0);\n"
"}")

        self.Light_D.addWidget(self.Light_D1)

        self.verticalLayoutWidget_5 = QWidget(self.page_1)
        self.verticalLayoutWidget_5.setObjectName(u"verticalLayoutWidget_5")
        self.verticalLayoutWidget_5.setGeometry(QRect(670, 160, 30, 30))
        self.Light_E = QVBoxLayout(self.verticalLayoutWidget_5)
        self.Light_E.setObjectName(u"Light_E")
        self.Light_E.setContentsMargins(0, 0, 0, 0)
        self.Light_E1 = QWidget(self.verticalLayoutWidget_5)
        self.Light_E1.setObjectName(u"Light_E1")
        self.Light_E1.setStyleSheet(u"QFrame{\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 0, 0);\n"
"}")

        self.Light_E.addWidget(self.Light_E1)

        self.verticalLayoutWidget_6 = QWidget(self.page_1)
        self.verticalLayoutWidget_6.setObjectName(u"verticalLayoutWidget_6")
        self.verticalLayoutWidget_6.setGeometry(QRect(670, 270, 30, 30))
        self.Light_F = QVBoxLayout(self.verticalLayoutWidget_6)
        self.Light_F.setObjectName(u"Light_F")
        self.Light_F.setContentsMargins(0, 0, 0, 0)
        self.Light_F1 = QWidget(self.verticalLayoutWidget_6)
        self.Light_F1.setObjectName(u"Light_F1")
        self.Light_F1.setStyleSheet(u"QFrame{\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 0, 0);\n"
"}")
        self.Light_F.addWidget(self.Light_F1)   
        
        self.stackedWidget.addWidget(self.page_1)
        
        self.graphicsView_1.raise_()
        self.graphicsView_2.raise_()
        self.graphicsView_3.raise_()
        self.graphicsView_4.raise_()
        self.graphicsView_5.raise_()
        self.graphicsView_6.raise_()
        self.graphicsView_7.raise_()
        self.graphicsView_8.raise_()
        
        self.ControllerKnob_3.raise_()
        self.verticalLayoutWidget.raise_()
        self.verticalLayoutWidget_2.raise_()
        self.verticalLayoutWidget_3.raise_()
        self.verticalLayoutWidget_4.raise_()
        self.verticalLayoutWidget_5.raise_()
        self.verticalLayoutWidget_6.raise_()
        self.verticalLayoutWidget_18.raise_()
        self.verticalLayoutWidget_19.raise_()


        self.speedLCD.raise_()
        self.connectionLabel.raise_()
        self.speedLabel1.raise_()
        self.speedLabel2.raise_()
        self.systemONLabel.raise_()
        self.systemOFFLabel.raise_()
        self.startPickLabel.raise_()
        self.startDropLabel.raise_()
        self.rotateLabel.raise_()
        self.forward.raise_()
        self.reverseLabel.raise_()
        self.leftLabel.raise_()
        self.rightLabel.raise_()
        
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.display_widget = QWidget(self.page_2)
        self.display_widget.setObjectName(u"display_widget")
        self.display_widget.setGeometry(QRect(9, 9, 761, 401))
        self.verticalLayout = QVBoxLayout(self.display_widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        
        
        # Check if it works
        self.label = QLabel(self.display_widget)
        self.label.setObjectName(u"helilabel")
        self.verticalLayout.addWidget(self.label) 
        self.pixmap = QtGui.QPixmap("/home/grips/canBus/Icon/Heli.png")
        self.pixmap  = self.pixmap.scaled(730, 380, Qt.IgnoreAspectRatio)
        self.label.setPixmap(self.pixmap)
        
        self.stackedWidget.addWidget(self.page_2)
        
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.graphicsView_9 = QGraphicsView(self.page_3)
        self.graphicsView_9.setObjectName(u"graphicsView_9")
        self.graphicsView_9.setGeometry(QRect(-3, -5, 391, 401))
        self.graphicsView_9.setStyleSheet(u"QFrame{\n"
"border-radius: 5px;\n"
"background-color: rgb(211, 211, 211);\n"
"}")
        self.graphicsView_10 = QGraphicsView(self.page_3)
        self.graphicsView_10.setObjectName(u"graphicsView_10")
        self.graphicsView_10.setGeometry(QRect(397, -5, 361, 391))
        self.graphicsView_10.setStyleSheet(u"QFrame{\n"
"border-radius: 5px;\n"
"background-color: rgb(211, 211, 211);\n"
"}")
        self.motorLabel_2 = QLabel(self.page_3)
        self.motorLabel_2.setObjectName(u"motorLabel_2")
        self.motorLabel_2.setGeometry(QRect(10, 30, 321, 21))
        font3 = QFont()
        font3.setPointSize(9)
        font3.setBold(True)
        font3.setWeight(75)
        self.motorLabel_2.setFont(font3)
        self.motorLabel_2.setStyleSheet(u"")
        self.motorLabel_2.setTextFormat(Qt.AutoText)
        self.motorLabel_3 = QLabel(self.page_3)
        self.motorLabel_3.setObjectName(u"motorLabel_3")
        self.motorLabel_3.setGeometry(QRect(10, 50, 321, 21))
        self.motorLabel_3.setFont(font3)
        self.motorLabel_3.setStyleSheet(u"")
        self.motorLabel_3.setTextFormat(Qt.AutoText)
        self.motorLabel_4 = QLabel(self.page_3)
        self.motorLabel_4.setObjectName(u"motorLabel_4")
        self.motorLabel_4.setGeometry(QRect(10, 70, 321, 21))
        self.motorLabel_4.setFont(font3)
        self.motorLabel_4.setStyleSheet(u"")
        self.motorLabel_4.setTextFormat(Qt.AutoText)
        self.motorLabel_5 = QLabel(self.page_3)
        self.motorLabel_5.setObjectName(u"motorLabel_5")
        self.motorLabel_5.setGeometry(QRect(10, 100, 341, 21))
        self.motorLabel_5.setFont(font3)
        self.motorLabel_5.setStyleSheet(u"")
        self.motorLabel_5.setTextFormat(Qt.AutoText)
        self.motorLabel_6 = QLabel(self.page_3)
        self.motorLabel_6.setObjectName(u"motorLabel_6")
        self.motorLabel_6.setGeometry(QRect(10, 120, 341, 21))
        self.motorLabel_6.setFont(font3)
        self.motorLabel_6.setStyleSheet(u"")
        self.motorLabel_6.setTextFormat(Qt.AutoText)
        self.motorLabel_7 = QLabel(self.page_3)
        self.motorLabel_7.setObjectName(u"motorLabel_7")
        self.motorLabel_7.setGeometry(QRect(10, 140, 341, 21))
        self.motorLabel_7.setFont(font3)
        self.motorLabel_7.setStyleSheet(u"")
        self.motorLabel_7.setTextFormat(Qt.AutoText)
        self.motorLabel_8 = QLabel(self.page_3)
        self.motorLabel_8.setObjectName(u"motorLabel_8")
        self.motorLabel_8.setGeometry(QRect(10, 160, 341, 21))
        self.motorLabel_8.setFont(font3)
        self.motorLabel_8.setStyleSheet(u"")
        self.motorLabel_8.setTextFormat(Qt.AutoText)
        self.motorLabel_9 = QLabel(self.page_3)
        self.motorLabel_9.setObjectName(u"motorLabel_9")
        self.motorLabel_9.setGeometry(QRect(10, 190, 271, 21))
        self.motorLabel_9.setFont(font3)
        self.motorLabel_9.setStyleSheet(u"")
        self.motorLabel_9.setTextFormat(Qt.AutoText)
        self.motorLabel_10 = QLabel(self.page_3)
        self.motorLabel_10.setObjectName(u"motorLabel_10")
        self.motorLabel_10.setGeometry(QRect(10, 210, 271, 21))
        self.motorLabel_10.setFont(font3)
        self.motorLabel_10.setStyleSheet(u"")
        self.motorLabel_10.setTextFormat(Qt.AutoText)
        self.motorLabel_11 = QLabel(self.page_3)
        self.motorLabel_11.setObjectName(u"motorLabel_11")
        self.motorLabel_11.setGeometry(QRect(10, 230, 271, 21))
        self.motorLabel_11.setFont(font3)
        self.motorLabel_11.setStyleSheet(u"")
        self.motorLabel_11.setTextFormat(Qt.AutoText)
        self.motorLabel_12 = QLabel(self.page_3)
        self.motorLabel_12.setObjectName(u"motorLabel_12")
        self.motorLabel_12.setGeometry(QRect(10, 250, 271, 21))
        self.motorLabel_12.setFont(font3)
        self.motorLabel_12.setStyleSheet(u"")
        self.motorLabel_12.setTextFormat(Qt.AutoText)
        self.motorLabel_13 = QLabel(self.page_3)
        self.motorLabel_13.setObjectName(u"motorLabel_13")
        self.motorLabel_13.setGeometry(QRect(10, 280, 341, 21))
        self.motorLabel_13.setFont(font3)
        self.motorLabel_13.setStyleSheet(u"")
        self.motorLabel_13.setTextFormat(Qt.AutoText)
        self.motorLabel_1 = QLabel(self.page_3)
        self.motorLabel_1.setObjectName(u"motorLabel_1")
        self.motorLabel_1.setGeometry(QRect(10, 10, 321, 21))
        self.motorLabel_1.setFont(font3)
        self.motorLabel_1.setStyleSheet(u"")
        self.motorLabel_1.setTextFormat(Qt.AutoText)
        self.sensorLabel_1 = QLabel(self.page_3)
        self.sensorLabel_1.setObjectName(u"sensorLabel_1")
        self.sensorLabel_1.setGeometry(QRect(400, 10, 321, 21))
        self.sensorLabel_1.setFont(font3)
        self.sensorLabel_1.setStyleSheet(u"")
        self.sensorLabel_1.setTextFormat(Qt.AutoText)
        self.sensorLabel_2 = QLabel(self.page_3)
        self.sensorLabel_2.setObjectName(u"sensorLabel_2")
        self.sensorLabel_2.setGeometry(QRect(400, 30, 321, 21))
        self.sensorLabel_2.setFont(font3)
        self.sensorLabel_2.setStyleSheet(u"")
        self.sensorLabel_2.setTextFormat(Qt.AutoText)
        self.sensorLabel_3 = QLabel(self.page_3)
        self.sensorLabel_3.setObjectName(u"sensorLabel_3")
        self.sensorLabel_3.setGeometry(QRect(400, 50, 321, 21))
        self.sensorLabel_3.setFont(font3)
        self.sensorLabel_3.setStyleSheet(u"")
        self.sensorLabel_3.setTextFormat(Qt.AutoText)
        self.sensorLabel_4 = QLabel(self.page_3)
        self.sensorLabel_4.setObjectName(u"sensorLabel_4")
        self.sensorLabel_4.setGeometry(QRect(400, 70, 321, 21))
        self.sensorLabel_4.setFont(font3)
        self.sensorLabel_4.setStyleSheet(u"")
        self.sensorLabel_4.setTextFormat(Qt.AutoText)
        self.sensorLabel_5 = QLabel(self.page_3)
        self.sensorLabel_5.setObjectName(u"sensorLabel_5")
        self.sensorLabel_5.setGeometry(QRect(400, 90, 321, 21))
        self.sensorLabel_5.setFont(font3)
        self.sensorLabel_5.setStyleSheet(u"")
        self.sensorLabel_5.setTextFormat(Qt.AutoText)
        self.sensorLabel_6 = QLabel(self.page_3)
        self.sensorLabel_6.setObjectName(u"sensorLabel_6")
        self.sensorLabel_6.setGeometry(QRect(400, 110, 321, 21))
        self.sensorLabel_6.setFont(font3)
        self.sensorLabel_6.setStyleSheet(u"")
        self.sensorLabel_6.setTextFormat(Qt.AutoText)
        self.sensorLabel_7 = QLabel(self.page_3)
        self.sensorLabel_7.setObjectName(u"sensorLabel_7")
        self.sensorLabel_7.setGeometry(QRect(400, 130, 321, 21))
        self.sensorLabel_7.setFont(font3)
        self.sensorLabel_7.setStyleSheet(u"")
        self.sensorLabel_7.setTextFormat(Qt.AutoText)
        self.sensorLabel_8 = QLabel(self.page_3)
        self.sensorLabel_8.setObjectName(u"sensorLabel_8")
        self.sensorLabel_8.setGeometry(QRect(400, 150, 321, 21))
        self.sensorLabel_8.setFont(font3)
        self.sensorLabel_8.setStyleSheet(u"")
        self.sensorLabel_8.setTextFormat(Qt.AutoText)
        self.sensorLabel_9 = QLabel(self.page_3)
        self.sensorLabel_9.setObjectName(u"sensorLabel_9")
        self.sensorLabel_9.setGeometry(QRect(400, 180, 321, 21))
        self.sensorLabel_9.setFont(font3)
        self.sensorLabel_9.setStyleSheet(u"")
        self.sensorLabel_9.setTextFormat(Qt.AutoText)
        self.sensorLabel_10 = QLabel(self.page_3)
        self.sensorLabel_10.setObjectName(u"sensorLabel_10")
        self.sensorLabel_10.setGeometry(QRect(400, 200, 331, 21))
        self.sensorLabel_10.setFont(font3)
        self.sensorLabel_10.setStyleSheet(u"")
        self.sensorLabel_10.setTextFormat(Qt.AutoText)
        self.sensorLabel_11 = QLabel(self.page_3)
        self.sensorLabel_11.setObjectName(u"sensorLabel_11")
        self.sensorLabel_11.setGeometry(QRect(400, 220, 331, 21))
        self.sensorLabel_11.setFont(font3)
        self.sensorLabel_11.setStyleSheet(u"")
        self.sensorLabel_11.setTextFormat(Qt.AutoText)
        self.sensorLabel_12 = QLabel(self.page_3)
        self.sensorLabel_12.setObjectName(u"sensorLabel_12")
        self.sensorLabel_12.setGeometry(QRect(400, 240, 331, 21))
        self.sensorLabel_12.setFont(font3)
        self.sensorLabel_12.setStyleSheet(u"")
        self.sensorLabel_12.setTextFormat(Qt.AutoText)
        self.sensorLabel_13 = QLabel(self.page_3)
        self.sensorLabel_13.setObjectName(u"sensorLabel_13")
        self.sensorLabel_13.setGeometry(QRect(400, 270, 301, 21))
        self.sensorLabel_13.setFont(font3)
        self.sensorLabel_13.setStyleSheet(u"")
        self.sensorLabel_13.setTextFormat(Qt.AutoText)
        self.sensorLabel_14 = QLabel(self.page_3)
        self.sensorLabel_14.setObjectName(u"sensorLabel_14")
        self.sensorLabel_14.setGeometry(QRect(400, 290, 301, 21))
        self.sensorLabel_14.setFont(font3)
        self.sensorLabel_14.setStyleSheet(u"")
        self.sensorLabel_14.setTextFormat(Qt.AutoText)
        self.motorLabel_14 = QLabel(self.page_3)
        self.motorLabel_14.setObjectName(u"motorLabel_14")
        self.motorLabel_14.setGeometry(QRect(10, 300, 341, 21))
        self.motorLabel_14.setFont(font3)
        self.motorLabel_14.setStyleSheet(u"")
        self.motorLabel_14.setTextFormat(Qt.AutoText)
        self.sensorLabel_15 = QLabel(self.page_3)
        self.sensorLabel_15.setObjectName(u"sensorLabel_15")
        self.sensorLabel_15.setGeometry(QRect(400, 310, 301, 21))
        self.sensorLabel_15.setFont(font3)
        self.sensorLabel_15.setStyleSheet(u"")
        self.sensorLabel_15.setTextFormat(Qt.AutoText)
        self.sensorLabel_16 = QLabel(self.page_3)
        self.sensorLabel_16.setObjectName(u"sensorLabel_16")
        self.sensorLabel_16.setGeometry(QRect(400, 330, 301, 21))
        self.sensorLabel_16.setFont(font3)
        self.sensorLabel_16.setStyleSheet(u"")
        self.sensorLabel_16.setTextFormat(Qt.AutoText)
        self.sensorLabel_17 = QLabel(self.page_3)
        self.sensorLabel_17.setObjectName(u"sensorLabel_17")
        self.sensorLabel_17.setGeometry(QRect(400, 350, 281, 21))
        self.sensorLabel_17.setFont(font3)
        self.sensorLabel_17.setStyleSheet(u"")
        self.sensorLabel_17.setTextFormat(Qt.AutoText)
        self.canOpenLabel_1 = QLabel(self.page_3)
        self.canOpenLabel_1.setObjectName(u"canOpenLabel_1")
        self.canOpenLabel_1.setGeometry(QRect(10, 350, 111, 21))
        self.canOpenLabel_1.setFont(font3)
        self.canOpenLabel_1.setStyleSheet(u"")
        self.canOpenLabel_1.setTextFormat(Qt.AutoText)
        self.canOpenLabel_2 = QLabel(self.page_3)
        self.canOpenLabel_2.setObjectName(u"canOpenLabel_2")
        self.canOpenLabel_2.setGeometry(QRect(122, 330, 16, 21))
        self.canOpenLabel_2.setFont(font3)
        self.canOpenLabel_2.setStyleSheet(u"")
        self.canOpenLabel_2.setTextFormat(Qt.AutoText)
        self.canOpenLabel_3 = QLabel(self.page_3)
        self.canOpenLabel_3.setObjectName(u"canOpenLabel_3")
        self.canOpenLabel_3.setGeometry(QRect(152, 330, 16, 21))
        self.canOpenLabel_3.setFont(font3)
        self.canOpenLabel_3.setStyleSheet(u"")
        self.canOpenLabel_3.setTextFormat(Qt.AutoText)
        self.canOpenLabel_4 = QLabel(self.page_3)
        self.canOpenLabel_4.setObjectName(u"canOpenLabel_4")
        self.canOpenLabel_4.setGeometry(QRect(182, 330, 16, 21))
        self.canOpenLabel_4.setFont(font3)
        self.canOpenLabel_4.setStyleSheet(u"")
        self.canOpenLabel_4.setTextFormat(Qt.AutoText)
        self.canOpenLabel_5 = QLabel(self.page_3)
        self.canOpenLabel_5.setObjectName(u"canOpenLabel_5")
        self.canOpenLabel_5.setGeometry(QRect(212, 330, 16, 21))
        self.canOpenLabel_5.setFont(font3)
        self.canOpenLabel_5.setStyleSheet(u"")
        self.canOpenLabel_5.setTextFormat(Qt.AutoText)
        self.canOpenLabel_6 = QLabel(self.page_3)
        self.canOpenLabel_6.setObjectName(u"canOpenLabel_6")
        self.canOpenLabel_6.setGeometry(QRect(242, 330, 16, 21))
        self.canOpenLabel_6.setFont(font3)
        self.canOpenLabel_6.setStyleSheet(u"")
        self.canOpenLabel_6.setTextFormat(Qt.AutoText)
        self.canOpenLabel_7 = QLabel(self.page_3)
        self.canOpenLabel_7.setObjectName(u"canOpenLabel_7")
        self.canOpenLabel_7.setGeometry(QRect(272, 330, 16, 21))
        self.canOpenLabel_7.setFont(font3)
        self.canOpenLabel_7.setStyleSheet(u"")
        self.canOpenLabel_7.setTextFormat(Qt.AutoText)
        self.canOpenLabel_8 = QLabel(self.page_3)
        self.canOpenLabel_8.setObjectName(u"canOpenLabel_8")
        self.canOpenLabel_8.setGeometry(QRect(302, 330, 16, 21))
        self.canOpenLabel_8.setFont(font3)
        self.canOpenLabel_8.setStyleSheet(u"")
        self.canOpenLabel_8.setTextFormat(Qt.AutoText)
        self.canOpenLabel_9 = QLabel(self.page_3)
        self.canOpenLabel_9.setObjectName(u"canOpenLabel_9")
        self.canOpenLabel_9.setGeometry(QRect(332, 330, 16, 21))
        self.canOpenLabel_9.setFont(font3)
        self.canOpenLabel_9.setStyleSheet(u"")
        self.canOpenLabel_9.setTextFormat(Qt.AutoText)
        
        self.verticalLayoutWidget_20 = QWidget(self.page_3)
        self.verticalLayoutWidget_20.setObjectName(u"verticalLayoutWidget_20")
        self.verticalLayoutWidget_20.setGeometry(QRect(300, 5, 16, 21))
        self.BM1 = QVBoxLayout(self.verticalLayoutWidget_20)
        self.BM1.setObjectName(u"BM1")
        self.BM1.setContentsMargins(0, 0, 0, 0)
        self.BM_1 = QWidget(self.verticalLayoutWidget_20)
        self.BM_1.setObjectName(u"BM_1")
        self.BM_1.setStyleSheet(u"QFrame{\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 0, 0);\n"
"}")

        self.BM1.addWidget(self.BM_1)

        self.verticalLayoutWidget_21 = QWidget(self.page_3)
        self.verticalLayoutWidget_21.setObjectName(u"verticalLayoutWidget_21")
        self.verticalLayoutWidget_21.setGeometry(QRect(300, 25, 16, 21))
        self.BM2 = QVBoxLayout(self.verticalLayoutWidget_21)
        self.BM2.setObjectName(u"BM2")
        self.BM2.setContentsMargins(0, 0, 0, 0)
        self.BM_2 = QWidget(self.verticalLayoutWidget_21)
        self.BM_2.setObjectName(u"BM_2")
        self.BM_2.setStyleSheet(u"QFrame{\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 0, 0);\n"
"}")

        self.BM2.addWidget(self.BM_2)

        self.verticalLayoutWidget_22 = QWidget(self.page_3)
        self.verticalLayoutWidget_22.setObjectName(u"verticalLayoutWidget_22")
        self.verticalLayoutWidget_22.setGeometry(QRect(300, 45, 16, 21))
        self.BM3 = QVBoxLayout(self.verticalLayoutWidget_22)
        self.BM3.setObjectName(u"BM3")
        self.BM3.setContentsMargins(0, 0, 0, 0)
        self.BM_3 = QWidget(self.verticalLayoutWidget_22)
        self.BM_3.setObjectName(u"BM_3")
        self.BM_3.setStyleSheet(u"QFrame{\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 0, 0);\n"
"}")

        self.BM3.addWidget(self.BM_3)

        self.verticalLayoutWidget_23 = QWidget(self.page_3)
        self.verticalLayoutWidget_23.setObjectName(u"verticalLayoutWidget_23")
        self.verticalLayoutWidget_23.setGeometry(QRect(300, 65, 16, 21))
        self.BM4 = QVBoxLayout(self.verticalLayoutWidget_23)
        self.BM4.setObjectName(u"BM4")
        self.BM4.setContentsMargins(0, 0, 0, 0)
        self.BM_4 = QWidget(self.verticalLayoutWidget_23)
        self.BM_4.setObjectName(u"BM_4")
        self.BM_4.setStyleSheet(u"QFrame{\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 0, 0);\n"
"}")

        self.BM4.addWidget(self.BM_4)

        self.verticalLayoutWidget_24 = QWidget(self.page_3)
        self.verticalLayoutWidget_24.setObjectName(u"verticalLayoutWidget_24")
        self.verticalLayoutWidget_24.setGeometry(QRect(300, 95, 16, 21))
        self.BM5 = QVBoxLayout(self.verticalLayoutWidget_24)
        self.BM5.setObjectName(u"BM5")
        self.BM5.setContentsMargins(0, 0, 0, 0)
        self.BM_5 = QWidget(self.verticalLayoutWidget_24)
        self.BM_5.setObjectName(u"BM_5")
        self.BM_5.setStyleSheet(u"QFrame{\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 0, 0);\n"
"}")

        self.BM5.addWidget(self.BM_5)

        self.verticalLayoutWidget_25 = QWidget(self.page_3)
        self.verticalLayoutWidget_25.setObjectName(u"verticalLayoutWidget_25")
        self.verticalLayoutWidget_25.setGeometry(QRect(300, 115, 16, 21))
        self.BM6 = QVBoxLayout(self.verticalLayoutWidget_25)
        self.BM6.setObjectName(u"BM6")
        self.BM6.setContentsMargins(0, 0, 0, 0)
        self.BM_6 = QWidget(self.verticalLayoutWidget_25)
        self.BM_6.setObjectName(u"BM_6")
        self.BM_6.setStyleSheet(u"QFrame{\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 0, 0);\n"
"}")

        self.BM6.addWidget(self.BM_6)

        self.verticalLayoutWidget_26 = QWidget(self.page_3)
        self.verticalLayoutWidget_26.setObjectName(u"verticalLayoutWidget_26")
        self.verticalLayoutWidget_26.setGeometry(QRect(300, 135, 16, 21))
        self.BM7 = QVBoxLayout(self.verticalLayoutWidget_26)
        self.BM7.setObjectName(u"BM7")
        self.BM7.setContentsMargins(0, 0, 0, 0)
        self.BM_7 = QWidget(self.verticalLayoutWidget_26)
        self.BM_7.setObjectName(u"BM_7")
        self.BM_7.setStyleSheet(u"QFrame{\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 0, 0);\n"
"}")

        self.BM7.addWidget(self.BM_7)

        self.verticalLayoutWidget_27 = QWidget(self.page_3)
        self.verticalLayoutWidget_27.setObjectName(u"verticalLayoutWidget_27")
        self.verticalLayoutWidget_27.setGeometry(QRect(300, 155, 16, 21))
        self.BM8 = QVBoxLayout(self.verticalLayoutWidget_27)
        self.BM8.setObjectName(u"BM8")
        self.BM8.setContentsMargins(0, 0, 0, 0)
        self.BM_8 = QWidget(self.verticalLayoutWidget_27)
        self.BM_8.setObjectName(u"BM_8")
        self.BM_8.setStyleSheet(u"QFrame{\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 0, 0);\n"
"}")

        self.BM8.addWidget(self.BM_8)

        self.verticalLayoutWidget_28 = QWidget(self.page_3)
        self.verticalLayoutWidget_28.setObjectName(u"verticalLayoutWidget_28")
        self.verticalLayoutWidget_28.setGeometry(QRect(240, 185, 16, 21))
        self.SM1 = QVBoxLayout(self.verticalLayoutWidget_28)
        self.SM1.setObjectName(u"SM1")
        self.SM1.setContentsMargins(0, 0, 0, 0)
        self.SM_1 = QWidget(self.verticalLayoutWidget_28)
        self.SM_1.setObjectName(u"SM_1")
        self.SM_1.setStyleSheet(u"QFrame{\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 0, 0);\n"
"}")

        self.SM1.addWidget(self.SM_1)

        self.verticalLayoutWidget_29 = QWidget(self.page_3)
        self.verticalLayoutWidget_29.setObjectName(u"verticalLayoutWidget_29")
        self.verticalLayoutWidget_29.setGeometry(QRect(240, 205, 16, 21))
        self.SM2 = QVBoxLayout(self.verticalLayoutWidget_29)
        self.SM2.setObjectName(u"SM2")
        self.SM2.setContentsMargins(0, 0, 0, 0)
        self.SM_2 = QWidget(self.verticalLayoutWidget_29)
        self.SM_2.setObjectName(u"SM_2")
        self.SM_2.setStyleSheet(u"QFrame{\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 0, 0);\n"
"}")

        self.SM2.addWidget(self.SM_2)

        self.verticalLayoutWidget_30 = QWidget(self.page_3)
        self.verticalLayoutWidget_30.setObjectName(u"verticalLayoutWidget_30")
        self.verticalLayoutWidget_30.setGeometry(QRect(240, 225, 16, 21))
        self.SM3 = QVBoxLayout(self.verticalLayoutWidget_30)
        self.SM3.setObjectName(u"SM3")
        self.SM3.setContentsMargins(0, 0, 0, 0)
        self.SM_3 = QWidget(self.verticalLayoutWidget_30)
        self.SM_3.setObjectName(u"SM_3")
        self.SM_3.setStyleSheet(u"QFrame{\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 0, 0);\n"
"}")

        self.SM3.addWidget(self.SM_3)

        self.verticalLayoutWidget_31 = QWidget(self.page_3)
        self.verticalLayoutWidget_31.setObjectName(u"verticalLayoutWidget_31")
        self.verticalLayoutWidget_31.setGeometry(QRect(240, 245, 16, 21))
        self.SM4 = QVBoxLayout(self.verticalLayoutWidget_31)
        self.SM4.setObjectName(u"SM4")
        self.SM4.setContentsMargins(0, 0, 0, 0)
        self.SM_4 = QWidget(self.verticalLayoutWidget_31)
        self.SM_4.setObjectName(u"SM_4")
        self.SM_4.setStyleSheet(u"QFrame{\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 0, 0);\n"
"}")

        self.SM4.addWidget(self.SM_4)

        self.verticalLayoutWidget_32 = QWidget(self.page_3)
        self.verticalLayoutWidget_32.setObjectName(u"verticalLayoutWidget_32")
        self.verticalLayoutWidget_32.setGeometry(QRect(310, 275, 16, 21))
        self.AM1 = QVBoxLayout(self.verticalLayoutWidget_32)
        self.AM1.setObjectName(u"AM1")
        self.AM1.setContentsMargins(0, 0, 0, 0)
        self.AM_1 = QWidget(self.verticalLayoutWidget_32)
        self.AM_1.setObjectName(u"AM_1")
        self.AM_1.setStyleSheet(u"QFrame{\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 0, 0);\n"
"}")

        self.AM1.addWidget(self.AM_1)

        self.verticalLayoutWidget_33 = QWidget(self.page_3)
        self.verticalLayoutWidget_33.setObjectName(u"verticalLayoutWidget_33")
        self.verticalLayoutWidget_33.setGeometry(QRect(310, 295, 16, 21))
        self.PV1 = QVBoxLayout(self.verticalLayoutWidget_33)
        self.PV1.setObjectName(u"PV1")
        self.PV1.setContentsMargins(0, 0, 0, 0)
        self.PV_1 = QWidget(self.verticalLayoutWidget_33)
        self.PV_1.setObjectName(u"PV_1")
        self.PV_1.setStyleSheet(u"QFrame{\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 0, 0);\n"
"}")

        self.PV1.addWidget(self.PV_1)

        self.verticalLayoutWidget_34 = QWidget(self.page_3)
        self.verticalLayoutWidget_34.setObjectName(u"verticalLayoutWidget_34")
        self.verticalLayoutWidget_34.setGeometry(QRect(680, 5, 16, 21))
        self.DS1 = QVBoxLayout(self.verticalLayoutWidget_34)
        self.DS1.setObjectName(u"DS1")
        self.DS1.setContentsMargins(0, 0, 0, 0)
        self.DS_1 = QWidget(self.verticalLayoutWidget_34)
        self.DS_1.setObjectName(u"DS_1")
        self.DS_1.setStyleSheet(u"QFrame{\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 0, 0);\n"
"}")

        self.DS1.addWidget(self.DS_1)

        self.verticalLayoutWidget_35 = QWidget(self.page_3)
        self.verticalLayoutWidget_35.setObjectName(u"verticalLayoutWidget_35")
        self.verticalLayoutWidget_35.setGeometry(QRect(680, 25, 16, 21))
        self.DS2 = QVBoxLayout(self.verticalLayoutWidget_35)
        self.DS2.setObjectName(u"DS2")
        self.DS2.setContentsMargins(0, 0, 0, 0)
        self.DS_2 = QWidget(self.verticalLayoutWidget_35)
        self.DS_2.setObjectName(u"DS_2")
        self.DS_2.setStyleSheet(u"QFrame{\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 0, 0);\n"
"}")

        self.DS2.addWidget(self.DS_2)

        self.verticalLayoutWidget_36 = QWidget(self.page_3)
        self.verticalLayoutWidget_36.setObjectName(u"verticalLayoutWidget_36")
        self.verticalLayoutWidget_36.setGeometry(QRect(680, 45, 16, 21))
        self.DS3 = QVBoxLayout(self.verticalLayoutWidget_36)
        self.DS3.setObjectName(u"DS3")
        self.DS3.setContentsMargins(0, 0, 0, 0)
        self.DS_3 = QWidget(self.verticalLayoutWidget_36)
        self.DS_3.setObjectName(u"DS_3")
        self.DS_3.setStyleSheet(u"QFrame{\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 0, 0);\n"
"}")

        self.DS3.addWidget(self.DS_3)

        self.verticalLayoutWidget_37 = QWidget(self.page_3)
        self.verticalLayoutWidget_37.setObjectName(u"verticalLayoutWidget_37")
        self.verticalLayoutWidget_37.setGeometry(QRect(680, 65, 16, 21))
        self.DS4 = QVBoxLayout(self.verticalLayoutWidget_37)
        self.DS4.setObjectName(u"DS4")
        self.DS4.setContentsMargins(0, 0, 0, 0)
        self.DS_4 = QWidget(self.verticalLayoutWidget_37)
        self.DS_4.setObjectName(u"DS_4")
        self.DS_4.setStyleSheet(u"QFrame{\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 0, 0);\n"
"}")

        self.DS4.addWidget(self.DS_4)

        self.verticalLayoutWidget_38 = QWidget(self.page_3)
        self.verticalLayoutWidget_38.setObjectName(u"verticalLayoutWidget_38")
        self.verticalLayoutWidget_38.setGeometry(QRect(680, 85, 16, 21))
        self.DS5 = QVBoxLayout(self.verticalLayoutWidget_38)
        self.DS5.setObjectName(u"DS5")
        self.DS5.setContentsMargins(0, 0, 0, 0)
        self.DS_5 = QWidget(self.verticalLayoutWidget_38)
        self.DS_5.setObjectName(u"DS_5")
        self.DS_5.setStyleSheet(u"QFrame{\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 0, 0);\n"
"}")

        self.DS5.addWidget(self.DS_5)

        self.verticalLayoutWidget_39 = QWidget(self.page_3)
        self.verticalLayoutWidget_39.setObjectName(u"verticalLayoutWidget_39")
        self.verticalLayoutWidget_39.setGeometry(QRect(680, 105, 16, 21))
        self.DS6 = QVBoxLayout(self.verticalLayoutWidget_39)
        self.DS6.setObjectName(u"DS6")
        self.DS6.setContentsMargins(0, 0, 0, 0)
        self.DS_6 = QWidget(self.verticalLayoutWidget_39)
        self.DS_6.setObjectName(u"DS_6")
        self.DS_6.setStyleSheet(u"QFrame{\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 0, 0);\n"
"}")

        self.DS6.addWidget(self.DS_6)

        self.verticalLayoutWidget_40 = QWidget(self.page_3)
        self.verticalLayoutWidget_40.setObjectName(u"verticalLayoutWidget_40")
        self.verticalLayoutWidget_40.setGeometry(QRect(680, 125, 16, 21))
        self.DS7 = QVBoxLayout(self.verticalLayoutWidget_40)
        self.DS7.setObjectName(u"DS7")
        self.DS7.setContentsMargins(0, 0, 0, 0)
        self.DS_7 = QWidget(self.verticalLayoutWidget_40)
        self.DS_7.setObjectName(u"DS_7")
        self.DS_7.setStyleSheet(u"QFrame{\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 0, 0);\n"
"}")

        self.DS7.addWidget(self.DS_7)

        self.verticalLayoutWidget_41 = QWidget(self.page_3)
        self.verticalLayoutWidget_41.setObjectName(u"verticalLayoutWidget_41")
        self.verticalLayoutWidget_41.setGeometry(QRect(680, 145, 16, 21))
        self.DS8 = QVBoxLayout(self.verticalLayoutWidget_41)
        self.DS8.setObjectName(u"DS8")
        self.DS8.setContentsMargins(0, 0, 0, 0)
        self.DS_8 = QWidget(self.verticalLayoutWidget_41)
        self.DS_8.setObjectName(u"DS_8")
        self.DS_8.setStyleSheet(u"QFrame{\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 0, 0);\n"
"}")

        self.DS8.addWidget(self.DS_8)

        self.verticalLayoutWidget_42 = QWidget(self.page_3)
        self.verticalLayoutWidget_42.setObjectName(u"verticalLayoutWidget_42")
        self.verticalLayoutWidget_42.setGeometry(QRect(680, 175, 16, 21))
        self.DS9 = QVBoxLayout(self.verticalLayoutWidget_42)
        self.DS9.setObjectName(u"DS9")
        self.DS9.setContentsMargins(0, 0, 0, 0)
        self.DS_9 = QWidget(self.verticalLayoutWidget_42)
        self.DS_9.setObjectName(u"DS_9")
        self.DS_9.setStyleSheet(u"QFrame{\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 0, 0);\n"
"}")

        self.DS9.addWidget(self.DS_9)

        self.verticalLayoutWidget_43 = QWidget(self.page_3)
        self.verticalLayoutWidget_43.setObjectName(u"verticalLayoutWidget_43")
        self.verticalLayoutWidget_43.setGeometry(QRect(680, 195, 16, 21))
        self.DS10 = QVBoxLayout(self.verticalLayoutWidget_43)
        self.DS10.setObjectName(u"DS10")
        self.DS10.setContentsMargins(0, 0, 0, 0)
        self.DS_10 = QWidget(self.verticalLayoutWidget_43)
        self.DS_10.setObjectName(u"DS_10")
        self.DS_10.setStyleSheet(u"QFrame{\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 0, 0);\n"
"}")

        self.DS10.addWidget(self.DS_10)

        self.verticalLayoutWidget_44 = QWidget(self.page_3)
        self.verticalLayoutWidget_44.setObjectName(u"verticalLayoutWidget_44")
        self.verticalLayoutWidget_44.setGeometry(QRect(680, 215, 16, 21))
        self.DS11 = QVBoxLayout(self.verticalLayoutWidget_44)
        self.DS11.setObjectName(u"DS11")
        self.DS11.setContentsMargins(0, 0, 0, 0)
        self.DS_11 = QWidget(self.verticalLayoutWidget_44)
        self.DS_11.setObjectName(u"DS_11")
        self.DS_11.setStyleSheet(u"QFrame{\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 0, 0);\n"
"}")

        self.DS11.addWidget(self.DS_11)

        self.verticalLayoutWidget_45 = QWidget(self.page_3)
        self.verticalLayoutWidget_45.setObjectName(u"verticalLayoutWidget_45")
        self.verticalLayoutWidget_45.setGeometry(QRect(680, 235, 16, 21))
        self.DS12 = QVBoxLayout(self.verticalLayoutWidget_45)
        self.DS12.setObjectName(u"DS12")
        self.DS12.setContentsMargins(0, 0, 0, 0)
        self.DS_12 = QWidget(self.verticalLayoutWidget_45)
        self.DS_12.setObjectName(u"DS_12")
        self.DS_12.setStyleSheet(u"QFrame{\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 0, 0);\n"
"}")

        self.DS12.addWidget(self.DS_12)

        self.verticalLayoutWidget_46 = QWidget(self.page_3)
        self.verticalLayoutWidget_46.setObjectName(u"verticalLayoutWidget_46")
        self.verticalLayoutWidget_46.setGeometry(QRect(680, 265, 16, 21))
        self.AS1 = QVBoxLayout(self.verticalLayoutWidget_46)
        self.AS1.setObjectName(u"AS1")
        self.AS1.setContentsMargins(0, 0, 0, 0)
        self.AS_1 = QWidget(self.verticalLayoutWidget_46)
        self.AS_1.setObjectName(u"AS_1")
        self.AS_1.setStyleSheet(u"QFrame{\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 0, 0);\n"
"}")

        self.AS1.addWidget(self.AS_1)

        self.verticalLayoutWidget_47 = QWidget(self.page_3)
        self.verticalLayoutWidget_47.setObjectName(u"verticalLayoutWidget_47")
        self.verticalLayoutWidget_47.setGeometry(QRect(680, 285, 16, 21))
        self.AS2 = QVBoxLayout(self.verticalLayoutWidget_47)
        self.AS2.setObjectName(u"AS2")
        self.AS2.setContentsMargins(0, 0, 0, 0)
        self.AS_2 = QWidget(self.verticalLayoutWidget_47)
        self.AS_2.setObjectName(u"AS_2")
        self.AS_2.setStyleSheet(u"QFrame{\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 0, 0);\n"
"}")

        self.AS2.addWidget(self.AS_2)

        self.verticalLayoutWidget_48 = QWidget(self.page_3)
        self.verticalLayoutWidget_48.setObjectName(u"verticalLayoutWidget_48")
        self.verticalLayoutWidget_48.setGeometry(QRect(680, 305, 16, 21))
        self.AS3 = QVBoxLayout(self.verticalLayoutWidget_48)
        self.AS3.setObjectName(u"AS3")
        self.AS3.setContentsMargins(0, 0, 0, 0)
        self.AS_3 = QWidget(self.verticalLayoutWidget_48)
        self.AS_3.setObjectName(u"AS_3")
        self.AS_3.setStyleSheet(u"QFrame{\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 0, 0);\n"
"}")

        self.AS3.addWidget(self.AS_3)

        self.verticalLayoutWidget_49 = QWidget(self.page_3)
        self.verticalLayoutWidget_49.setObjectName(u"verticalLayoutWidget_49")
        self.verticalLayoutWidget_49.setGeometry(QRect(680, 325, 16, 21))
        self.AS4 = QVBoxLayout(self.verticalLayoutWidget_49)
        self.AS4.setObjectName(u"AS4")
        self.AS4.setContentsMargins(0, 0, 0, 0)
        self.AS_4 = QWidget(self.verticalLayoutWidget_49)
        self.AS_4.setObjectName(u"AS_4")
        self.AS_4.setStyleSheet(u"QFrame{\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 0, 0);\n"
"}")

        self.AS4.addWidget(self.AS_4)

        self.verticalLayoutWidget_50 = QWidget(self.page_3)
        self.verticalLayoutWidget_50.setObjectName(u"verticalLayoutWidget_50")
        self.verticalLayoutWidget_50.setGeometry(QRect(680, 345, 16, 21))
        self.AS5 = QVBoxLayout(self.verticalLayoutWidget_50)
        self.AS5.setObjectName(u"AS5")
        self.AS5.setContentsMargins(0, 0, 0, 0)
        self.AS_5 = QWidget(self.verticalLayoutWidget_50)
        self.AS_5.setObjectName(u"AS_5")
        self.AS_5.setStyleSheet(u"QFrame{\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 0, 0);\n"
"}")

        self.AS5.addWidget(self.AS_5)

        self.verticalLayoutWidget_51 = QWidget(self.page_3)
        self.verticalLayoutWidget_51.setObjectName(u"verticalLayoutWidget_51")
        self.verticalLayoutWidget_51.setGeometry(QRect(120, 345, 16, 21))
        self.CAN1 = QVBoxLayout(self.verticalLayoutWidget_51)
        self.CAN1.setObjectName(u"CAN1")
        self.CAN1.setContentsMargins(0, 0, 0, 0)
        self.CAN_1 = QWidget(self.verticalLayoutWidget_51)
        self.CAN_1.setObjectName(u"CAN_1")
        self.CAN_1.setStyleSheet(u"QFrame{\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 0, 0);\n"
"}")

        self.CAN1.addWidget(self.CAN_1)

        self.verticalLayoutWidget_52 = QWidget(self.page_3)
        self.verticalLayoutWidget_52.setObjectName(u"verticalLayoutWidget_52")
        self.verticalLayoutWidget_52.setGeometry(QRect(150, 345, 16, 21))
        self.CAN2 = QVBoxLayout(self.verticalLayoutWidget_52)
        self.CAN2.setObjectName(u"CAN2")
        self.CAN2.setContentsMargins(0, 0, 0, 0)
        self.CAN_2 = QWidget(self.verticalLayoutWidget_52)
        self.CAN_2.setObjectName(u"CAN_2")
        self.CAN_2.setStyleSheet(u"QFrame{\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 0, 0);\n"
"}")

        self.CAN2.addWidget(self.CAN_2)

        self.verticalLayoutWidget_53 = QWidget(self.page_3)
        self.verticalLayoutWidget_53.setObjectName(u"verticalLayoutWidget_53")
        self.verticalLayoutWidget_53.setGeometry(QRect(180, 345, 16, 21))
        self.CAN3 = QVBoxLayout(self.verticalLayoutWidget_53)
        self.CAN3.setObjectName(u"CAN3")
        self.CAN3.setContentsMargins(0, 0, 0, 0)
        self.CAN_3 = QWidget(self.verticalLayoutWidget_53)
        self.CAN_3.setObjectName(u"CAN_3")
        self.CAN_3.setStyleSheet(u"QFrame{\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 0, 0);\n"
"}")

        self.CAN3.addWidget(self.CAN_3)

        self.verticalLayoutWidget_54 = QWidget(self.page_3)
        self.verticalLayoutWidget_54.setObjectName(u"verticalLayoutWidget_54")
        self.verticalLayoutWidget_54.setGeometry(QRect(210, 345, 16, 21))
        self.CAN4 = QVBoxLayout(self.verticalLayoutWidget_54)
        self.CAN4.setObjectName(u"CAN4")
        self.CAN4.setContentsMargins(0, 0, 0, 0)
        self.CAN_4 = QWidget(self.verticalLayoutWidget_54)
        self.CAN_4.setObjectName(u"CAN_4")
        self.CAN_4.setStyleSheet(u"QFrame{\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 0, 0);\n"
"}")

        self.CAN4.addWidget(self.CAN_4)

        self.verticalLayoutWidget_55 = QWidget(self.page_3)
        self.verticalLayoutWidget_55.setObjectName(u"verticalLayoutWidget_55")
        self.verticalLayoutWidget_55.setGeometry(QRect(240, 345, 16, 21))
        self.CAN5 = QVBoxLayout(self.verticalLayoutWidget_55)
        self.CAN5.setObjectName(u"CAN5")
        self.CAN5.setContentsMargins(0, 0, 0, 0)
        self.CAN_5 = QWidget(self.verticalLayoutWidget_55)
        self.CAN_5.setObjectName(u"CAN_5")
        self.CAN_5.setStyleSheet(u"QFrame{\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 0, 0);\n"
"}")

        self.CAN5.addWidget(self.CAN_5)

        self.verticalLayoutWidget_56 = QWidget(self.page_3)
        self.verticalLayoutWidget_56.setObjectName(u"verticalLayoutWidget_56")
        self.verticalLayoutWidget_56.setGeometry(QRect(270, 345, 16, 21))
        self.CAN6 = QVBoxLayout(self.verticalLayoutWidget_56)
        self.CAN6.setObjectName(u"CAN6")
        self.CAN6.setContentsMargins(0, 0, 0, 0)
        self.CAN_6 = QWidget(self.verticalLayoutWidget_56)
        self.CAN_6.setObjectName(u"CAN_6")
        self.CAN_6.setStyleSheet(u"QFrame{\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 0, 0);\n"
"}")

        self.CAN6.addWidget(self.CAN_6)

        self.verticalLayoutWidget_57 = QWidget(self.page_3)
        self.verticalLayoutWidget_57.setObjectName(u"verticalLayoutWidget_57")
        self.verticalLayoutWidget_57.setGeometry(QRect(300, 345, 16, 21))
        self.CAN7 = QVBoxLayout(self.verticalLayoutWidget_57)
        self.CAN7.setObjectName(u"CAN7")
        self.CAN7.setContentsMargins(0, 0, 0, 0)
        self.CAN_7 = QWidget(self.verticalLayoutWidget_57)
        self.CAN_7.setObjectName(u"CAN_7")
        self.CAN_7.setStyleSheet(u"QFrame{\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 0, 0);\n"
"}")

        self.CAN7.addWidget(self.CAN_7)

        self.verticalLayoutWidget_58 = QWidget(self.page_3)
        self.verticalLayoutWidget_58.setObjectName(u"verticalLayoutWidget_58")
        self.verticalLayoutWidget_58.setGeometry(QRect(330, 345, 16, 21))
        self.CAN8 = QVBoxLayout(self.verticalLayoutWidget_58)
        self.CAN8.setObjectName(u"CAN1_8")
        self.CAN8.setContentsMargins(0, 0, 0, 0)
        self.CAN_8 = QWidget(self.verticalLayoutWidget_58)
        self.CAN_8.setObjectName(u"CAN_8")
        self.CAN_8.setStyleSheet(u"QFrame{\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 0, 0);\n"
"}")

        self.CAN8.addWidget(self.CAN_8)

        self.stackedWidget.addWidget(self.page_3)
        
        self.graphicsView_9.raise_()
        self.graphicsView_10.raise_()

        self.motorLabel_1.raise_()
        self.motorLabel_2.raise_()
        self.motorLabel_3.raise_()
        self.motorLabel_4.raise_()
        self.motorLabel_5.raise_()
        self.motorLabel_6.raise_()
        self.motorLabel_7.raise_()
        self.motorLabel_8.raise_()
        self.motorLabel_9.raise_()
        self.motorLabel_10.raise_()
        self.motorLabel_11.raise_()
        self.motorLabel_12.raise_()
        self.motorLabel_13.raise_()
        
        self.sensorLabel_1.raise_()
        self.sensorLabel_2.raise_()
        self.sensorLabel_3.raise_()
        self.sensorLabel_4.raise_()
        self.sensorLabel_5.raise_()
        self.sensorLabel_6.raise_()
        self.sensorLabel_7.raise_()
        self.sensorLabel_8.raise_()
        self.sensorLabel_9.raise_()
        self.sensorLabel_10.raise_()
        self.sensorLabel_11.raise_()
        self.sensorLabel_12.raise_()
        self.sensorLabel_13.raise_()
        self.sensorLabel_14.raise_()
        self.motorLabel_14.raise_()
        self.sensorLabel_15.raise_()
        self.sensorLabel_16.raise_()
        self.sensorLabel_17.raise_()

        self.canOpenLabel_1.raise_()
        self.canOpenLabel_2.raise_()
        self.canOpenLabel_3.raise_()
        self.canOpenLabel_4.raise_()
        self.canOpenLabel_5.raise_()
        self.canOpenLabel_6.raise_()
        self.canOpenLabel_7.raise_()
        self.canOpenLabel_8.raise_()
        self.canOpenLabel_9.raise_()

        self.verticalLayoutWidget_20.raise_()
        self.verticalLayoutWidget_21.raise_()
        self.verticalLayoutWidget_22.raise_()
        self.verticalLayoutWidget_23.raise_()
        self.verticalLayoutWidget_24.raise_()
        self.verticalLayoutWidget_25.raise_()
        self.verticalLayoutWidget_26.raise_()
        self.verticalLayoutWidget_27.raise_()
        self.verticalLayoutWidget_28.raise_()
        self.verticalLayoutWidget_29.raise_()
        self.verticalLayoutWidget_30.raise_()
        self.verticalLayoutWidget_31.raise_()
        self.verticalLayoutWidget_32.raise_()
        self.verticalLayoutWidget_33.raise_()
        self.verticalLayoutWidget_34.raise_()
        self.verticalLayoutWidget_35.raise_()
        self.verticalLayoutWidget_36.raise_()
        self.verticalLayoutWidget_37.raise_()
        self.verticalLayoutWidget_38.raise_()
        self.verticalLayoutWidget_39.raise_()
        self.verticalLayoutWidget_40.raise_()
        self.verticalLayoutWidget_41.raise_()
        self.verticalLayoutWidget_42.raise_()
        self.verticalLayoutWidget_43.raise_()
        self.verticalLayoutWidget_44.raise_()
        self.verticalLayoutWidget_45.raise_()
        self.verticalLayoutWidget_46.raise_()
        self.verticalLayoutWidget_47.raise_()
        self.verticalLayoutWidget_48.raise_()
        self.verticalLayoutWidget_49.raise_()
        self.verticalLayoutWidget_50.raise_()
        self.verticalLayoutWidget_51.raise_()
        self.verticalLayoutWidget_52.raise_()
        self.verticalLayoutWidget_53.raise_()
        self.verticalLayoutWidget_54.raise_()
        self.verticalLayoutWidget_55.raise_()
        self.verticalLayoutWidget_56.raise_()
        self.verticalLayoutWidget_57.raise_()
        self.verticalLayoutWidget_58.raise_()
         
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.verticalLayout_2 = QVBoxLayout(self.page_4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.camWidget = QTabWidget(self.page_4)
        self.camWidget.setObjectName(u"camWidget")
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(True)
        font1.setWeight(75)
        self.camWidget.setFont(font1)
        self.camera_1 = QWidget()
        self.camera_1.setObjectName(u"camera_1")
        self.camera_1.setEnabled(True)
        self.c1Label = QLabel(self.camera_1)
        self.c1Label.setObjectName(u"c1Label")
        self.c1Label.setGeometry(QRect(10, 10, 721, 321))
        self.camWidget.addTab(self.camera_1, "")
        self.camera_2 = QWidget()
        self.camera_2.setObjectName(u"camera_2")
        self.c2Label = QLabel(self.camera_2)
        self.c2Label.setObjectName(u"c2Label")
        self.c2Label.setGeometry(QRect(10, 10, 721, 321))
        self.camWidget.addTab(self.camera_2, "")

        self.verticalLayout_2.addWidget(self.camWidget)

        self.stackedWidget.addWidget(self.page_4)
        
        self.verticalLayout_3.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.frame)

        Controller.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(Controller)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 800, 21))
        font = QFont()
        font.setPointSize(17)
        self.menuBar.setFont(font)
        self.menuController = QMenu(self.menuBar)
        self.menuController.setObjectName(u"menuController")
        self.menuSettings = QMenu(self.menuBar)
        self.menuSettings.setObjectName(u"menuSettings")
        self.menuHelp = QMenu(self.menuBar)
        self.menuHelp.setObjectName(u"menuHelp")
        self.menuPower = QMenu(self.menuBar)
        self.menuPower.setObjectName(u"menuPower")
        Controller.setMenuBar(self.menuBar)
        
        self.statusBar = QStatusBar(Controller)
        self.statusBar.setObjectName(u"statusBar")
        Controller.setStatusBar(self.statusBar)

        self.menuBar.addAction(self.menuPower.menuAction())
        self.menuBar.addAction(self.menuController.menuAction())
        self.menuBar.addAction(self.menuSettings.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())
        self.menuController.addAction(self.actionController)
        self.menuController.addAction(self.actionDisplay)
        self.menuController.addAction(self.actionSensors)
        self.menuController.addAction(self.actionCamera)
        self.menuSettings.addAction(self.actionConnect)
        self.menuSettings.addAction(self.actionSpeed)
        self.menuPower.addAction(self.actionShutdown)
        self.menuHelp.addAction(self.actionAbout)
        self.retranslateUi(Controller)

        self.stackedWidget.setCurrentIndex(0)
        self.camWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Controller)
    # setupUi
    
    def showAbout(self):
        about = QMessageBox()
        about.setWindowIcon(QIcon('/home/grips/canBus/Icon/about.png'))
        about.setText('Controller v2.0')
        about.setWindowTitle('About')
        about.setIcon(QMessageBox.Information)
        about.setInformativeText('\nCopyright GriPS Automation \nAll rights reserved')
        about.setDetailedText('For information about this application Contact:\n' +
        'Help Desk\n' 
        'Phone: +49 (89) 452 15 88-0\n' 
        'Email: office@grips-automation.com')
        about.setStandardButtons(QMessageBox.Ok)
        about.exec_()

    def showError(self):
        error = QMessageBox()
        error.setText('Controller v1.0')
        error.setWindowTitle('Error')
        error.setIcon(QMessageBox.Warning)
        error.setInformativeText('\nServer not running : Invalid IP Address')
        error.exec_()
        
    def showCanError(self):
        error = QMessageBox()
        error.setText('Controller v1.0')
        error.setWindowTitle('Error')
        error.setIcon(QMessageBox.Critical)
        error.setInformativeText('\nCannot Send Can Data')
        error.exec_()
        
    def retranslateUi(self, Controller):
        Controller.setWindowTitle(QCoreApplication.translate("Controller", u"Controller App", None))
        self.actionController.setText(QCoreApplication.translate("Controller", u"Controller", None))
        self.actionCamera.setText(QCoreApplication.translate("Controller", u"Camera", None))
        self.actionSensors.setText(QCoreApplication.translate("Controller", u"Sensors", None))
        self.actionDisplay.setText(QCoreApplication.translate("Controller", u"Display", None))
        self.actionShutdown.setText(QCoreApplication.translate("Controller", u"Shutdown", None))
        self.actionConnect.setText(QCoreApplication.translate("Controller", u"Connect", None))
        self.actionSpeed.setText(QCoreApplication.translate("Controller", u"Speed", None))
        self.actionAbout.setText(QCoreApplication.translate("Controller", u"About...", None))
        self.menuController.setTitle(QCoreApplication.translate("Controller", u"Scenes", None))
        self.menuSettings.setTitle(QCoreApplication.translate("Controller", u"Settings", None))
        self.menuHelp.setTitle(QCoreApplication.translate("Controller", u"Help", None))
        self.menuPower.setTitle(QCoreApplication.translate("Controller", u"Power", None))
        self.connectionLabel.setText(QCoreApplication.translate("Controller", u"<html><head/><body><p><span style=\" color:#aa0000;\">Disconnected</span></p></body></html>", None))
        self.speedLabel2.setText(QCoreApplication.translate("Controller", u"<html><head/><body><p><span style=\" color:#000000;\">Speed</span></p></body></html>", None))
        self.systemONLabel.setText(QCoreApplication.translate("Controller", u"<html><head/><body><p><span style=\" color:#000000;\">System ON</span></p></body></html>", None))
        self.systemOFFLabel.setText(QCoreApplication.translate("Controller", u"<html><head/><body><p><span style=\" color:#000000;\">System OFF</span></p></body></html>", None))
        self.speedLabel1.setText(QCoreApplication.translate("Controller", u"<html><head/><body><p><span style=\" color:#000000;\">Speed</span></p></body></html>", None))
        self.rotateLabel.setText(QCoreApplication.translate("Controller", u"<html><head/><body><p><span style=\" color:#000000;\">Rotate</span></p></body></html>", None))
        self.startPickLabel.setText(QCoreApplication.translate("Controller", u"<html><head/><body><p><span style=\" color:#000000;\">Start Pick</span></p></body></html>", None))
        self.startDropLabel.setText(QCoreApplication.translate("Controller", u"<html><head/><body><p><span style=\" color:#000000;\">Start Drop</span></p></body></html>", None))
        self.forward.setText(QCoreApplication.translate("Controller", u"<html><head/><body><p><span style=\" color:#000000;\">Forward</span></p></body></html>", None))
        self.reverseLabel.setText(QCoreApplication.translate("Controller", u"<html><head/><body><p><span style=\" color:#000000;\">Reverse</span></p></body></html>", None))
        self.leftLabel.setText(QCoreApplication.translate("Controller", u"<html><head/><body><p><span style=\" color:#000000;\">Left</span></p></body></html>", None))
        self.rightLabel.setText(QCoreApplication.translate("Controller", u"<html><head/><body><p><span style=\" color:#000000;\">Right</span></p></body></html>", None))

        self.motorLabel_1.setText(QCoreApplication.translate("Controller", u"<html><head/><body><p><span style=\" color:#000000;\">BM1 -  Brushless Motor 1 - AGV motion</span></p></body></html>", None))
        self.motorLabel_2.setText(QCoreApplication.translate("Controller", u"<html><head/><body><p><span style=\" color:#000000;\">BM2 -  Brushless Motor 2 - AGV motion</span></p></body></html>", None))
        self.motorLabel_3.setText(QCoreApplication.translate("Controller", u"<html><head/><body><p><span style=\" color:#000000;\">BM3 -  Brushless Motor 3 - AGV motion</span></p></body></html>", None))
        self.motorLabel_4.setText(QCoreApplication.translate("Controller", u"<html><head/><body><p><span style=\" color:#000000;\">BM4 -  Brushless Motor 4 - AGV motion</span></p></body></html>", None))
        self.motorLabel_5.setText(QCoreApplication.translate("Controller", u"<html><head/><body><p><span style=\" color:#000000;\">BM5 -  Brushless Motor 1 - Gripper Motion</span></p></body></html>", None))
        self.motorLabel_6.setText(QCoreApplication.translate("Controller", u"<html><head/><body><p><span style=\" color:#000000;\">BM6 -  Brushless Motor 2 - Gripper Motion</span></p></body></html>", None))
        self.motorLabel_7.setText(QCoreApplication.translate("Controller", u"<html><head/><body><p><span style=\" color:#000000;\">BM7 -  Brushless Motor 3 - Gripper Motion</span></p></body></html>", None))
        self.motorLabel_8.setText(QCoreApplication.translate("Controller", u"<html><head/><body><p><span style=\" color:#000000;\">BM8 -  Brushless Motor 4 - Gripper Motion</span></p></body></html>", None))
        self.motorLabel_9.setText(QCoreApplication.translate("Controller", u"<html><head/><body><p><span style=\" color:#000000;\">SM1 - Stepper Motor 1 - Gripper</span></p></body></html>", None))
        self.motorLabel_10.setText(QCoreApplication.translate("Controller", u"<html><head/><body><p><span style=\" color:#000000;\">SM2 - Stepper Motor 2 - Gripper</span></p></body></html>", None))
        self.motorLabel_11.setText(QCoreApplication.translate("Controller", u"<html><head/><body><p><span style=\" color:#000000;\">SM3 - Stepper Motor 3 - Gripper</span></p></body></html>", None))
        self.motorLabel_12.setText(QCoreApplication.translate("Controller", u"<html><head/><body><p><span style=\" color:#000000;\">SM4 - Stepper Motor 4 - Gripper</span></p></body></html>", None))
        self.motorLabel_13.setText(QCoreApplication.translate("Controller", u"<html><head/><body><p><span style=\" color:#000000;\">AM1 - Alternating Current Motor - Lift Up</span></p></body></html>", None))
        self.motorLabel_14.setText(QCoreApplication.translate("Controller", u"<html><head/><body><p><span style=\" color:#000000;\">PV1 - Pneumatic Value - Lift Down</span></p></body></html>", None))
        
        self.sensorLabel_1.setText(QCoreApplication.translate("Controller", u"<html><head/><body><p><span style=\" color:#000000;\">DS1 - Digital Sensor 1 - Arm Retracted</span></p></body></html>", None))
        self.sensorLabel_2.setText(QCoreApplication.translate("Controller", u"<html><head/><body><p><span style=\" color:#000000;\">DS2 - Digital Sensor 2 - Arm Retracted</span></p></body></html>", None))
        self.sensorLabel_3.setText(QCoreApplication.translate("Controller", u"<html><head/><body><p><span style=\" color:#000000;\">DS3 - Digital Sensor 3 - Arm Retracted</span></p></body></html>", None))
        self.sensorLabel_4.setText(QCoreApplication.translate("Controller", u"<html><head/><body><p><span style=\" color:#000000;\">DS4 - Digital Sensor 4 - Arm Retracted</span></p></body></html>", None))
        self.sensorLabel_5.setText(QCoreApplication.translate("Controller", u"<html><head/><body><p><span style=\" color:#000000;\">DS5 - Digital Sensor 5 - Arm Extended</span></p></body></html>", None))
        self.sensorLabel_6.setText(QCoreApplication.translate("Controller", u"<html><head/><body><p><span style=\" color:#000000;\">DS6 - Digital Sensor 6 - Arm Extended</span></p></body></html>", None))
        self.sensorLabel_7.setText(QCoreApplication.translate("Controller", u"<html><head/><body><p><span style=\" color:#000000;\">DS7 - Digital Sensor 7 - Arm Extended</span></p></body></html>", None))
        self.sensorLabel_8.setText(QCoreApplication.translate("Controller", u"<html><head/><body><p><span style=\" color:#000000;\">DS8 - Digital Sensor 8 - Arm Extended</span></p></body></html>", None))
        self.sensorLabel_9.setText(QCoreApplication.translate("Controller", u"<html><head/><body><p><span style=\" color:#000000;\">DS9 - Digital Sensor 9 - Gripper Open</span></p></body></html>", None))
        self.sensorLabel_10.setText(QCoreApplication.translate("Controller", u"<html><head/><body><p><span style=\" color:#000000;\">DS10 - Digital Sensor 10 - Gripper Open</span></p></body></html>", None))
        self.sensorLabel_11.setText(QCoreApplication.translate("Controller", u"<html><head/><body><p><span style=\" color:#000000;\">DS11 - Digital Sensor 11 - Gripper Open</span></p></body></html>", None))
        self.sensorLabel_12.setText(QCoreApplication.translate("Controller", u"<html><head/><body><p><span style=\" color:#000000;\">DS12 - Digital Sensor 12 - Gripper Open</span></p></body></html>", None))
        self.sensorLabel_13.setText(QCoreApplication.translate("Controller", u"<html><head/><body><p><span style=\" color:#000000;\">AS1 - Analog Sensor 1 - Pipe Center</span></p></body></html>", None))
        self.sensorLabel_14.setText(QCoreApplication.translate("Controller", u"<html><head/><body><p><span style=\" color:#000000;\">AS2 - Analog Sensor 2 - Pipe Center</span></p></body></html>", None))
        self.sensorLabel_15.setText(QCoreApplication.translate("Controller", u"<html><head/><body><p><span style=\" color:#000000;\">AS3 - Analog Sensor 3 - Pipe Center</span></p></body></html>", None))
        self.sensorLabel_16.setText(QCoreApplication.translate("Controller", u"<html><head/><body><p><span style=\" color:#000000;\">AS4 - Analog Sensor 4 - Pipe Center</span></p></body></html>", None))
        self.sensorLabel_17.setText(QCoreApplication.translate("Controller", u"<html><head/><body><p><span style=\" color:#000000;\">AS5 - Analog Sensor 5 - Lift Limit</span></p></body></html>", None))
        
        self.canOpenLabel_1.setText(QCoreApplication.translate("Controller", u"<html><head/><body><p><span style=\" color:#000000;\">CANopen COM</span></p></body></html>", None))
        self.canOpenLabel_2.setText(QCoreApplication.translate("Controller", u"<html><head/><body><p><span style=\" color:#000000;\">1</span></p></body></html>", None))
        self.canOpenLabel_3.setText(QCoreApplication.translate("Controller", u"<html><head/><body><p><span style=\" color:#000000;\">2</span></p></body></html>", None))
        self.canOpenLabel_4.setText(QCoreApplication.translate("Controller", u"<html><head/><body><p><span style=\" color:#000000;\">3</span></p></body></html>", None))
        self.canOpenLabel_5.setText(QCoreApplication.translate("Controller", u"<html><head/><body><p><span style=\" color:#000000;\">4</span></p></body></html>", None))
        self.canOpenLabel_6.setText(QCoreApplication.translate("Controller", u"<html><head/><body><p><span style=\" color:#000000;\">5</span></p></body></html>", None))
        self.canOpenLabel_7.setText(QCoreApplication.translate("Controller", u"<html><head/><body><p><span style=\" color:#000000;\">6</span></p></body></html>", None))
        self.canOpenLabel_8.setText(QCoreApplication.translate("Controller", u"<html><head/><body><p><span style=\" color:#000000;\">7</span></p></body></html>", None))
        self.canOpenLabel_9.setText(QCoreApplication.translate("Controller", u"<html><head/><body><p><span style=\" color:#000000;\">8</span></p></body></html>", None))
        
        self.c1Label.setText("")
        self.camWidget.setTabText(self.camWidget.indexOf(self.camera_1), QCoreApplication.translate("Controller", u"Camera 1", None))
        self.c2Label.setText("")
        self.camWidget.setTabText(self.camWidget.indexOf(self.camera_2), QCoreApplication.translate("Controller", u"Camera 2", None))
        
        #self.pushButton.setText(QCoreApplication.translate("Controller", u"Start", None))#Button
    # retranslateUi

class Ui_Settings(object):
    def setupUi(self, Settings):
        if not Settings.objectName():
            Settings.setObjectName(u"Settings")
        Settings.setFixedSize(400, 300)
        Settings.setWindowFlag (QtCore.Qt.WindowStaysOnTopHint, False)
        self.buttonBox = QDialogButtonBox(Settings)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(230, 270, 156, 23))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.speed = QLabel(Settings)
        self.speed.setObjectName(u"speed")
        self.speed.setGeometry(QRect(20, 10, 81, 16))
        self.lcdNumber = QLCDNumber(Settings)
        self.lcdNumber.setObjectName(u"lcdNumber")
        self.lcdNumber.setGeometry(QRect(110, 10, 81, 23))
        self.lcdNumber.setFrameShadow(QFrame.Sunken)
        self.lcdNumber.setLineWidth(1)
        self.horizontalSlider = QSlider(Settings)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setGeometry(QRect(20, 50, 361, 22))
        self.horizontalSlider.setTickPosition(QSlider.TicksBothSides)
        self.horizontalSlider.setMaximum(100)
        self.horizontalSlider.setSingleStep(25)
        self.horizontalSlider.setOrientation(Qt.Horizontal)
        self.Zero = QLabel(Settings)
        self.Zero.setObjectName(u"Zero")
        self.Zero.setGeometry(QRect(20, 70, 47, 13))
        self.Twentyfive = QLabel(Settings)
        self.Twentyfive.setObjectName(u"Twentyfive")
        self.Twentyfive.setGeometry(QRect(108, 70, 47, 13))
        self.Fifty = QLabel(Settings)
        self.Fifty.setObjectName(u"Fifty")
        self.Fifty.setGeometry(QRect(192, 70, 47, 13))
        self.Hundred = QLabel(Settings)
        self.Hundred.setObjectName(u"Hundred")
        self.Hundred.setGeometry(QRect(360, 70, 47, 13))
        self.Seventyfive = QLabel(Settings)
        self.Seventyfive.setObjectName(u"Seventyfive")
        self.Seventyfive.setGeometry(QRect(281, 70, 47, 13))
        self.inButton = QPushButton(Settings)
        self.inButton.setGeometry(QRect(20, 120, 171, 51))
        self.inButton.setIcon(QIcon("/home/grips/canBus/Icon/plus.png"))

        self.deButton = QPushButton(Settings)
        self.deButton.setGeometry(QRect(210, 120, 171, 51))
        self.deButton.setIcon(QIcon("/home/grips/canBus/Icon/minus.png"))
        

        self.retranslateUi(Settings)
        #self.buttonBox.accepted.connect(Settings.accept)
        #self.buttonBox.rejected.connect(Settings.reject)
        self.horizontalSlider.valueChanged.connect(self.lcdNumber.display)
                
        QMetaObject.connectSlotsByName(Settings)
    # setupUi
        
    def retranslateUi(self, Settings):
        Settings.setWindowTitle(QCoreApplication.translate("Settings", u"Settings", None))
        self.speed.setText(QCoreApplication.translate("Settings", u"Speed(U/min)", None))
        self.Zero.setText(QCoreApplication.translate("Settings", u"0", None))
        self.Twentyfive.setText(QCoreApplication.translate("Settings", u"25", None))
        self.Fifty.setText(QCoreApplication.translate("Settings", u"50", None))
        self.Hundred.setText(QCoreApplication.translate("Settings", u"100", None))
        self.Seventyfive.setText(QCoreApplication.translate("Settings", u"75", None))
    # retranslateUi

class Ui_Connection_Server(object):
    def setupUi(self, Connection):
        if not Connection.objectName():
            Connection.setObjectName(u"Connection")
        Connection.setFixedSize(403, 191)
        self.buttonBox = QDialogButtonBox(Connection)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(50, 150, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.graphicsView_7 = QGraphicsView(Connection)
        self.graphicsView_7.setObjectName(u"graphicsView_7")
        self.graphicsView_7.setGeometry(QRect(10, 80, 381, 51))
        self.graphicsView_7.setStyleSheet(u"QFrame{\n"
"border-radius: 5px;\n"
"background-color: rgb(211, 211, 211);\n"
"}")
        self.verticalLayoutWidget = QWidget(Connection)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget_18")
        self.verticalLayoutWidget.setGeometry(QRect(22, 86, 25, 31))
        self.ConnectionLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.ConnectionLayout.setObjectName(u"ConnectionLayout")
        self.ConnectionLayout.setContentsMargins(0, 0, 0, 0)
        self.Connection_A = QWidget(self.verticalLayoutWidget)
        self.Connection_A.setObjectName(u"Connection_A")
        self.Connection_A.setStyleSheet(u"QFrame{\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 0, 0);\n"
"}")

        self.ConnectionLayout.addWidget(self.Connection_A)

        self.connection_label = QLabel(Connection)
        self.connection_label.setObjectName(u"connection_label")
        self.connection_label.setGeometry(QRect(60, 90, 160, 31))
        font = QFont()
        font.setFamily(u"MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.connection_label.setFont(font)
        self.status = QLabel(Connection)
        self.status.setObjectName(u"status")
        self.status.setGeometry(QRect(220, 90, 160, 31))
        font1 = QFont()
        font1.setPointSize(15)
        font1.setBold(True)
        font1.setWeight(75)
        self.status.setFont(font1)
        self.status.setStyleSheet(u"")
        self.status.setTextFormat(Qt.AutoText)
        self.connect = QPushButton(Connection)
        self.connect.setObjectName(u"connect")
        self.connect.setGeometry(QRect(10, 20, 181, 51))
        self.connect.setMinimumSize(QSize(181, 51))
        self.connect.setMaximumSize(QSize(181, 51))
        font2 = QFont()
        font2.setPointSize(12)
        self.connect.setFont(font2)
        self.disconnect = QPushButton(Connection)
        self.disconnect.setObjectName(u"disconnect")
        self.disconnect.setGeometry(QRect(210, 20, 181, 51))
        self.disconnect.setMinimumSize(QSize(181, 51))
        self.disconnect.setMaximumSize(QSize(181, 51))
        self.disconnect.setFont(font2)

        self.retranslateUi(Connection)
        #self.buttonBox.accepted.connect(Connection.accept)
        #self.buttonBox.rejected.connect(Connection.reject)

        QMetaObject.connectSlotsByName(Connection)
    # setupUi

    def retranslateUi(self, Connection):
        Connection.setWindowTitle(QCoreApplication.translate("Connection", u"Thread Connection", None))
        self.connection_label.setText(QCoreApplication.translate("Connection", u"Connection Status :", None))
        self.status.setText(QCoreApplication.translate("Connection", u"<html><head/><body><p><span style=\" color:#aa0000;\">Disconnected</span></p></body></html>", None))
        self.connect.setText(QCoreApplication.translate("Connection", u"Connect", None))
        self.disconnect.setText(QCoreApplication.translate("Connection", u"Disconnect", None))
    # retranslateUi

class Ui_Connection_Client(object):
    def setupUi(self, Connection):
        if not Connection.objectName():
            Connection.setObjectName(u"Connection")
        Connection.resize(403, 231)
        self.buttonBox = QDialogButtonBox(Connection)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(50, 190, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.graphicsView_7 = QGraphicsView(Connection)
        self.graphicsView_7.setObjectName(u"graphicsView_7")
        self.graphicsView_7.setGeometry(QRect(10, 120, 381, 51))
        self.graphicsView_7.setStyleSheet(u"QFrame{\n"
"border-radius: 5px;\n"
"background-color: rgb(211, 211, 211);\n"
"}")
        self.verticalLayoutWidget_18 = QWidget(Connection)
        self.verticalLayoutWidget_18.setObjectName(u"verticalLayoutWidget_18")
        self.verticalLayoutWidget_18.setGeometry(QRect(22, 126, 25, 31))
        self.ConnectionLayout = QVBoxLayout(self.verticalLayoutWidget_18)
        self.ConnectionLayout.setObjectName(u"ConnectionLayout")
        self.ConnectionLayout.setContentsMargins(0, 0, 0, 0)
        self.Connection_A = QWidget(self.verticalLayoutWidget_18)
        self.Connection_A.setObjectName(u"Connection_A")
        self.Connection_A.setStyleSheet(u"QFrame{\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 0, 0);\n"
"}")

        self.ConnectionLayout.addWidget(self.Connection_A)

        self.connection_label = QLabel(Connection)
        self.connection_label.setObjectName(u"connection_label")
        self.connection_label.setGeometry(QRect(60, 130, 160, 31))
        font = QFont()
        font.setFamily(u"MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.connection_label.setFont(font)
        self.status = QLabel(Connection)
        self.status.setObjectName(u"status")
        self.status.setGeometry(QRect(220, 130, 160, 31))
        font1 = QFont()
        font1.setPointSize(15)
        font1.setBold(True)
        font1.setWeight(75)
        self.status.setFont(font1)
        self.status.setStyleSheet(u"")
        self.status.setTextFormat(Qt.AutoText)
        self.connect = QPushButton(Connection)
        self.connect.setObjectName(u"connect")
        self.connect.setGeometry(QRect(10, 60, 181, 51))
        font2 = QFont()
        font2.setPointSize(12)
        self.connect.setFont(font2)
        self.disconnect = QPushButton(Connection)
        self.disconnect.setObjectName(u"disconnect")
        self.disconnect.setGeometry(QRect(210, 60, 181, 51))
        self.disconnect.setFont(font2)
        self.comboBox = QComboBox(Connection)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(150, 21, 241, 21))
        font3 = QFont()
        font3.setPointSize(14)
        self.comboBox.setFont(font3)
        self.comboBox.setLayoutDirection(Qt.RightToLeft)
        self.label = QLabel(Connection)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 121, 21))
        font4 = QFont()
        font4.setPointSize(13)
        self.label.setFont(font4)

        self.retranslateUi(Connection)
        #self.buttonBox.accepted.connect(Connection.accept)
        #self.buttonBox.rejected.connect(Connection.reject)

        QMetaObject.connectSlotsByName(Connection)
    # setupUi

    def retranslateUi(self, Connection):
        Connection.setWindowTitle(QCoreApplication.translate("Connection", u"Dialog", None))
        self.connection_label.setText(QCoreApplication.translate("Connection", u"Connection Status :", None))
        self.status.setText(QCoreApplication.translate("Connection", u"<html><head/><body><p><span style=\" color:#aa0000;\">Disconnected</span></p></body></html>", None))
        self.connect.setText(QCoreApplication.translate("Connection", u"Connect", None))
        self.disconnect.setText(QCoreApplication.translate("Connection", u"Disconnect", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Connection", u"192.168.1.151", u"AGV-1"))
        self.comboBox.setItemText(1, QCoreApplication.translate("Connection", u"192.168.1.152", u"AGV-2"))
        self.comboBox.setItemText(2, QCoreApplication.translate("Connection", u"192.168.1.153", u"AGV-3"))
        self.comboBox.setItemText(3, QCoreApplication.translate("Connection", u"192.168.1.154", u"AGV-4"))

        self.comboBox.setPlaceholderText("")
        self.label.setText(QCoreApplication.translate("Connection", u"Select AGV:", None))
    # retranslateUi