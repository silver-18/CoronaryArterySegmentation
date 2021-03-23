# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwidget.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWidget(object):
    def setupUi(self, MainWidget):
        MainWidget.setObjectName("MainWidget")
        MainWidget.resize(1920, 1080)
        MainWidget.setMinimumSize(QtCore.QSize(1024, 768))
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(MainWidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.groupBox = QtWidgets.QGroupBox(MainWidget)
        self.groupBox.setMinimumSize(QtCore.QSize(500, 0))
        self.groupBox.setMaximumSize(QtCore.QSize(500, 16777215))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.LoadData = QtWidgets.QPushButton(self.groupBox)
        self.LoadData.setMinimumSize(QtCore.QSize(300, 50))
        self.LoadData.setObjectName("LoadData")
        self.verticalLayout_2.addWidget(self.LoadData)
        self.ImagePath = QtWidgets.QLabel(self.groupBox)
        self.ImagePath.setMaximumSize(QtCore.QSize(16777215, 100))
        self.ImagePath.setAlignment(QtCore.Qt.AlignCenter)
        self.ImagePath.setWordWrap(True)
        self.ImagePath.setObjectName("ImagePath")
        self.verticalLayout_2.addWidget(self.ImagePath)
        self.BackgroundPath = QtWidgets.QLabel(self.groupBox)
        self.BackgroundPath.setMaximumSize(QtCore.QSize(16777215, 100))
        self.BackgroundPath.setAlignment(QtCore.Qt.AlignCenter)
        self.BackgroundPath.setObjectName("BackgroundPath")
        self.verticalLayout_2.addWidget(self.BackgroundPath)
        self.LabelPath = QtWidgets.QLabel(self.groupBox)
        self.LabelPath.setMaximumSize(QtCore.QSize(16777215, 100))
        self.LabelPath.setAlignment(QtCore.Qt.AlignCenter)
        self.LabelPath.setWordWrap(True)
        self.LabelPath.setObjectName("LabelPath")
        self.verticalLayout_2.addWidget(self.LabelPath)
        self.groupBoxXYZ = QtWidgets.QGroupBox(self.groupBox)
        self.groupBoxXYZ.setMaximumSize(QtCore.QSize(16777215, 100))
        self.groupBoxXYZ.setTitle("")
        self.groupBoxXYZ.setObjectName("groupBoxXYZ")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBoxXYZ)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.LabelX = QtWidgets.QLabel(self.groupBoxXYZ)
        self.LabelX.setScaledContents(True)
        self.LabelX.setAlignment(QtCore.Qt.AlignCenter)
        self.LabelX.setObjectName("LabelX")
        self.horizontalLayout.addWidget(self.LabelX)
        self.LabelValueX = QtWidgets.QLabel(self.groupBoxXYZ)
        self.LabelValueX.setText("")
        self.LabelValueX.setScaledContents(True)
        self.LabelValueX.setAlignment(QtCore.Qt.AlignCenter)
        self.LabelValueX.setObjectName("LabelValueX")
        self.horizontalLayout.addWidget(self.LabelValueX)
        self.LabelY = QtWidgets.QLabel(self.groupBoxXYZ)
        self.LabelY.setScaledContents(True)
        self.LabelY.setAlignment(QtCore.Qt.AlignCenter)
        self.LabelY.setObjectName("LabelY")
        self.horizontalLayout.addWidget(self.LabelY)
        self.LabelValueY = QtWidgets.QLabel(self.groupBoxXYZ)
        self.LabelValueY.setText("")
        self.LabelValueY.setScaledContents(True)
        self.LabelValueY.setAlignment(QtCore.Qt.AlignCenter)
        self.LabelValueY.setObjectName("LabelValueY")
        self.horizontalLayout.addWidget(self.LabelValueY)
        self.LabelZ = QtWidgets.QLabel(self.groupBoxXYZ)
        self.LabelZ.setScaledContents(True)
        self.LabelZ.setAlignment(QtCore.Qt.AlignCenter)
        self.LabelZ.setObjectName("LabelZ")
        self.horizontalLayout.addWidget(self.LabelZ)
        self.LabelValueZ = QtWidgets.QLabel(self.groupBoxXYZ)
        self.LabelValueZ.setText("")
        self.LabelValueZ.setScaledContents(True)
        self.LabelValueZ.setAlignment(QtCore.Qt.AlignCenter)
        self.LabelValueZ.setObjectName("LabelValueZ")
        self.horizontalLayout.addWidget(self.LabelValueZ)
        self.verticalLayout_2.addWidget(self.groupBoxXYZ)
        self.View3D = QtWidgets.QPushButton(self.groupBox)
        self.View3D.setObjectName("View3D")
        self.verticalLayout_2.addWidget(self.View3D)
        self.ViewSlice = QtWidgets.QPushButton(self.groupBox)
        self.ViewSlice.setObjectName("ViewSlice")
        self.verticalLayout_2.addWidget(self.ViewSlice)
        self.groupBoxView = QtWidgets.QGroupBox(self.groupBox)
        self.groupBoxView.setTitle("")
        self.groupBoxView.setObjectName("groupBoxView")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBoxView)
        self.gridLayout.setObjectName("gridLayout")
        self.HideLabel = QtWidgets.QPushButton(self.groupBoxView)
        self.HideLabel.setObjectName("HideLabel")
        self.gridLayout.addWidget(self.HideLabel, 3, 1, 1, 1)
        self.ShowLabel = QtWidgets.QPushButton(self.groupBoxView)
        self.ShowLabel.setObjectName("ShowLabel")
        self.gridLayout.addWidget(self.ShowLabel, 3, 0, 1, 1)
        self.HidePredict = QtWidgets.QPushButton(self.groupBoxView)
        self.HidePredict.setObjectName("HidePredict")
        self.gridLayout.addWidget(self.HidePredict, 2, 1, 1, 1)
        self.ShowPredict = QtWidgets.QPushButton(self.groupBoxView)
        self.ShowPredict.setObjectName("ShowPredict")
        self.gridLayout.addWidget(self.ShowPredict, 2, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBoxView)
        self.SaveFig = QtWidgets.QPushButton(self.groupBox)
        self.SaveFig.setObjectName("SaveFig")
        self.verticalLayout_2.addWidget(self.SaveFig)
        self.progressBar = QtWidgets.QProgressBar(self.groupBox)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_2.addWidget(self.progressBar)
        self.horizontalLayout_3.addWidget(self.groupBox)
        self.groupBoxMayavi = QtWidgets.QGroupBox(MainWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBoxMayavi.sizePolicy().hasHeightForWidth())
        self.groupBoxMayavi.setSizePolicy(sizePolicy)
        self.groupBoxMayavi.setMinimumSize(QtCore.QSize(700, 700))
        self.groupBoxMayavi.setTitle("")
        self.groupBoxMayavi.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBoxMayavi.setObjectName("groupBoxMayavi")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBoxMayavi)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.horizontalLayout_3.addWidget(self.groupBoxMayavi)

        self.retranslateUi(MainWidget)
        QtCore.QMetaObject.connectSlotsByName(MainWidget)

    def retranslateUi(self, MainWidget):
        _translate = QtCore.QCoreApplication.translate
        MainWidget.setWindowTitle(_translate("MainWidget", "ViewRaw"))
        self.LoadData.setText(_translate("MainWidget", "LoadData"))
        self.ImagePath.setText(_translate("MainWidget", "ImagePath"))
        self.BackgroundPath.setText(_translate("MainWidget", "BackgroundPath"))
        self.LabelPath.setText(_translate("MainWidget", "LabelPath"))
        self.LabelX.setText(_translate("MainWidget", "X:"))
        self.LabelY.setText(_translate("MainWidget", "Y:"))
        self.LabelZ.setText(_translate("MainWidget", "Z:"))
        self.View3D.setText(_translate("MainWidget", "View3D"))
        self.ViewSlice.setText(_translate("MainWidget", "ViewSlice"))
        self.HideLabel.setText(_translate("MainWidget", "HideLabel"))
        self.ShowLabel.setText(_translate("MainWidget", "ShowLabel"))
        self.HidePredict.setText(_translate("MainWidget", "HidePredict"))
        self.ShowPredict.setText(_translate("MainWidget", "ShowPredict"))
        self.SaveFig.setText(_translate("MainWidget", "SaveFig"))
        self.progressBar.setFormat(_translate("MainWidget", "%p%"))
