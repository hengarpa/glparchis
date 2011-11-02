#-*- coding: utf-8 -*- 
import os
from PyQt4.QtGui import *
from PyQt4.QtCore import *

def qcolor(colorstr):
    if colorstr=="yellow":
       return QColor(255, 255, 0)        
    elif colorstr=="blue":
       return QColor(0, 0, 255)
    elif colorstr=="red":
       return QColor(255, 0, 0 )
    elif colorstr=="green":
       return QColor(0, 255, 0)
def colorid(color):
    if color=="yellow":
        return 0
    elif color=="blue":
        return 1
    elif color=="red":
        return 2
    elif color=="green":
        return 3
        
def icoficha(color):
    ico = QIcon()
    ico.addPixmap(pixficha(color), QIcon.Normal, QIcon.Off) 
    return ico

def pixficha(color):
    """Devuelve un pixmap del color de la ficha"""
    if color=="yellow":
        return QPixmap(":/glparchis/fichaamarilla.png")
    elif color=="blue":
        return QPixmap(":/glparchis/fichaazul.png")
    elif color=="green":
        return QPixmap(":/glparchis/fichaverde.png")
    elif color=="red":
        return QPixmap(":/glparchis/ficharoja.png")
        
def q2s(q):
    """Qstring to python string en utf8"""
    return str(QString.toUtf8(q))
    
def s2q(st):
    """utf8 python string to qstring"""
    if st==None:
        return QString("")
    else:
        return QString(st.decode("UTF8"))

def i2b(integer):
    """Convierte 1 en Truue 0 en False"""
    if integer==1:
        return True
    elif integer==0:
        return False
        
def c2b(state):
    """QCheckstate to python bool"""
    if state==Qt.Checked:
        return True
    else:
        return False

def icodado(numero):
        ico = QIcon()
        ico.addPixmap(pixdado(numero), QIcon.Normal, QIcon.Off) 
        return ico

def fichas_name2id(name):
    if name=="yellow1": return 0
    if name=="yellow2": return 1
    if name=="yellow3": return 2
    if name=="yellow4": return 3
    if name=="blue1": return 4
    if name=="blue2": return 5
    if name=="blue3": return 6
    if name=="blue4": return 7
    if name=="red1": return 8
    if name=="red2": return 9
    if name=="red3": return 10
    if name=="red4": return 11
    if name=="green1": return 12
    if name=="green2": return 13
    if name=="green3": return 14
    if name=="green4": return 15

def pixdado(numero):
    """Devulve un QPixmap segun el valor del numero 0-6"""
    if numero==1:
        pix=QPixmap(":/glparchis/cube1.png")
    elif numero==2:
        pix=QPixmap(":/glparchis/cube2.png")
    elif numero==3:
        pix=QPixmap(":/glparchis/cube3.png")
    elif numero==4:
        pix=QPixmap(":/glparchis/cube4.png")
    elif numero==5:
        pix=QPixmap(":/glparchis/cube5.png")
    elif numero==6:
        pix=QPixmap(":/glparchis/cube6.png")
    elif numero==None:              
        pix=QPixmap(":/glparchis/cube.png")
    return pix

