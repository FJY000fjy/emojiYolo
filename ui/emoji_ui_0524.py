# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'emoji_0524.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1456, 646)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.media = QtWidgets.QLabel(self.centralwidget)
        self.media.setGeometry(QtCore.QRect(10, 10, 821, 551))
        self.media.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.media.setObjectName("media")
        self.emoji = QtWidgets.QLabel(self.centralwidget)
        self.emoji.setGeometry(QtCore.QRect(840, 10, 601, 551))
        self.emoji.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.emoji.setObjectName("emoji")
        self.increase_conf = QtWidgets.QPushButton(self.centralwidget)
        self.increase_conf.setGeometry(QtCore.QRect(1160, 570, 141, 31))
        self.increase_conf.setObjectName("increase_conf")
        self.decrease_conf = QtWidgets.QPushButton(self.centralwidget)
        self.decrease_conf.setGeometry(QtCore.QRect(1160, 600, 141, 31))
        self.decrease_conf.setObjectName("decrease_conf")
        self.increase_iou = QtWidgets.QPushButton(self.centralwidget)
        self.increase_iou.setGeometry(QtCore.QRect(1300, 570, 141, 31))
        self.increase_iou.setObjectName("increase_iou")
        self.decrease_iou = QtWidgets.QPushButton(self.centralwidget)
        self.decrease_iou.setGeometry(QtCore.QRect(1300, 600, 141, 31))
        self.decrease_iou.setObjectName("decrease_iou")
        self.get_weight = QtWidgets.QPushButton(self.centralwidget)
        self.get_weight.setGeometry(QtCore.QRect(20, 570, 171, 61))
        self.get_weight.setObjectName("get_weight")
        self.video = QtWidgets.QPushButton(self.centralwidget)
        self.video.setGeometry(QtCore.QRect(600, 570, 181, 61))
        self.video.setObjectName("video")
        self.init_model = QtWidgets.QPushButton(self.centralwidget)
        self.init_model.setGeometry(QtCore.QRect(200, 570, 201, 61))
        self.init_model.setObjectName("init_model")
        self.picture = QtWidgets.QPushButton(self.centralwidget)
        self.picture.setGeometry(QtCore.QRect(410, 570, 181, 61))
        self.picture.setObjectName("picture")
        self.camera = QtWidgets.QPushButton(self.centralwidget)
        self.camera.setGeometry(QtCore.QRect(790, 570, 201, 61))
        self.camera.setObjectName("camera")
        self.see_history = QtWidgets.QPushButton(self.centralwidget)
        self.see_history.setGeometry(QtCore.QRect(1010, 570, 141, 61))
        self.see_history.setObjectName("see_history")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "emojiAI"))
        self.media.setText(_translate("MainWindow", "media"))
        self.emoji.setText(_translate("MainWindow", "emoji"))
        self.increase_conf.setText(_translate("MainWindow", "increase confidence"))
        self.decrease_conf.setText(_translate("MainWindow", "decrease confidence"))
        self.increase_iou.setText(_translate("MainWindow", "increase IoU"))
        self.decrease_iou.setText(_translate("MainWindow", "decrease IoU"))
        self.get_weight.setText(_translate("MainWindow", "Selected weight"))
        self.video.setText(_translate("MainWindow", "Detect video"))
        self.init_model.setText(_translate("MainWindow", "weight Model initialization"))
        self.picture.setText(_translate("MainWindow", "Detect pictures"))
        self.camera.setText(_translate("MainWindow", "camera detection"))
        self.see_history.setText(_translate("MainWindow", "history"))
