# -*- coding: utf-8 -*-
from math import *
def posfichas6(maxcasillas, posCasillas):
    """La posición de fichas de radio 1.4 es decir diametro 2.8 se colocan centradas en 1.5 de alto
    En lo ancho será a 0.3 de los extremos , es dicir a 1.7 el centro y a 5,3
    
    En las oblicuas se mete 0.7 del lado en el que está oblicuo
    """
    def n(id):
        """Para horizontales"""
        return ((posCasillas[id][0]+1.7, posCasillas[id][1]+1.5, 0.9), (posCasillas[id][0]+5.3, posCasillas[id][1]+1.5, 0.9))
    def w(id):
        """Para verticales"""
        return ((posCasillas[id][0]+1.5-3, posCasillas[id][1]+1.7, 0.9), (posCasillas[id][0]+1.5-3, posCasillas[id][1]+5.3, 0.9))
    def nw(id):
        return ((posCasillas[id][0]+r1*cos(alfa1), posCasillas[id][1]+r1*sin(alfa1), 0.9), (posCasillas[id][0]+r2*cos(alfa2), posCasillas[id][1]+r2*sin(alfa2), 0.9))
    def sw(id):
        return ((posCasillas[id][0]-r1*cos(alfa1)-3*sin(pi/3), posCasillas[id][1]+r1*sin(alfa1)-3*cos(pi/3), 0.9), (posCasillas[id][0]-r2*cos(alfa2)-3*sin(pi/3), posCasillas[id][1]+r2*cos(alfa2)+3*sin(pi/3), 0.9))
    def se(id):
        return ((posCasillas[id][0]-r1*cos(alfa1), posCasillas[id][1]-r1*sin(alfa1), 0.9), (posCasillas[id][0]-r2*cos(alfa2), posCasillas[id][1]-r2*sin(alfa2), 0.9))
    def ne(id):
        return ((posCasillas[id][0]+r1*cos(alfa1)+3*sin(pi/3), posCasillas[id][1]-r1*sin(alfa1)+3*cos(pi/3), 0.9), (posCasillas[id][0]+r2*cos(alfa2)+3*sin(pi/3), posCasillas[id][1]-r2*sin(alfa2)+3*cos(pi/3), 0.9))
    def s(id):
        (a, b)=n(id)
        return ((a[0]-7, a[1]-3, a[2]),  (b[0]-7,  b[1]-3,  b[2]))

    """Para nw
    C1 hace un angulo con el centro  0 de arctag 1.5/1.7+pi/4 =1.5083775167989393 rad
    y el radio es raix de 1.5^2+1.7^2= 2.2671568097509267
    
    c2 hace un angulo con el centro O de arctag 1.5/5.3 + pi/4 =1.0612040619859708
    y el radio es raix de 1.5^2+5.3^2= 5.508175741568165
    
    C3 recortando por 1.7
    
    C4 recortando por 5.3"""
    
    
    
    alfa1=atan(1.5/1.7)+pi/3
    r1=sqrt(1.5*1.5+1.7*1.7)
    alfa2=atan(1.5/5.3)+pi/3
    r2=sqrt(1.5*1.5+5.3*5.3)
    alfa3=atan(1.5/2.2)+pi/3
    r3=sqrt(2.2*2.2+5.3*5.3)
    alfa4=atan(1.5/4.8)+pi/3
    r4=sqrt(1.5*1.5+4.8*4.8)
    a=7*sqrt(3)/2
    b=3*sqrt(3)/2    
    posFichas=[None]*maxcasillas
    posFichas[0]=((0, 0, 0), (0, 0, 0))
    posFichas[1]=n(1)
    posFichas[2]=n(2)
    posFichas[3]=n(3)
    posFichas[4]=n(4)
    posFichas[5]=n(5)
    posFichas[6]=n(6)
    posFichas[7]=n(7)
    posFichas[8]=((22.7+0.7, 40.5, 0.9), (26.3, 40.5, 0.9))
    posFichas[9]=((17.050961894323343+3*cos(pi/6), 38.16006535994247-3*sin(pi/6), 0.9), (18.85096189432334+3*cos(pi/6)-0.7*sin(pi/6), 41.277756813566455-3*sin(pi/6)-0.7*cos(pi/6), 0.9))
    posFichas[10]=nw(10)
    posFichas[11]=nw(11)
    posFichas[12]=nw(12)
    posFichas[13]=nw(13)
    posFichas[14]=nw(14)
    posFichas[15]=nw(15)
    posFichas[16]=nw(16)
    posFichas[17]=nw(17)
    posFichas[18]=nw(18)
    posFichas[19]=nw(19)
    posFichas[20]=nw(20)
    posFichas[21]=nw(21)
    posFichas[22]=nw(22)
    posFichas[23]=nw(23)
    posFichas[24]=nw(24)
    posFichas[25]=((10.050961894323342+3*cos(pi/6)+0.7*sin(pi/6), 26.035709706960333-3*sin(pi/6)+0.7*cos(pi/6), 0.9), (11.850961894323342+3*cos(pi/6), 29.153401160584313-3*sin(pi/6), 0.9))
    posFichas[26]=((11.850961894323342+3*cos(pi/6), 18.473531880469263+3*sin(pi/6), 0.9), (10.050961894323342+3*cos(pi/6)+0.7*sin(pi/6), 21.700326799712375+3*sin(pi/6)-0.7*cos(pi/6), 0.9))
    posFichas[27]=sw(27)
    posFichas[28]=sw(28)
    posFichas[29]=sw(29)
    posFichas[30]=sw(30)
    posFichas[31]=sw(31)
    posFichas[32]=sw(32)
    posFichas[33]=sw(33)
    posFichas[34]=sw(34)
    posFichas[35]=sw(35)
    posFichas[36]=sw(36)
    posFichas[37]=sw(37)
    posFichas[38]=sw(38)
    posFichas[39]=sw(39)
    posFichas[40]=sw(40)
    posFichas[41]=sw(41)
    posFichas[42]=((18.85096189432334+3*cos(pi/6)-0.7*sin(pi/6), 6.349176227487122+3*sin(pi/6)+0.7*cos(pi/6), 0.9), (17.050961894323343+3*cos(pi/6), 9.575971146730236+3*sin(pi/6), 0.9))
    posFichas[43]=((22.7+0.7, 4.126933041053578+3, 0.9), (26.299999999999997, 4.126933041053578+3, 0.9))
    
    posFichas[44]=s(44)
    posFichas[45]=s(45)
    posFichas[46]=s(46)
    posFichas[47]=s(47)
    posFichas[48]=s(48)
    posFichas[49]=s(49)
    posFichas[50]=s(50)
    posFichas[51]=s(51)
    posFichas[52]=s(52)
    posFichas[53]=s(53)
    posFichas[54]=s(54)
    posFichas[55]=s(55)
    posFichas[56]=s(56)
    posFichas[57]=s(57)
    posFichas[58]=s(58)
    posFichas[59]=((36.7, 4.126933041053578+3, 0.9), (40.3-0.7, 4.126933041053578+3, 0.9))
    posFichas[60]=((45.94903810567666-3*cos(pi/6), 9.466867681111104+3*sin(pi/6), 0.9), (44.14903810567666-3*cos(pi/6)+0.7*sin(pi/6), 6.349176227487124+3*sin(pi/6)+0.7*cos(pi/6), 0.9))
    posFichas[61]=se(61)
    posFichas[62]=se(62)
    posFichas[63]=se(63)
    posFichas[64]=se(64)
    posFichas[65]=se(65)
    posFichas[66]=se(66)
    posFichas[67]=se(67)
    posFichas[68]=se(68)
    posFichas[69]=se(69)
    posFichas[70]=se(70)
    posFichas[71]=se(71)
    posFichas[72]=se(72)
    posFichas[73]=se(73)
    posFichas[74]=se(74)
    posFichas[75]=se(75)
    posFichas[76]=((52.94903810567666-3*cos(pi/6)-0.7*sin(pi/6), 21.591223334093243+3*sin(pi/6)-0.7*cos(pi/6), 0.9), (51.14903810567666-3*cos(pi/6), 18.473531880469263+3*sin(pi/6), 0.9))
    posFichas[77]=((51.14903810567666-3*cos(pi/6), 29.153401160584313-3*sin(pi/6), 0.9), (52.94903810567666-3*cos(pi/6)-0.7*sin(pi/6), 26.035709706960333-3*sin(pi/6)+0.7*cos(pi/6), 0.9))

    posFichas[78]=ne(78)
    posFichas[79]=ne(79)
    posFichas[80]=ne(80)
    posFichas[81]=ne(81)
    posFichas[82]=ne(82)
    posFichas[83]=ne(83)
    posFichas[84]=ne(84)
    posFichas[85]=ne(85)
    posFichas[86]=ne(86)
    posFichas[87]=ne(87)
    posFichas[88]=ne(88)
    posFichas[89]=ne(89)
    posFichas[90]=ne(90)
    posFichas[91]=ne(91)
    posFichas[92]=ne(92)
    print (posFichas[92])
    posFichas[93]=((44.14903810567666-3*cos(pi/6)+0.7*sin(pi/6), 41.277756813566455-3*sin(pi/6)-0.7*cos(pi/6), 0.9), (45.94903810567666-3*cos(pi/6), 38.16006535994248-3*sin(pi/6), 0.9))
    posFichas[94]=((36.7, 43.5-3, 0.9), (40.3-0.7, 43.5-3, 0.9))
    posFichas[95]=n(95)
    posFichas[96]=n(96)
    posFichas[97]=n(97)
    posFichas[98]=n(98)
    posFichas[99]=n(99)
    posFichas[100]=n(100)
    posFichas[101]=n(101)
    posFichas[102]=n(102)
    posFichas[103]=n(103)
    posFichas[104]=n(104)
    posFichas[105]=n(105)
    posFichas[106]=n(106)
    posFichas[107]=n(107)
    posFichas[108]=n(108)
    posFichas[109]=n(109)
    posFichas[110]=((0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0))
    posFichas[111]=nw(111)
    posFichas[112]=nw(112)
    posFichas[113]=nw(113)
    posFichas[114]=nw(114)
    posFichas[115]=nw(115)
    posFichas[116]=nw(116)
    posFichas[117]=nw(117)
    posFichas[118]=((0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0))
    posFichas[119]=sw(119)
    posFichas[120]=sw(120)
    posFichas[121]=sw(121)
    posFichas[122]=sw(122)
    posFichas[123]=sw(123)
    posFichas[124]=sw(124)
    posFichas[125]=sw(125)
    posFichas[126]=((0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0))
    posFichas[127]=s(127)
    posFichas[128]=s(128)
    posFichas[129]=s(129)
    posFichas[130]=s(130)
    posFichas[131]=s(131)
    posFichas[132]=s(132)
    posFichas[133]=s(133)
    posFichas[134]=((0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0))
    posFichas[135]=se(135)
    posFichas[136]=se(136)
    posFichas[137]=se(137)
    posFichas[138]=se(138)
    posFichas[139]=se(139)
    posFichas[140]=se(140)
    posFichas[141]=se(141)
    posFichas[142]=((0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0))
    posFichas[143]=ne(143)
    posFichas[144]=ne(144)
    posFichas[145]=ne(145)
    posFichas[146]=ne(146)
    posFichas[147]=ne(147)
    posFichas[148]=ne(148)
    posFichas[149]=ne(149)
    posFichas[150]=ne(150)
    posFichas[151]=((0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0))
    posFichas[152]=((0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0))
    posFichas[153]=((0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0))
    posFichas[154]=((0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0))
    posFichas[155]=((0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0))
    posFichas[156]=((0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0))

    return posFichas