version="20111102"
colores=["yellow", "blue", "red", "green"]
cfgfile=os.environ['HOME']+ "/.glparchis/glparchis.cfg"
lastfile=os.environ['HOME']+ "/.glparchis/last.glparchis"
#Es la posición fisica de la casilla
posCasillas=[None]*105
posCasillas[0]=(0, 0, 0)
posCasillas[1]=(21, 60, 0.7)
posCasillas[2]=(21, 57, 0.7)
posCasillas[3]=(21, 54, 0.7)
posCasillas[4]=(21, 51, 0.7)
posCasillas[5]=(21, 48, 0.7)
posCasillas[6]=(21, 45, 0.7)
posCasillas[7]=(21, 42, 0.7)
posCasillas[8]=(28,  42, 0.7)
posCasillas[9]=(21, 42, 0.7)
posCasillas[10]=(21, 35, 0.7)
posCasillas[11]=(18, 35, 0.7)
posCasillas[12]=(15, 35, 0.7)
posCasillas[13]=(12, 35, 0.7)
posCasillas[14]=(9, 35, 0.7)
posCasillas[15]=(6, 35, 0.7)
posCasillas[16]=(3, 35, 0.7)
posCasillas[17]=(3, 28, 0.7)
posCasillas[18]=(3, 21, 0.7)
posCasillas[19]=(6, 21, 0.7)
posCasillas[20]=(9, 21, 0.7)
posCasillas[21]=(12, 21, 0.7)
posCasillas[22]=(15, 21, 0.7)
posCasillas[23]=(18, 21, 0.7)
posCasillas[24]=(21, 21, 0.7)
posCasillas[25]=(21, 28, 0.7)
posCasillas[26]=(21, 21, 0.7)
posCasillas[27]=(21, 18, 0.7)
posCasillas[28]=(21, 15, 0.7)
posCasillas[29]=(21, 12, 0.7)
posCasillas[30]=(21, 9, 0.7)
posCasillas[31]=(21, 6, 0.7)
posCasillas[32]=(21, 3, 0.7)
posCasillas[33]=(21, 0, 0.7)
posCasillas[34]=(28, 0, 0.7)
posCasillas[35]=(35, 0, 0.7)
posCasillas[36]=(35, 3, 0.7)
posCasillas[37]=(35, 6, 0.7)
posCasillas[38]=(35, 9, 0.7)
posCasillas[39]=(35, 12, 0.7)
posCasillas[40]=(35, 15, 0.7)
posCasillas[41]=(35, 18, 0.7)
posCasillas[42]=(35, 21, 0.7)
posCasillas[43]=(42, 21, 0.7)
posCasillas[44]=(45, 21, 0.7)
posCasillas[45]=(48, 21, 0.7)
posCasillas[46]=(51, 21, 0.7)
posCasillas[47]=(54, 21, 0.7)
posCasillas[48]=(57, 21, 0.7)
posCasillas[49]=(60, 21, 0.7)
posCasillas[50]=(63, 21, 0.7)
posCasillas[51]=(63, 28, 0.7)
posCasillas[52]=(63, 35, 0.7)
posCasillas[53]=(60, 35, 0.7)
posCasillas[54]=(57, 35, 0.7)
posCasillas[55]=(54, 35, 0.7)
posCasillas[56]=(51, 35, 0.7)
posCasillas[57]=(48, 35, 0.7)
posCasillas[58]=(45, 35, 0.7)
posCasillas[59]=(42, 35, 0.7)
posCasillas[60]=(42 ,42, 0.7)
posCasillas[61]=(35, 42, 0.7)
posCasillas[62]=(35, 45, 0.7)
posCasillas[63]=(35, 48, 0.7)
posCasillas[64]=(35, 51, 0.7)
posCasillas[65]=(35, 54, 0.7)
posCasillas[66]=(35, 57, 0.7)
posCasillas[67]=(35, 60, 0.7)
posCasillas[68]=(28, 60, 0.7)
posCasillas[69]=(28, 57, 0.7)
posCasillas[70]=(28, 54, 0.7)
posCasillas[71]=(28, 51, 0.7)
posCasillas[72]=(28, 48, 0.7)
posCasillas[73]=(28, 45, 0.7)
posCasillas[74]=(28, 42, 0.7)
posCasillas[75]=(28, 39, 0.7)
posCasillas[76]=(39, 39, 0.7)
posCasillas[77]=(6, 28, 0.7)
posCasillas[78]=(9, 28, 0.7)
posCasillas[79]=(12, 28, 0.7)
posCasillas[80]=(15, 28, 0.7)
posCasillas[81]=(18, 28, 0.7)
posCasillas[82]=(21, 28, 0.7)
posCasillas[83]=(24, 28, 0.7)
posCasillas[84]=(24, 39, 0.7)
posCasillas[85]=(28, 3, 0.7)
posCasillas[86]=(28, 6, 0.7)
posCasillas[87]=(28, 9, 0.7)
posCasillas[88]=(28, 12, 0.7)
posCasillas[89]=(28, 15, 0.7)
posCasillas[90]=(28, 18, 0.7)
posCasillas[91]=(28, 21, 0.7)
posCasillas[92]=(24, 24, 0.7)
posCasillas[93]=(60, 28, 0.7)
posCasillas[94]=(57, 28, 0.7)
posCasillas[95]=(54, 28, 0.7)
posCasillas[96]=(51, 28, 0.7)
posCasillas[97]=(48, 28, 0.7)
posCasillas[98]=(45, 28, 0.7)
posCasillas[99]=(42, 28, 0.7)
posCasillas[100]=(39, 24, 0.7)
posCasillas[101]=(0, 42, 0.7)
posCasillas[102]=(0, 0, 0.7)
posCasillas[103]=(42, 0, 0.7)
posCasillas[104]=(42,  42, 0.7)

