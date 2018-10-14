# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/frmMain.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_frmMain(object):
    def setupUi(self, frmMain):
        frmMain.setObjectName("frmMain")
        frmMain.setWindowModality(QtCore.Qt.ApplicationModal)
        frmMain.resize(995, 568)
        frmMain.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/glparchis/ficharoja.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        frmMain.setWindowIcon(icon)
        frmMain.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.wdg = QtWidgets.QWidget(frmMain)
        self.wdg.setObjectName("wdg")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.wdg)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.setObjectName("layout")
        self.horizontalLayout.addLayout(self.layout)
        frmMain.setCentralWidget(self.wdg)
        self.menuBar = QtWidgets.QMenuBar(frmMain)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 995, 30))
        self.menuBar.setObjectName("menuBar")
        self.menuAyuda = QtWidgets.QMenu(self.menuBar)
        self.menuAyuda.setObjectName("menuAyuda")
        self.menuJugar = QtWidgets.QMenu(self.menuBar)
        self.menuJugar.setObjectName("menuJugar")
        self.menuConfiguraci_n = QtWidgets.QMenu(self.menuBar)
        self.menuConfiguraci_n.setObjectName("menuConfiguraci_n")
        self.menuVer = QtWidgets.QMenu(self.menuBar)
        self.menuVer.setObjectName("menuVer")
        frmMain.setMenuBar(self.menuBar)
        self.toolBar = QtWidgets.QToolBar(frmMain)
        self.toolBar.setIconSize(QtCore.QSize(24, 24))
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.toolBar.setObjectName("toolBar")
        frmMain.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionSalir = QtWidgets.QAction(frmMain)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/glparchis/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSalir.setIcon(icon1)
        self.actionSalir.setObjectName("actionSalir")
        self.actionAcercaDe = QtWidgets.QAction(frmMain)
        self.actionAcercaDe.setIcon(icon)
        self.actionAcercaDe.setObjectName("actionAcercaDe")
        self.actionRecuperarPartida = QtWidgets.QAction(frmMain)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/glparchis/open.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRecuperarPartida.setIcon(icon2)
        self.actionRecuperarPartida.setObjectName("actionRecuperarPartida")
        self.actionGuardarPartida = QtWidgets.QAction(frmMain)
        self.actionGuardarPartida.setEnabled(False)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/glparchis/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionGuardarPartida.setIcon(icon3)
        self.actionGuardarPartida.setObjectName("actionGuardarPartida")
        self.actionPartidaNueva4 = QtWidgets.QAction(frmMain)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/glparchis/game4.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPartidaNueva4.setIcon(icon4)
        self.actionPartidaNueva4.setObjectName("actionPartidaNueva4")
        self.actionSettings = QtWidgets.QAction(frmMain)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/glparchis/configure.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSettings.setIcon(icon5)
        self.actionSettings.setObjectName("actionSettings")
        self.actionHelp = QtWidgets.QAction(frmMain)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/glparchis/help.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionHelp.setIcon(icon6)
        self.actionHelp.setObjectName("actionHelp")
        self.actionUpdates = QtWidgets.QAction(frmMain)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/glparchis/update.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionUpdates.setIcon(icon7)
        self.actionUpdates.setObjectName("actionUpdates")
        self.actionSound = QtWidgets.QAction(frmMain)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/glparchis/sound.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSound.setIcon(icon8)
        self.actionSound.setObjectName("actionSound")
        self.actionPartidaNueva6 = QtWidgets.QAction(frmMain)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/glparchis/game6.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPartidaNueva6.setIcon(icon9)
        self.actionPartidaNueva6.setObjectName("actionPartidaNueva6")
        self.actionPartidaNueva8 = QtWidgets.QAction(frmMain)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/glparchis/game8.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPartidaNueva8.setIcon(icon10)
        self.actionPartidaNueva8.setObjectName("actionPartidaNueva8")
        self.actionFullScreen = QtWidgets.QAction(frmMain)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/glparchis/fullscreen.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFullScreen.setIcon(icon11)
        self.actionFullScreen.setObjectName("actionFullScreen")
        self.actionMundialStatistics = QtWidgets.QAction(frmMain)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/glparchis/statistics.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionMundialStatistics.setIcon(icon12)
        self.actionMundialStatistics.setObjectName("actionMundialStatistics")
        self.actionAcercarTablero = QtWidgets.QAction(frmMain)
        self.actionAcercarTablero.setEnabled(False)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/glparchis/zoom-in.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAcercarTablero.setIcon(icon13)
        self.actionAcercarTablero.setObjectName("actionAcercarTablero")
        self.actionAlejarTablero = QtWidgets.QAction(frmMain)
        self.actionAlejarTablero.setEnabled(False)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(":/glparchis/zoom-out.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAlejarTablero.setIcon(icon14)
        self.actionAlejarTablero.setObjectName("actionAlejarTablero")
        self.actionPartidaNueva3 = QtWidgets.QAction(frmMain)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(":/glparchis/game3.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPartidaNueva3.setIcon(icon15)
        self.actionPartidaNueva3.setObjectName("actionPartidaNueva3")
        self.actionReportBug = QtWidgets.QAction(frmMain)
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(":/glparchis/reportbug.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionReportBug.setIcon(icon16)
        self.actionReportBug.setObjectName("actionReportBug")
        self.actionAutomaticDice = QtWidgets.QAction(frmMain)
        self.actionAutomaticDice.setCheckable(True)
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap(":/glparchis/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAutomaticDice.setIcon(icon17)
        self.actionAutomaticDice.setObjectName("actionAutomaticDice")
        self.menuAyuda.addAction(self.actionHelp)
        self.menuAyuda.addSeparator()
        self.menuAyuda.addAction(self.actionMundialStatistics)
        self.menuAyuda.addSeparator()
        self.menuAyuda.addAction(self.actionUpdates)
        self.menuAyuda.addSeparator()
        self.menuAyuda.addAction(self.actionReportBug)
        self.menuAyuda.addSeparator()
        self.menuAyuda.addAction(self.actionAcercaDe)
        self.menuJugar.addAction(self.actionPartidaNueva4)
        self.menuJugar.addAction(self.actionPartidaNueva6)
        self.menuJugar.addAction(self.actionPartidaNueva8)
        self.menuJugar.addSeparator()
        self.menuJugar.addAction(self.actionRecuperarPartida)
        self.menuJugar.addAction(self.actionGuardarPartida)
        self.menuJugar.addSeparator()
        self.menuJugar.addAction(self.actionSalir)
        self.menuConfiguraci_n.addAction(self.actionSound)
        self.menuConfiguraci_n.addSeparator()
        self.menuConfiguraci_n.addSeparator()
        self.menuConfiguraci_n.addAction(self.actionSettings)
        self.menuVer.addAction(self.actionAcercarTablero)
        self.menuVer.addAction(self.actionAlejarTablero)
        self.menuVer.addSeparator()
        self.menuVer.addAction(self.actionFullScreen)
        self.menuBar.addAction(self.menuJugar.menuAction())
        self.menuBar.addAction(self.menuVer.menuAction())
        self.menuBar.addAction(self.menuConfiguraci_n.menuAction())
        self.menuBar.addAction(self.menuAyuda.menuAction())
        self.toolBar.addAction(self.actionPartidaNueva3)
        self.toolBar.addAction(self.actionPartidaNueva4)
        self.toolBar.addAction(self.actionPartidaNueva6)
        self.toolBar.addAction(self.actionPartidaNueva8)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionAutomaticDice)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionRecuperarPartida)
        self.toolBar.addAction(self.actionGuardarPartida)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionSound)
        self.toolBar.addAction(self.actionAcercarTablero)
        self.toolBar.addAction(self.actionAlejarTablero)
        self.toolBar.addAction(self.actionFullScreen)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionSettings)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionHelp)
        self.toolBar.addAction(self.actionMundialStatistics)
        self.toolBar.addAction(self.actionAcercaDe)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionSalir)

        self.retranslateUi(frmMain)
        self.actionSalir.triggered.connect(frmMain.close)
        QtCore.QMetaObject.connectSlotsByName(frmMain)

    def retranslateUi(self, frmMain):
        _translate = QtCore.QCoreApplication.translate
        self.menuAyuda.setTitle(_translate("frmMain", "A&yuda"))
        self.menuJugar.setTitle(_translate("frmMain", "J&ugar"))
        self.menuConfiguraci_n.setTitle(_translate("frmMain", "&Configuracion"))
        self.menuVer.setTitle(_translate("frmMain", "Ver"))
        self.toolBar.setWindowTitle(_translate("frmMain", "toolBar"))
        self.actionSalir.setText(_translate("frmMain", "S&alir"))
        self.actionSalir.setShortcut(_translate("frmMain", "Esc"))
        self.actionAcercaDe.setText(_translate("frmMain", "Acerca &de"))
        self.actionRecuperarPartida.setText(_translate("frmMain", "&Recuperar partida"))
        self.actionGuardarPartida.setText(_translate("frmMain", "&Guardar partida"))
        self.actionPartidaNueva4.setText(_translate("frmMain", "Partida de &4 jugadores"))
        self.actionPartidaNueva4.setToolTip(_translate("frmMain", "Partida de 4 jugadores"))
        self.actionPartidaNueva4.setShortcut(_translate("frmMain", "Ctrl+4"))
        self.actionSettings.setText(_translate("frmMain", "&Preferencias"))
        self.actionHelp.setText(_translate("frmMain", "&Ayuda del juego"))
        self.actionHelp.setToolTip(_translate("frmMain", "Muestra la ayuda del juego"))
        self.actionHelp.setShortcut(_translate("frmMain", "F1"))
        self.actionUpdates.setText(_translate("frmMain", "&Buscar actualizaciones"))
        self.actionUpdates.setToolTip(_translate("frmMain", "Busca actualizaciones en Internet"))
        self.actionSound.setText(_translate("frmMain", "&Sonido encendido"))
        self.actionSound.setToolTip(_translate("frmMain", "Enciende o apaga el sonido"))
        self.actionSound.setShortcut(_translate("frmMain", "F5"))
        self.actionPartidaNueva6.setText(_translate("frmMain", "Partida de &6 jugadores"))
        self.actionPartidaNueva6.setToolTip(_translate("frmMain", "Partida de 6 jugadores"))
        self.actionPartidaNueva6.setShortcut(_translate("frmMain", "Ctrl+6"))
        self.actionPartidaNueva8.setText(_translate("frmMain", "Partida de &8 jugadores"))
        self.actionPartidaNueva8.setToolTip(_translate("frmMain", "Partida de 8 jugadores"))
        self.actionPartidaNueva8.setShortcut(_translate("frmMain", "Ctrl+8"))
        self.actionFullScreen.setText(_translate("frmMain", "&Cambiar al modo de pantalla completa"))
        self.actionFullScreen.setToolTip(_translate("frmMain", "Cambiar al modo de pantalla completa"))
        self.actionFullScreen.setShortcut(_translate("frmMain", "F11"))
        self.actionMundialStatistics.setText(_translate("frmMain", "&Estadisticas mundiales"))
        self.actionMundialStatistics.setToolTip(_translate("frmMain", "Estadisticas mundiales"))
        self.actionAcercarTablero.setText(_translate("frmMain", "&Acercar tablero"))
        self.actionAcercarTablero.setToolTip(_translate("frmMain", "Acercar tablero"))
        self.actionAcercarTablero.setShortcut(_translate("frmMain", "+"))
        self.actionAlejarTablero.setText(_translate("frmMain", "A&lejar tablero"))
        self.actionAlejarTablero.setToolTip(_translate("frmMain", "Alejar tablero"))
        self.actionAlejarTablero.setShortcut(_translate("frmMain", "-"))
        self.actionPartidaNueva3.setText(_translate("frmMain", "Partida de &3 jugadores"))
        self.actionPartidaNueva3.setToolTip(_translate("frmMain", "Partida de 3 jugadores"))
        self.actionPartidaNueva3.setShortcut(_translate("frmMain", "Ctrl+4"))
        self.actionReportBug.setText(_translate("frmMain", "&Report a bug"))
        self.actionReportBug.setToolTip(_translate("frmMain", "Report a bug"))
        self.actionAutomaticDice.setText(_translate("frmMain", "Enciendo o apaga el automatismo del dado"))
        self.actionAutomaticDice.setToolTip(_translate("frmMain", "Enciendo o apaga el automatismo del dado"))

import glparchis_rc
