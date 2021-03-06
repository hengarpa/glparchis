# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'glparchis/ui/wdgGame.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_wdgGame(object):
    def setupUi(self, wdgGame):
        wdgGame.setObjectName("wdgGame")
        wdgGame.resize(1173, 714)
        self.horizontalLayout = QtWidgets.QHBoxLayout(wdgGame)
        self.horizontalLayout.setContentsMargins(1, 1, 1, 1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.splitter = QtWidgets.QSplitter(wdgGame)
        self.splitter.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setHandleWidth(5)
        self.splitter.setObjectName("splitter")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.layPanel = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.layPanel.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.layPanel.setContentsMargins(0, 0, 0, 0)
        self.layPanel.setObjectName("layPanel")
        self.cmdTirarDado = QtWidgets.QPushButton(self.layoutWidget)
        self.cmdTirarDado.setIconSize(QtCore.QSize(48, 48))
        self.cmdTirarDado.setAutoDefault(True)
        self.cmdTirarDado.setDefault(True)
        self.cmdTirarDado.setObjectName("cmdTirarDado")
        self.layPanel.addWidget(self.cmdTirarDado)
        self.panelScroll = QtWidgets.QScrollArea(self.layoutWidget)
        self.panelScroll.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.panelScroll.setWidgetResizable(True)
        self.panelScroll.setObjectName("panelScroll")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 523, 638))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.panelScrollLayout = QtWidgets.QVBoxLayout()
        self.panelScrollLayout.setObjectName("panelScrollLayout")
        self.verticalLayout_5.addLayout(self.panelScrollLayout)
        self.panelScroll.setWidget(self.scrollAreaWidgetContents)
        self.layPanel.addWidget(self.panelScroll)
        self.chkAvanza = QtWidgets.QCheckBox(self.layoutWidget)
        self.chkAvanza.setChecked(True)
        self.chkAvanza.setObjectName("chkAvanza")
        self.layPanel.addWidget(self.chkAvanza)
        self.layoutWidget_2 = QtWidgets.QWidget(self.splitter)
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tab = QtWidgets.QTabWidget(self.layoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab.sizePolicy().hasHeightForWidth())
        self.tab.setSizePolicy(sizePolicy)
        self.tab.setAutoFillBackground(True)
        self.tab.setTabPosition(QtWidgets.QTabWidget.East)
        self.tab.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tab.setObjectName("tab")
        self.tabGame = QtWidgets.QWidget()
        self.tabGame.setObjectName("tabGame")
        self.gridLayout = QtWidgets.QGridLayout(self.tabGame)
        self.gridLayout.setObjectName("gridLayout")
        self.ogl = wdgOGL(self.tabGame)
        self.ogl.setSizeIncrement(QtCore.QSize(10, 10))
        self.ogl.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.ogl.setObjectName("ogl")
        self.gridLayout.addWidget(self.ogl, 0, 0, 1, 1)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/glparchis/keko.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tab.addTab(self.tabGame, icon, "")
        self.tabStatistics = QtWidgets.QWidget()
        self.tabStatistics.setObjectName("tabStatistics")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.tabStatistics)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.table = QTableStatistics(self.tabStatistics)
        self.table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.table.setAlternatingRowColors(True)
        self.table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.table.setObjectName("table")
        self.table.setColumnCount(0)
        self.table.setRowCount(17)
        item = QtWidgets.QTableWidgetItem()
        self.table.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/glparchis/cube1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon1)
        self.table.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/glparchis/cube2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon2)
        self.table.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/glparchis/cube3.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon3)
        self.table.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/glparchis/cube4.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon4)
        self.table.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/glparchis/cube5.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon5)
        self.table.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/glparchis/cube6.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon6)
        self.table.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setVerticalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setVerticalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setVerticalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setVerticalHeaderItem(16, item)
        self.verticalLayout_3.addWidget(self.table)
        self.lblTime = QtWidgets.QLabel(self.tabStatistics)
        self.lblTime.setStyleSheet("font: 75 bold 11pt \"Sans Serif\";")
        self.lblTime.setText("")
        self.lblTime.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTime.setObjectName("lblTime")
        self.verticalLayout_3.addWidget(self.lblTime)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.tab.addTab(self.tabStatistics, icon5, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.tab_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.tabHS = QtWidgets.QTabWidget(self.tab_2)
        self.tabHS.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabHS.setObjectName("tabHS")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.tab_6)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.tblHighScores3 = QtWidgets.QTableWidget(self.tab_6)
        self.tblHighScores3.setObjectName("tblHighScores3")
        self.tblHighScores3.setColumnCount(4)
        self.tblHighScores3.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tblHighScores3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblHighScores3.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblHighScores3.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblHighScores3.setHorizontalHeaderItem(3, item)
        self.tblHighScores3.verticalHeader().setVisible(False)
        self.verticalLayout_7.addWidget(self.tblHighScores3)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/glparchis/game3.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabHS.addTab(self.tab_6, icon7, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.tab_5)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.tblHighScores4 = QtWidgets.QTableWidget(self.tab_5)
        self.tblHighScores4.setObjectName("tblHighScores4")
        self.tblHighScores4.setColumnCount(4)
        self.tblHighScores4.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tblHighScores4.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblHighScores4.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblHighScores4.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblHighScores4.setHorizontalHeaderItem(3, item)
        self.tblHighScores4.verticalHeader().setVisible(False)
        self.verticalLayout_4.addWidget(self.tblHighScores4)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/glparchis/game4.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabHS.addTab(self.tab_5, icon8, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.tab_3)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.tblHighScores6 = QtWidgets.QTableWidget(self.tab_3)
        self.tblHighScores6.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tblHighScores6.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tblHighScores6.setObjectName("tblHighScores6")
        self.tblHighScores6.setColumnCount(4)
        self.tblHighScores6.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tblHighScores6.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblHighScores6.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblHighScores6.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblHighScores6.setHorizontalHeaderItem(3, item)
        self.tblHighScores6.verticalHeader().setVisible(False)
        self.horizontalLayout_5.addWidget(self.tblHighScores6)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/glparchis/game6.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabHS.addTab(self.tab_3, icon9, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.tab_4)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.tblHighScores8 = QtWidgets.QTableWidget(self.tab_4)
        self.tblHighScores8.setObjectName("tblHighScores8")
        self.tblHighScores8.setColumnCount(4)
        self.tblHighScores8.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tblHighScores8.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblHighScores8.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblHighScores8.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblHighScores8.setHorizontalHeaderItem(3, item)
        self.tblHighScores8.verticalHeader().setVisible(False)
        self.horizontalLayout_6.addWidget(self.tblHighScores8)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/glparchis/game8.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabHS.addTab(self.tab_4, icon10, "")
        self.verticalLayout_6.addWidget(self.tabHS)
        self.label = QtWidgets.QLabel(self.tab_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.verticalLayout_6.addWidget(self.label)
        self.horizontalLayout_3.addLayout(self.verticalLayout_6)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/glparchis/corona.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tab.addTab(self.tab_2, icon11, "")
        self.verticalLayout_2.addWidget(self.tab)
        self.horizontalLayout.addWidget(self.splitter)

        self.retranslateUi(wdgGame)
        self.tab.setCurrentIndex(0)
        self.tabHS.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(wdgGame)

    def retranslateUi(self, wdgGame):
        _translate = QtCore.QCoreApplication.translate
        self.cmdTirarDado.setToolTip(_translate("wdgGame", "Pulsa este boton, haga doble click en el tablero o pulse ENTER, para tirar el dado"))
        self.cmdTirarDado.setText(_translate("wdgGame", "Tira el dado"))
        self.chkAvanza.setText(_translate("wdgGame", "Panel de usuario sigue al jugador actual"))
        self.tab.setTabText(self.tab.indexOf(self.tabGame), _translate("wdgGame", "Juego"))
        item = self.table.verticalHeaderItem(0)
        item.setText(_translate("wdgGame", "Numero de tiradas"))
        item = self.table.verticalHeaderItem(2)
        item.setText(_translate("wdgGame", "Dado saca 1"))
        item = self.table.verticalHeaderItem(3)
        item.setText(_translate("wdgGame", "Dado saca 2"))
        item = self.table.verticalHeaderItem(4)
        item.setText(_translate("wdgGame", "Dado saca 3"))
        item = self.table.verticalHeaderItem(5)
        item.setText(_translate("wdgGame", "Dado saca 4"))
        item = self.table.verticalHeaderItem(6)
        item.setText(_translate("wdgGame", "Dado saca 5"))
        item = self.table.verticalHeaderItem(7)
        item.setText(_translate("wdgGame", "Dado saca 6"))
        item = self.table.verticalHeaderItem(9)
        item.setText(_translate("wdgGame", "3 seises seguidos"))
        item = self.table.verticalHeaderItem(11)
        item.setText(_translate("wdgGame", "Fichas comidas por mi"))
        item = self.table.verticalHeaderItem(12)
        item.setText(_translate("wdgGame", "Fichas comidas por otro"))
        item = self.table.verticalHeaderItem(14)
        item.setText(_translate("wdgGame", "Casillas avanzadas"))
        item = self.table.verticalHeaderItem(16)
        item.setText(_translate("wdgGame", "Puntuacion"))
        self.tab.setTabText(self.tab.indexOf(self.tabStatistics), _translate("wdgGame", "Estadisticas"))
        item = self.tblHighScores3.horizontalHeaderItem(0)
        item.setText(_translate("wdgGame", "Fecha"))
        item = self.tblHighScores3.horizontalHeaderItem(1)
        item.setText(_translate("wdgGame", "Nombre"))
        item = self.tblHighScores3.horizontalHeaderItem(2)
        item.setText(_translate("wdgGame", "Tiempo de partida"))
        item = self.tblHighScores3.horizontalHeaderItem(3)
        item.setText(_translate("wdgGame", "Puntuacion"))
        self.tabHS.setTabText(self.tabHS.indexOf(self.tab_6), _translate("wdgGame", "Partida de 4 jugadores"))
        item = self.tblHighScores4.horizontalHeaderItem(0)
        item.setText(_translate("wdgGame", "Fecha"))
        item = self.tblHighScores4.horizontalHeaderItem(1)
        item.setText(_translate("wdgGame", "Nombre"))
        item = self.tblHighScores4.horizontalHeaderItem(2)
        item.setText(_translate("wdgGame", "Tiempo de partida"))
        item = self.tblHighScores4.horizontalHeaderItem(3)
        item.setText(_translate("wdgGame", "Puntuacion"))
        self.tabHS.setTabText(self.tabHS.indexOf(self.tab_5), _translate("wdgGame", "Partida de 4 jugadores"))
        item = self.tblHighScores6.horizontalHeaderItem(0)
        item.setText(_translate("wdgGame", "Fecha"))
        item = self.tblHighScores6.horizontalHeaderItem(1)
        item.setText(_translate("wdgGame", "Nombre"))
        item = self.tblHighScores6.horizontalHeaderItem(2)
        item.setText(_translate("wdgGame", "Tiempo de partida"))
        item = self.tblHighScores6.horizontalHeaderItem(3)
        item.setText(_translate("wdgGame", "Puntuacion"))
        self.tabHS.setTabText(self.tabHS.indexOf(self.tab_3), _translate("wdgGame", "Partida de 6 jugadores"))
        item = self.tblHighScores8.horizontalHeaderItem(0)
        item.setText(_translate("wdgGame", "Fecha"))
        item = self.tblHighScores8.horizontalHeaderItem(1)
        item.setText(_translate("wdgGame", "Nombre"))
        item = self.tblHighScores8.horizontalHeaderItem(2)
        item.setText(_translate("wdgGame", "Tiempo de partida"))
        item = self.tblHighScores8.horizontalHeaderItem(3)
        item.setText(_translate("wdgGame", "Puntuacion"))
        self.tabHS.setTabText(self.tabHS.indexOf(self.tab_4), _translate("wdgGame", "Partida de 8 jugadores"))
        self.label.setText(_translate("wdgGame", "<html><head/><body><p>La puntuacion que se obtiene al terminar la partida depende de lo lejos que hayan acabado las fichas de los oponentes de la casilla central y de la diferencia entre las fichas comidas por mi y las fichas que me comieron otros jugadores</p></body></html>"))
        self.tab.setTabText(self.tab.indexOf(self.tab_2), _translate("wdgGame", "Mejores puntuaciones"))

from glparchis.ui.myQGLWidget import wdgOGL
from glparchis.ui.qtablestatistics import QTableStatistics
import glparchis.images.glparchis_rc