#Es la posición física de la ficha en la casilla tanto si hay uno como si dos.
##En casilla horizontal se suma al punto inferiro ezdo 1.5 en altura y 1.7 ala primera y 5.3 a la segunda
##En las oblucuas a la lejana se resta 1.5 y ala siguiente 2 desde este punto
posFichas=[None]*105
posFichas[0]=((0, 0, 0), (0, 0, 0))
posFichas[1]=((22.7, 61.5, 0.9), (26.3, 61.5, 0.9))
posFichas[2]=((22.7, 58.5, 0.9), (26.3, 58.5, 0.9))
posFichas[3]=((22.7, 55.5, 0.9), (26.3, 55.5, 0.9))
posFichas[4]=((22.7, 52.5, 0.9), (26.3, 52.5, 0.9))
posFichas[5]=((22.7, 49.5, 0.9), (26.3, 49.5, 0.9))
posFichas[6]=((22.7, 46.5, 0.9), (26.3, 46.5, 0.9))
posFichas[7]=((22.7, 43.5, 0.9), (26.3, 43.5, 0.9))
posFichas[8]=((24.5, 40.5, 0.9), (26.5, 40.5, 0.9))
posFichas[9]=((22.5, 38.5, 0.9), (22.5, 36.5, 0.9))
posFichas[10]=((19.5, 40.3, 0.9), (19.5, 36.7, 0.9))
posFichas[11]=((16.5, 40.3, 0.9), (16.5, 36.7, 0.9))
posFichas[12]=((13.5, 40.3, 0.9), (13.5, 36.7, 0.9))
posFichas[13]=((10.5, 40.3, 0.9), (10.5, 36.7, 0.9))
posFichas[14]=((7.5, 40.3, 0.9), (7.5, 36.7, 0.9))
posFichas[15]=((4.5, 40.3, 0.9), (4.5, 36.7, 0.9))
posFichas[16]=((1.5, 40.3, 0.9), (1.5, 36.7, 0.9))
posFichas[17]=((1.5, 33.3, 0.9), (1.5, 29.7, 0.9))
posFichas[18]=((1.5, 26.3, 0.9), (1.5, 22.7, 0.9))
posFichas[19]=((4.5, 26.3, 0.9), (4.5, 22.7, 0.9))
posFichas[20]=((7.5, 26.3, 0.9), (7.5, 22.7, 0.9))
posFichas[21]=((10.5, 26.3, 0.9), (10.5, 22.7, 0.9))
posFichas[22]=((13.5, 26.3, 0.9), (13.5, 22.7, 0.9))
posFichas[23]=((16.5, 26.3, 0.9), (16.5, 22.7, 0.9))
posFichas[24]=((19.5, 26.3, 0.9), (19.5, 22.7, 0.9))
posFichas[25]=((22.5, 26.5, 0.9), (22.5, 24.5, 0.9))
posFichas[26]=((24.5, 22.5, 0.9), (26.5, 22.5, 0.9))
posFichas[27]=((22.7, 19.5, 0.9), (26.3, 19.5, 0.9))
posFichas[28]=((22.7, 16.5, 0.9), (26.3, 16.5, 0.9))
posFichas[29]=((22.7, 13.5, 0.9), (26.3, 13.5, 0.9))
posFichas[30]=((22.7, 10.5, 0.9), (26.3, 10.5, 0.9))
posFichas[31]=((22.7, 7.5, 0.9), (26.3, 7.5, 0.9))
posFichas[32]=((22.7, 4.5, 0.9), (26.3, 4.5, 0.9))
posFichas[33]=((22.7, 1.5, 0.9), (26.3, 1.5, 0.9))
posFichas[34]=((29.7, 1.5, 0.9), (33.3, 1.5, 0.9))
posFichas[35]=((36.7, 1.5, 0.9), (40.3, 1.5, 0.9))
posFichas[36]=((36.7, 4.5, 0.9), (40.3, 4.5, 0.9))
posFichas[37]=((36.7, 7.5, 0.9), (40.3, 7.5, 0.9))
posFichas[38]=((36.7, 10.5, 0.9), (40.3, 10.5, 0.9))
posFichas[39]=((36.7, 13.5, 0.9), (40.3, 13.5, 0.9))
posFichas[40]=((36.7, 16.5, 0.9), (40.3, 16.5, 0.9))
posFichas[41]=((36.7, 19.5, 0.9), (40.3, 19.5, 0.9))
posFichas[42]=((36.5, 22.5, 0.9), (38.5, 22.5, 0.9))
posFichas[43]=((40.5, 26.5, 0.9), (40.5, 24.5, 0.9))
posFichas[44]=((43.5, 26.3, 0.9), (43.5, 22.7, 0.9))
posFichas[45]=((46.5, 26.3, 0.9), (46.5, 22.7, 0.9))
posFichas[46]=((49.5, 26.3, 0.9), (49.5, 22.7, 0.9))
posFichas[47]=((52.5, 26.3, 0.9), (52.5, 22.7, 0.9))
posFichas[48]=((55.5, 26.3, 0.9), (55.5, 22.7, 0.9))
posFichas[49]=((58.5, 26.3, 0.9), (58.5, 22.7, 0.9))
posFichas[50]=((61.5, 26.3, 0.9), (61.5, 22.7, 0.9))
posFichas[51]=((61.5, 33.3, 0.9), (61.5, 29.7, 0.9))
posFichas[52]=((61.5, 40.3, 0.9), (61.5, 36.7, 0.9))
posFichas[53]=((58.5, 40.3, 0.9), (58.5, 36.7, 0.9))
posFichas[54]=((55.5, 40.3, 0.9), (55.5, 36.7, 0.9))
posFichas[55]=((52.5, 40.3, 0.9), (52.5, 36.7, 0.9))
posFichas[56]=((49.5, 40.3, 0.9), (49.5, 36.7, 0.9))
posFichas[57]=((46.5, 40.3, 0.9), (46.5, 36.7, 0.9))
posFichas[58]=((43.5, 40.3, 0.9), (43.5, 36.7, 0.9))
posFichas[59]=((40.5, 38.5, 0.9), (40.5, 36.5, 0.9))
posFichas[60]=((36.5, 40.5, 0.9), (38.5, 40.5, 0.9))
posFichas[61]=((36.7, 43.5, 0.9), (40.3, 43.5, 0.9))
posFichas[62]=((36.7, 46.5, 0.9), (40.3, 46.5, 0.9))
posFichas[63]=((36.7, 49.5, 0.9), (40.3, 49.5, 0.9))
posFichas[64]=((36.7, 52.5, 0.9), (40.3, 52.5, 0.9))
posFichas[65]=((36.7, 55.5, 0.9), (40.3, 55.5, 0.9))
posFichas[66]=((36.7, 58.5, 0.9), (40.3, 58.5, 0.9))
posFichas[67]=((36.7, 61.5, 0.9), (40.3, 61.5, 0.9))
posFichas[68]=((29.7, 61.5, 0.9), (33.3, 61.5, 0.9))
posFichas[69]=((29.7, 58.5, 0.9), (33.3, 58.5, 0.9))
posFichas[70]=((29.7, 55.5, 0.9), (33.3, 55.5, 0.9))
posFichas[71]=((29.7, 52.5, 0.9), (33.3, 52.5, 0.9))
posFichas[72]=((29.7, 49.5, 0.9), (33.3, 49.5, 0.9))
posFichas[73]=((29.7, 46.5, 0.9), (33.3, 46.5, 0.9))
posFichas[74]=((29.7, 43.5, 0.9), (33.3, 43.5, 0.9))
posFichas[75]=((29.7, 40.5, 0.9), (33.3, 40.5, 0.9))
posFichas[76]=((29.7, 37.5, 0.9), (33.3, 37.5, 0.9))
posFichas[77]=((4.5, 33.3, 0.9), (4.5, 29.7, 0.9))
posFichas[78]=((7.5, 33.3, 0.9), (7.5, 29.7, 0.9))
posFichas[79]=((10.5, 33.3, 0.9), (10.5, 29.7, 0.9))
posFichas[80]=((13.5, 33.3, 0.9), (13.5, 29.7, 0.9))
posFichas[81]=((16.5, 33.3, 0.9), (16.5, 29.7, 0.9))
posFichas[82]=((19.5, 33.3, 0.9), (19.5, 29.7, 0.9))
posFichas[83]=((22.5, 33.3, 0.9), (22.5, 29.7, 0.9))
posFichas[84]=((25.5, 33.3, 0.9), (25.5, 29.7, 0.9))
posFichas[85]=((29.7, 4.5, 0.9), (33.3, 4.5, 0.9))
posFichas[86]=((29.7, 7.5, 0.9), (33.3, 7.5, 0.9))
posFichas[87]=((29.7, 10.5, 0.9), (33.3, 10.5, 0.9))
posFichas[88]=((29.7, 13.5, 0.9), (33.3, 13.5, 0.9))
posFichas[89]=((29.7, 16.5, 0.9), (33.3, 16.5, 0.9))
posFichas[90]=((29.7, 19.5, 0.9), (33.3, 19.5, 0.9))
posFichas[91]=((29.7, 22.5, 0.9), (33.3, 22.5, 0.9))
posFichas[92]=((29.7, 25.5, 0.9), (33.3, 25.5, 0.9))
posFichas[93]=((58.5, 33.3, 0.9), (58.5, 29.7, 0.9))
posFichas[94]=((55.5, 33.3, 0.9), (55.5, 29.7, 0.9))
posFichas[95]=((52.5, 33.3, 0.9), (52.5, 29.7, 0.9))
posFichas[96]=((49.5, 33.3, 0.9), (49.5, 29.7, 0.9))
posFichas[97]=((46.5, 33.3, 0.9), (46.5, 29.7, 0.9))
posFichas[98]=((43.5, 33.3, 0.9), (43.5, 29.7, 0.9))
posFichas[99]=((40.5, 33.3, 0.9), (40.5, 29.7, 0.9))
posFichas[100]=((37.5, 33.3, 0.9), (37.5, 29.7, 0.9))
posFichas[101]=((7, 49, 0.9), (14, 49, 0.9), (14, 56, 0.9), (7, 56, 0.9))
posFichas[102]=((7, 7, 0.9), (14, 7, 0.9), (14, 14, 0.9), (7, 14, 0.9))
posFichas[103]=((49, 7, 0.9), (56, 7, 0.9), (49, 14, 0.9), (56, 14, 0.9))
posFichas[104]=((49, 49, 0.9), (56, 49, 0.9), (49, 56, 0.9), (56, 56, 0.9))

