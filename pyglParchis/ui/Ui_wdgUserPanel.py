# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/wdgUserPanel.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_wdgUserPanel(object):
    def setupUi(self, wdgUserPanel):
        wdgUserPanel.setObjectName("wdgUserPanel")
        wdgUserPanel.resize(407, 247)
        self.vboxlayout = QtWidgets.QVBoxLayout(wdgUserPanel)
        self.vboxlayout.setObjectName("vboxlayout")
        self.grp = QtWidgets.QGroupBox(wdgUserPanel)
        self.grp.setEnabled(True)
        self.grp.setObjectName("grp")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.grp)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self._3 = QtWidgets.QVBoxLayout()
        self._3.setObjectName("_3")
        self.lblAvatar = QtWidgets.QLabel(self.grp)
        self.lblAvatar.setEnabled(False)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(244, 244, 244))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.lblAvatar.setPalette(palette)
        self.lblAvatar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lblAvatar.setText("")
        self.lblAvatar.setPixmap(QtGui.QPixmap(":/glparchis/ficharoja.png"))
        self.lblAvatar.setAlignment(QtCore.Qt.AlignCenter)
        self.lblAvatar.setObjectName("lblAvatar")
        self._3.addWidget(self.lblAvatar)
        self._4 = QtWidgets.QHBoxLayout()
        self._4.setObjectName("_4")
        self.lbl1 = QtWidgets.QLabel(self.grp)
        self.lbl1.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl1.sizePolicy().hasHeightForWidth())
        self.lbl1.setSizePolicy(sizePolicy)
        self.lbl1.setText("")
        self.lbl1.setPixmap(QtGui.QPixmap(":/glparchis/cube.png"))
        self.lbl1.setScaledContents(True)
        self.lbl1.setObjectName("lbl1")
        self._4.addWidget(self.lbl1)
        self.lbl2 = QtWidgets.QLabel(self.grp)
        self.lbl2.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl2.sizePolicy().hasHeightForWidth())
        self.lbl2.setSizePolicy(sizePolicy)
        self.lbl2.setText("")
        self.lbl2.setPixmap(QtGui.QPixmap(":/glparchis/cube.png"))
        self.lbl2.setScaledContents(True)
        self.lbl2.setObjectName("lbl2")
        self._4.addWidget(self.lbl2)
        self.lbl3 = QtWidgets.QLabel(self.grp)
        self.lbl3.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl3.sizePolicy().hasHeightForWidth())
        self.lbl3.setSizePolicy(sizePolicy)
        self.lbl3.setText("")
        self.lbl3.setPixmap(QtGui.QPixmap(":/glparchis/cube.png"))
        self.lbl3.setScaledContents(True)
        self.lbl3.setObjectName("lbl3")
        self._4.addWidget(self.lbl3)
        self._3.addLayout(self._4)
        self.horizontalLayout.addLayout(self._3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lst = QtWidgets.QListWidget(self.grp)
        self.lst.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lst.setFont(font)
        self.lst.setObjectName("lst")
        self.verticalLayout.addWidget(self.lst)
        self.chk = QtWidgets.QCheckBox(self.grp)
        self.chk.setObjectName("chk")
        self.verticalLayout.addWidget(self.chk)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.vboxlayout.addWidget(self.grp)

        self.retranslateUi(wdgUserPanel)
        QtCore.QMetaObject.connectSlotsByName(wdgUserPanel)

    def retranslateUi(self, wdgUserPanel):
        _translate = QtCore.QCoreApplication.translate
        wdgUserPanel.setWindowTitle(_translate("wdgUserPanel", "Form"))
        self.grp.setTitle(_translate("wdgUserPanel", "Jugador"))
        self.chk.setText(_translate("wdgUserPanel", "Muestra el historial"))

import glparchis_rc
