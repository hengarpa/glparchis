#!/usr/bin/env python
#-*- coding: utf-8 -*- 

import sys, os, datetime
WindowsVersion=False #Hay dos una en libmyquotes y otra en glparchis
so="src.linux"
os.environ['glparchisso']=so
#src.linux src.windows bin.linux bin.windows
if so=="src.windows" or so=="bin.windows":
    sys.path.append("../lib/glparchis")
elif so=="src.linux" or so=="bin.linux":
    sys.path.append("/usr/lib/glparchis")

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from frmMain import *

def help():
    print ("Ayuda")

try:
    os.makedirs(os.path.expanduser("~/.glparchis/"))
except:
    pass

sys.setrecursionlimit(50000)


cfgfile=ConfigFile(os.path.expanduser("~/.glparchis/")+ "glparchis.cfg")
cfgfile.save()
print (cfgfile.language)

app = QApplication(sys.argv)
app.setApplicationName("glParchis {0}".format(str(datetime.datetime.now())))
app.setQuitOnLastWindowClosed(True)
try:
    from PyQt4.phonon import Phonon
    borrar= Phonon.MediaObject(app)
except ImportError:
    QMessageBox.critical(None, "glParchis",  "Tu instalación QT no tiene soporte Phonon")
    sys.exit(1)

from libglparchis import cargarQTranslator
cfgfile.qtranslator=QTranslator()
cargarQTranslator(cfgfile)

frmMain = frmMain(cfgfile) 
frmMain.show()
sys.exit(app.exec_())