#Muestra la casilla de la ruta del jugador0 Ruta[rita]=jug1,2,3,4
ruta=[None]*73
ruta[0]=(101, 102, 103, 104)
ruta[1]=(5, 22, 39, 56)
ruta[2]=(6, 23, 40, 57)
ruta[3]=(7, 24, 41, 58)
ruta[4]=(8, 25, 42, 59)
ruta[5]=(9, 26, 43, 60)
ruta[6]=(10, 27, 44, 61)
ruta[7]=(11, 28, 45, 62)
ruta[8]=(12, 29, 46, 63)
ruta[9]=(13, 30, 47, 64)
ruta[10]=(14, 31, 48, 65)
ruta[11]=(15, 32, 49, 66)
ruta[12]=(16, 33, 50, 67)
ruta[13]=(17, 34, 51, 68)
ruta[14]=(18, 35, 52, 1)
ruta[15]=(19, 36, 53, 2)
ruta[16]=(20, 37, 54, 3)
ruta[17]=(21, 38, 55, 4)
ruta[18]=(22, 39, 56, 5)
ruta[19]=(23, 40, 57, 6)
ruta[20]=(24, 41, 58, 7)
ruta[21]=(25, 42, 59, 8)
ruta[22]=(26, 43, 60, 9)
ruta[23]=(27, 44, 61, 10)
ruta[24]=(28, 45, 62, 11)
ruta[25]=(29, 46, 63, 12)
ruta[26]=(30, 47, 64, 13)
ruta[27]=(31, 48, 65, 14)
ruta[28]=(32, 49, 66, 15)
ruta[29]=(33, 50, 67, 16)
ruta[30]=(34, 51, 68, 17)
ruta[31]=(35, 52, 1, 18)
ruta[32]=(36, 53, 2, 19)
ruta[33]=(37, 54, 3, 20)
ruta[34]=(38, 55, 4, 21)
ruta[35]=(39, 56, 5, 22)
ruta[36]=(40, 57, 6, 23)
ruta[37]=(41, 58, 7, 24)
ruta[38]=(42, 59, 8, 25)
ruta[39]=(43, 60, 9, 26)
ruta[40]=(44, 61, 10, 27)
ruta[41]=(45, 62, 11, 28)
ruta[42]=(46, 63, 12, 29)
ruta[43]=(47, 64, 13, 30)
ruta[44]=(48, 65, 14, 31)
ruta[45]=(49, 66, 15,  32)
ruta[46]=(50, 67, 16 , 33)
ruta[47]=(51, 68, 17 , 34)
ruta[48]=(52, 1, 18 , 35)
ruta[49]=(53, 2, 19, 36)
ruta[50]=(54, 3, 20, 37)
ruta[51]=(55, 4, 21, 38)
ruta[52]=(56, 5, 22, 39)
ruta[53]=(57, 6, 23, 40)
ruta[54]=(58, 7, 24, 41)
ruta[55]=(59, 8, 25, 42)
ruta[56]=(60, 9, 26, 43)
ruta[57]=(61, 10, 27, 44)
ruta[58]=(62, 11, 28, 45)
ruta[59]=(63, 12, 29, 46)
ruta[60]=(64, 13, 30, 47)
ruta[61]=(65, 14, 31, 48)
ruta[62]=(66, 15, 32, 49)
ruta[63]=(67, 16, 33, 50)
ruta[64]=(68, 17, 34, 51)
ruta[65]=(69, 77, 85, 93)
ruta[66]=(70, 78, 86, 94)
ruta[67]=(71, 79, 87, 95)
ruta[68]=(72, 80, 88, 96)
ruta[69]=(73, 81, 89, 97)
ruta[70]=(74, 82, 90, 98)
ruta[71]=(75, 83, 91, 99)
ruta[72]=(76, 84, 92, 100)

class Name:
    """Enumeración usada para los names de opengl"""
    ficha=[0]*16
    for i in range(0, 16):
        ficha[i]=i
    tablero=16
    casilla=[0]*105
    for i in range(17, 122):
        casilla[i-17]=i
#    print ficha,  tablero, casilla
