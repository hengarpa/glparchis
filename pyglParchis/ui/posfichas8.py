# -*- coding: utf-8 -*-
from math import *
def posfichas8(maxcasillas, posCasillas):
    """La posición de fichas de radio 1.4 es decir diametro 2.8 se colocan centradas en 1.5 de alto
    En lo ancho será a 0.3 de los extremos , es dicir a 1.7 el centro y a 5,3
    
    En las oblicuas se mete 0.5 del lado en el que está oblicuo
    """
#    def n(id):
#        """Para horizontales"""
#        return ((posCasillas[id][0]+1.7, posCasillas[id][1]+1.5, 0.9), (posCasillas[id][0]+5.3, posCasillas[id][1]+1.5, 0.9))
#    def w(id):
#        """Para verticales"""
#        return ((posCasillas[id][0]+1.5-3, posCasillas[id][1]+1.7, 0.9), (posCasillas[id][0]+1.5-3, posCasillas[id][1]+5.3, 0.9))
#    def nw(id):
#        return ((posCasillas[id][0]+r1*cos(alfa1), posCasillas[id][1]+r1*sin(alfa1), 0.9), (posCasillas[id][0]+r2*cos(alfa2), posCasillas[id][1]+r2*sin(alfa2), 0.9))
#    def sw(id):
#        return ((posCasillas[id][0]-r1*cos(alfa1)-b, posCasillas[id][1]+r1*sin(alfa1)-b, 0.9), (posCasillas[id][0]-r2*cos(alfa2)-b, posCasillas[id][1]+r2*cos(alfa2), 0.9))
#    def se(id):
#        return ((posCasillas[id][0]-r1*cos(alfa1), posCasillas[id][1]-r1*sin(alfa1), 0.9), (posCasillas[id][0]-r2*cos(alfa2), posCasillas[id][1]-r2*sin(alfa2), 0.9))
#    def ne(id):
#        return ((posCasillas[id][0]+r1*cos(alfa1)+b, posCasillas[id][1]-r1*sin(alfa1)+b, 0.9), (posCasillas[id][0]+r2*cos(alfa2)+b, posCasillas[id][1]-r2*sin(alfa2)+b, 0.9))
#    def e(id):
#        """Para verticales y giradas"""
#        return ((posCasillas[id][0]+1.5, posCasillas[id][1]+1.7-7, 0.9), (posCasillas[id][0]+1.5, posCasillas[id][1]+5.3-7, 0.9))
#    """Para nw
#    C1 hace un angulo con el centro  0 de arctag 1.5/1.7+pi/4 =1.5083775167989393 rad
#    y el radio es raix de 1.5^2+1.7^2= 2.2671568097509267
#    
#    c2 hace un angulo con el centro O de arctag 1.5/5.3 + pi/4 =1.0612040619859708
#    y el radio es raix de 1.5^2+5.3^2= 5.508175741568165
#    
#    C3 recortando por 1.7
#    
#    C4 recortando por 5.3"""
#    alfa1=atan(1.5/1.7)+pi/4
#    r1=sqrt(1.5*1.5+1.7*1.7)
#    alfa2=atan(1.5/5.3)+pi/4
#    r2=sqrt(1.5*1.5+5.3*5.3)
#    alfa3=atan(1.5/2.2)+pi/4
#    r3=sqrt(2.2*2.2+5.3*5.3)
#    alfa4=atan(1.5/4.8)+pi/4
#    r4=sqrt(1.5*1.5+4.8*4.8)
#    a=7*sqrt(2)/2
#    b=3*sqrt(2)/2
#
#    posFichas=[None]*maxcasillas
#    posFichas[0]=((0, 0, 0.9), (0, 0, 0.9))
#    posFichas[1]=n(1)
#    posFichas[2]=n(2)
#    posFichas[3]=n(3)
#    posFichas[4]=n(4)
#    posFichas[5]=n(5)
#    posFichas[6]=n(6)
#    posFichas[7]=n(7)
#    posFichas[8]=((23.4, 40.5, 0.9), (26.3, 40.5, 0.9))
#    posFichas[9]=((posCasillas[9][0]+r1*cos(alfa1)-a+b, posCasillas[9][1]+r1*sin(alfa1)-a-b, 0.9), (posCasillas[9][0]+r4*cos(alfa4)-a+b, posCasillas[9][1]+r4*sin(alfa4)-a-b, 0.9))
#    posFichas[10]=nw(10)
#    posFichas[11]=nw(11)
#    posFichas[12]=nw(12)
#    posFichas[13]=nw(13)
#    posFichas[14]=nw(14)
#    posFichas[15]=nw(15)
#    posFichas[16]=nw(16)
#    posFichas[17]=nw(17)
#    posFichas[18]=nw(18)
#    posFichas[19]=nw(19)
#    posFichas[20]=nw(20)
#    posFichas[21]=nw(21)
#    posFichas[22]=nw(22)
#    posFichas[23]=nw(23)
#    posFichas[24]=nw(24)
#    posFichas[25]=((posCasillas[25][0]+r3*cos(alfa3)-a+b-0.5, posCasillas[25][1]+r3*sin(alfa3)-a-b-3, 0.9), (posCasillas[25][0]+r2*cos(alfa2)-a+b, posCasillas[25][1]+r2*sin(alfa2)-a-b, 0.9))
#    posFichas[26]=((7.650757595082503, 21.850757595082502, 0.9), (7.650757595082503, 24.950757595082504, 0.9))
#    posFichas[27]=w(27)
#    posFichas[28]=w(28)
#    posFichas[29]=w(29)
#    posFichas[30]=w(30)
#    posFichas[31]=w(31)
#    posFichas[32]=w(32)
#    posFichas[33]=w(33)
#    posFichas[34]=w(34)
#    posFichas[35]=w(35)
#    posFichas[36]=w(36)
#    posFichas[37]=w(37)
#    posFichas[38]=w(38)
#    posFichas[39]=w(39)
#    posFichas[40]=w(40)
#    posFichas[41]=w(41)
#    posFichas[42]=((7.650757595082503, 8.350757595082503, 0.9), (7.650757595082503, 11.450757595082504, 0.9))
#    posFichas[43]=((8.837763363591385+b, 1.3424314830139794+b, 0.9), (6.292178951319813+b+0.5, 3.888015895285551+b-0.5, 0.9))
#    posFichas[44]=sw(44)
#  
#    posFichas[45]=sw(45)
#    posFichas[46]=sw(46)
#    posFichas[47]=sw(47)
#    posFichas[48]=sw(48)
#    posFichas[49]=sw(49)
#    posFichas[50]=sw(50)
#    posFichas[51]=sw(51)
#    posFichas[52]=sw(52)
#    posFichas[53]=sw(53)
#    posFichas[54]=sw(54)
#    posFichas[55]=sw(55)
#    posFichas[56]=sw(56)
#    posFichas[57]=sw(57)
#    posFichas[58]=sw(58)
#    posFichas[59]=((18.73725830020305+b-0.5, -8.557063453597685+b+0.5, 0.9), (16.191673887931476+b, -6.011479041326114+b, 0.9))
#    posFichas[60]=((23.2, -7.198484809834994, 0.9), (26.3, -7.198484809834994, 0.9))
#    posFichas[61]=n(61)
#    posFichas[62]=n(62)
#    posFichas[63]=n(63)
#    posFichas[64]=n(64)
#    posFichas[65]=n(65)
#    posFichas[66]=n(66)
#    posFichas[67]=n(67)
#    posFichas[68]=n(68)
#    posFichas[69]=n(69)
#    posFichas[70]=n(70)
#    posFichas[71]=n(71)
#    posFichas[72]=n(72)
#    posFichas[73]=n(73)
#    posFichas[74]=n(74)
#    posFichas[75]=n(75)
#    posFichas[76]=((36.7, -7.198484809834994, 0.9), (39.8, -7.198484809834994, 0.9))
#    posFichas[77]=((46.80832611206852-b, -6.011479041326114+b, 0.9), (44.26274169979695-b+.5, -8.557063453597685+b+.5, 0.9))
#    posFichas[78]=se(78)
#    posFichas[79]=se(79)
#    posFichas[80]=se(80)
#    posFichas[81]=se(81)
#    posFichas[82]=se(82)
#    posFichas[83]=se(83)
#    posFichas[84]=se(84)
#    posFichas[85]=se(85)
#    posFichas[86]=se(86)
#    posFichas[87]=se(87)
#    posFichas[88]=se(88)
#    posFichas[89]=se(89)
#    posFichas[90]=se(90)
#    posFichas[91]=se(91)
#    posFichas[92]=se(92)
#    posFichas[93]=((56.70782104868019-b-0.5, 3.888015895285551+b-0.5, 0.9), (54.162236636408615-b, 1.3424314830139794+b, 0.9))
#    posFichas[94]=((55.3492424049175, 8.350757595082502, 0.9), (55.3492424049175, 11.450757595082504, 0.9))
#    posFichas[95]=e(95)
#    posFichas[96]=e(96)
#    posFichas[97]=e(97)
#    posFichas[98]=e(98)
#    posFichas[99]=e(99)
#    posFichas[100]=e(100)
#    posFichas[101]=e(101)
#    posFichas[102]=e(102)
#    posFichas[103]=e(103)
#    posFichas[104]=e(104)
#    posFichas[105]=e(105)
#    posFichas[106]=e(106)
#    posFichas[107]=e(107)
#    posFichas[108]=e(108)
#    posFichas[109]=e(109)
#    posFichas[110]=((55.3492424049175, 21.850757595082502, 0.9), (55.3492424049175, 24.9507575950825, 0.9))
#    posFichas[111]=((54.16223663640862-b, 31.959083707151024-b, 0.9), (56.707821048680195-b-0.5, 29.41349929487945-b+.5, 0.9))
#
#    posFichas[112]=ne(112)
#    posFichas[113]=ne(113)
#    posFichas[114]=ne(114)
#    posFichas[115]=ne(115)
#    posFichas[116]=ne(116)
#    posFichas[117]=ne(117)
#    posFichas[118]=ne(118)
#    posFichas[119]=ne(119)
#    posFichas[120]=ne(120)
#    posFichas[121]=ne(121)
#    posFichas[122]=ne(122)
#    posFichas[123]=ne(123)
#    posFichas[124]=ne(124)
#    posFichas[125]=ne(125)
#    posFichas[126]=ne(126)
#    posFichas[127]= ((44.262741699796955-b+.5, 41.85857864376269-b-.5, 0.9), (46.80832611206853-b, 39.312994231491125-b, 0.9))
#    posFichas[128]=((36.7, 40.5, 0.9), (39.8, 40.5, 0.9))
#    posFichas[129]=n(129)
#    posFichas[130]=n(130)
#    posFichas[131]=n(131)
#    posFichas[132]=n(132)
#    posFichas[133]=n(133)
#    posFichas[134]=n(134)
#    posFichas[135]=n(135)
#    posFichas[136]=n(136)
#    posFichas[137]=n(137)
#    posFichas[138]=n(138)
#    posFichas[139]=n(139)
#    posFichas[140]=n(140)
#    posFichas[141]=n(141)
#    posFichas[142]=n(142)
#    posFichas[143]=n(143)
#    posFichas[144]=((29.7-3.6, 40.5-3, 0.9), (29.7, 40.5-3, 0.9), (33.3, 40.5-3, 0.9), (33.3+3.6, 40.5-3, 0.9))
#    posFichas[145]=nw(145)
#    posFichas[146]=nw(146)
#    posFichas[147]=nw(147)
#    posFichas[148]=nw(148)
#    posFichas[149]=nw(149)
#    posFichas[150]=nw(150)
#    posFichas[151]=nw(151)
#
#    posFichas[152]=((13.363246763185288+b-2.52, 32.24192641962564-b-2.52, 0.9), (13.363246763185288+b, 32.24192641962564-b, 0.9), (15.908831175456859+b, 34.787510831897215-b, 0.9), (15.908831175456859+b+2.52, 34.787510831897215-b+2.52, 0.9))
#    posFichas[153]=w(153)
#    posFichas[154]=w(154)
#    posFichas[155]=w(155)
#    posFichas[156]=w(156)
#    posFichas[157]=w(157)
#    posFichas[158]=w(158)
#    posFichas[159]=w(159)
#    
#    posFichas[160]=((7.650757595082503+3,14.850757595082502-3.6 , 0.9), (7.650757595082503+3, 14.850757595082502, 0.9), (7.650757595082503+3, 18.450757595082504, 0.9),  (7.650757595082503+3,18.450757595082504+3.6, 0.9))
#    posFichas[161]=sw(161)
#    posFichas[162]=sw(162)
#    posFichas[163]=sw(163)
#    posFichas[164]=sw(164)
#    posFichas[165]=sw(165)
#    posFichas[166]=sw(166)
#    posFichas[167]=sw(167)
#    posFichas[168]=( (13.363246763185288+b-2.52, 1.059588770539361+b+2.52, 0.9), (13.363246763185288+b, 1.059588770539361+b, 0.9), (15.90883117545686+b, -1.4859956417322104+b, 0.9), (15.90883117545686+b+2.52, -1.4859956417322104+b-2.52, 0.9))
#    posFichas[169]=n(169)
#    posFichas[170]=n(170)
#    posFichas[171]=n(171)
#    posFichas[172]=n(172)
#    posFichas[173]=n(173)
#    posFichas[174]=n(174)
#    posFichas[175]=n(175)
#    posFichas[176]=((29.7-3.6, -7.198484809834994+3, 0.9), (29.7, -7.198484809834994+3, 0.9), (33.3, -7.198484809834994+3, 0.9), (33.3+3.6, -7.198484809834994+3, 0.9))
#    posFichas[177]=se(177)
#    posFichas[178]=se(178)
#    posFichas[179]=se(179)
#    posFichas[180]=se(180)
#    posFichas[181]=se(181)
#    posFichas[182]=se(182)
#    posFichas[183]=se(183)
#    posFichas[184]=( (49.63675323681471-b+2.52, 1.0595887705393618+b+2.52, 0.9), (49.63675323681471-b, 1.0595887705393618+b, 0.9), (47.09116882454314-b, -1.4859956417322095+b, 0.9),  (47.09116882454314-2.52-b, -1.4859956417322095+b-2.52, 0.9))
#    posFichas[185]=e(185)
#    posFichas[186]=e(186)
#    posFichas[187]=e(187)
#    posFichas[188]=e(188)
#    posFichas[189]=e(189)
#    posFichas[190]=e(190)
#    posFichas[191]=e(191)
#    posFichas[192]=((55.3492424049175-3,14.850757595082502-3.6 , 0.9), (55.3492424049175-3, 14.850757595082502, 0.9), (55.3492424049175-3, 18.450757595082504, 0.9),  (55.3492424049175-3,18.450757595082504+3.6, 0.9))
#    posFichas[193]=ne(193)
#    posFichas[194]=ne(194)
#    posFichas[195]=ne(195)
#    posFichas[196]=ne(196)
#    posFichas[197]=ne(197)
#    posFichas[198]=ne(198)
#    posFichas[199]=ne(199)
#    posFichas[200]=((47.09116882454314-b-2.52, 34.787510831897215-b+2.52, 0.9),(47.09116882454314-b, 34.787510831897215-b, 0.9), (49.63675323681471-b, 32.24192641962564-b, 0.9),  (49.63675323681471-b+2.52, 32.24192641962564-b-2.52, 0.9))
#
#    x=(22.7, 49.5, 0.9)
#    s=5#Separados
#    v=3#Hacia vertice 
#    h=1.21#horizonytal
#    posFichas[201]=((x[0]-s, x[1], 0.9), (x[0]-s-h, x[1]+v, 0.9), (x[0]-s-h-h, x[1]+v+v, 0.9), (x[0]-s-h-h-h, x[1]+v+v+v, 0.9))
#    
#    x=(-1.3492424049174971, 25.450757595082504, 0.9)
#    posFichas[202]=((x[0], x[1]+s, 0.9), (x[0]-v, x[1]+s+h, 0.9), (x[0]-v-v, x[1]+s+h+h, 0.9), (x[0]-v-v-v, x[1]+s+h+h+h, 0.9))
#    
#    print(posFichas[107])
#    x=(-1.3492424049174971, 7.850757595082503, 0.9)
#    posFichas[203]=((x[0], x[1]-s, 0.9), (x[0]-v, x[1]-s-h, 0.9), (x[0]-v-v, x[1]-s-h-h, 0.9), (x[0]-v-v-v, x[1]-s-h-h-h, 0.9))
#    x=(22.7, -16.198484809834994, 0.9)
#    posFichas[204]=((x[0]-s, x[1], 0.9), (x[0]-s-h, x[1]-v, 0.9), (x[0]-s-h-h, x[1]-v-v, 0.9), (x[0]-s-h-h-h, x[1]-v-v-v, 0.9))
#    x=(40.3, -16.198484809834994, 0.9)
#    posFichas[205]=((x[0]+s, x[1], 0.9), (x[0]+s+h, x[1]-v, 0.9), (x[0]+s+h+h, x[1]-v-v, 0.9), (x[0]+s+h+h+h, x[1]-v-v-v, 0.9))
#    x=(64.3492424049175, 7.850757595082502, 0.9)
#    posFichas[206]=((x[0], x[1]-s, 0.9), (x[0]+v, x[1]-s-h, 0.9), (x[0]+v+v, x[1]-s-h-h, 0.9), (x[0]+v+v+v, x[1]-s-h-h-h, 0.9))
#    x=(64.3492424049175, 25.4507575950825, 0.9)
#    posFichas[207]=((x[0], x[1]+s, 0.9), (x[0]+v, x[1]+s+h, 0.9), (x[0]+v+v, x[1]+s+h+h, 0.9), (x[0]+v+v+v, x[1]+s+h+h+h, 0.9))
#    x=(40.3, 49.5, 0.9)
#    posFichas[208]=((x[0]+s, x[1], 0.9), (x[0]+s+h, x[1]+v, 0.9), (x[0]+s+h+h, x[1]+v+v, 0.9), (x[0]+s+h+h+h, x[1]+v+v+v, 0.9))
#
#    for i, p in enumerate(posFichas):
#        print "posFichas["+str(i)+"]="+str(p)
        
        
        
    posFichas=[None]*maxcasillas
    posFichas[0]=((0, 0, 0.9), (0, 0, 0.9))
    posFichas[1]=((22.7, 61.5, 0.9), (26.3, 61.5, 0.9))
    posFichas[2]=((22.7, 58.5, 0.9), (26.3, 58.5, 0.9))
    posFichas[3]=((22.7, 55.5, 0.9), (26.3, 55.5, 0.9))
    posFichas[4]=((22.7, 52.5, 0.9), (26.3, 52.5, 0.9))
    posFichas[5]=((22.7, 49.5, 0.9), (26.3, 49.5, 0.9))
    posFichas[6]=((22.7, 46.5, 0.9), (26.3, 46.5, 0.9))
    posFichas[7]=((22.7, 43.5, 0.9), (26.3, 43.5, 0.9))
    posFichas[8]=((23.4, 40.5, 0.9), (26.3, 40.5, 0.9))
    posFichas[9]=((18.312994231491118, 37.19167388793148, 0.9), (20.505025253169414, 39.383704909609776, 0.9))
    posFichas[10]=((16.191673887931476, 39.312994231491125, 0.9), (18.737258300203045, 41.85857864376269, 0.9))
    posFichas[11]=((14.070353544371834, 41.43431457505077, 0.9), (16.615937956643407, 43.979898987322336, 0.9))
    posFichas[12]=((11.94903320081219, 43.55563491861041, 0.9), (14.494617613083761, 46.101219330881975, 0.9))
    posFichas[13]=((9.827712857252546, 45.676955262170054, 0.9), (12.373297269524118, 48.22253967444162, 0.9))
    posFichas[14]=((7.706392513692904, 47.79827560572969, 0.9), (10.251976925964476, 50.34386001800126, 0.9))
    posFichas[15]=((5.585072170133262, 49.91959594928934, 0.9), (8.130656582404834, 52.465180361560904, 0.9))
    posFichas[16]=((3.463751826573619, 52.04091629284898, 0.9), (6.00933623884519, 54.58650070512055, 0.9))
    posFichas[17]=((-1.4859956417322129, 47.091168824543146, 0.9), (1.0595887705393583, 49.63675323681471, 0.9))
    posFichas[18]=((-6.435743110038045, 42.141421356237316, 0.9), (-3.8901586977664735, 44.68700576850888, 0.9))
    posFichas[19]=((-4.314422766478401, 40.02010101267767, 0.9), (-1.7688383542068298, 42.56568542494924, 0.9))
    posFichas[20]=((-2.193102422918759, 37.89878066911803, 0.9), (0.35248198935281216, 40.4443650813896, 0.9))
    posFichas[21]=((-0.07178207935911615, 35.77746032555839, 0.9), (2.473802332912455, 38.32304473782995, 0.9))
    posFichas[22]=((2.049538264200527, 33.65613998199874, 0.9), (4.595122676472098, 36.20172439427031, 0.9))
    posFichas[23]=((4.170858607760169, 31.534819638439096, 0.9), (6.716443020031741, 34.08040405071067, 0.9))
    posFichas[24]=((6.292178951319812, 29.413499294879454, 0.9), (8.837763363591383, 31.959083707151027, 0.9))
    posFichas[25]=((8.838811084783943, 27.59681606926402, 0.9), (10.959083707151027, 29.766695551725903, 0.9))
    posFichas[26]=((7.650757595082503, 21.850757595082502, 0.9), (7.650757595082503, 24.950757595082504, 0.9))
    posFichas[27]=((4.650757595082503, 21.850757595082502, 0.9), (4.650757595082503, 25.450757595082504, 0.9))
    posFichas[28]=((1.6507575950825029, 21.850757595082502, 0.9), (1.6507575950825029, 25.450757595082504, 0.9))
    posFichas[29]=((-1.3492424049174971, 21.850757595082502, 0.9), (-1.3492424049174971, 25.450757595082504, 0.9))
    posFichas[30]=((-4.349242404917497, 21.850757595082502, 0.9), (-4.349242404917497, 25.450757595082504, 0.9))
    posFichas[31]=((-7.349242404917497, 21.850757595082502, 0.9), (-7.349242404917497, 25.450757595082504, 0.9))
    posFichas[32]=((-10.349242404917497, 21.850757595082502, 0.9), (-10.349242404917497, 25.450757595082504, 0.9))
    posFichas[33]=((-13.349242404917497, 21.850757595082502, 0.9), (-13.349242404917497, 25.450757595082504, 0.9))
    posFichas[34]=((-13.349242404917497, 14.850757595082502, 0.9), (-13.349242404917497, 18.450757595082504, 0.9))
    posFichas[35]=((-13.349242404917497, 7.850757595082503, 0.9), (-13.349242404917497, 11.450757595082504, 0.9))
    posFichas[36]=((-10.349242404917497, 7.850757595082503, 0.9), (-10.349242404917497, 11.450757595082504, 0.9))
    posFichas[37]=((-7.349242404917497, 7.850757595082503, 0.9), (-7.349242404917497, 11.450757595082504, 0.9))
    posFichas[38]=((-4.349242404917497, 7.850757595082503, 0.9), (-4.349242404917497, 11.450757595082504, 0.9))
    posFichas[39]=((-1.3492424049174971, 7.850757595082503, 0.9), (-1.3492424049174971, 11.450757595082504, 0.9))
    posFichas[40]=((1.6507575950825029, 7.850757595082503, 0.9), (1.6507575950825029, 11.450757595082504, 0.9))
    posFichas[41]=((4.650757595082503, 7.850757595082503, 0.9), (4.650757595082503, 11.450757595082504, 0.9))
    posFichas[42]=((7.650757595082503, 8.350757595082502, 0.9), (7.650757595082503, 11.450757595082504, 0.9))
    posFichas[43]=((10.959083707151027, 3.4637518265736222, 0.9), (8.913499294879456, 5.509336238845194, 0.9))
    posFichas[44]=((8.837763363591385, 1.3424314830139794, 0.9), (6.292178951319813, 3.888015895285551, 0.9))
    posFichas[45]=((6.716443020031742, -0.7788888605456634, 0.9), (4.170858607760171, 1.766695551725908, 0.9))
    posFichas[46]=((4.595122676472099, -2.9002092041053062, 0.9), (2.0495382642005273, -0.35462479183373485, 0.9))
    posFichas[47]=((2.473802332912456, -5.021529547664949, 0.9), (-0.07178207935911551, -2.4759451353933777, 0.9))
    posFichas[48]=((0.3524819893528126, -7.142849891224592, 0.9), (-2.1931024229187583, -4.5972654789530205, 0.9))
    posFichas[49]=((-1.768838354206829, -9.264170234784235, 0.9), (-4.3144227664784, -6.718585822512663, 0.9))
    posFichas[50]=((-3.8901586977664726, -11.385490578343877, 0.9), (-6.435743110038044, -8.839906166072305, 0.9))
    posFichas[51]=((1.0595887705393605, -16.33523804664971, 0.9), (-1.4859956417322104, -13.789653634378139, 0.9))
    posFichas[52]=((6.009336238845191, -21.284985514955544, 0.9), (3.4637518265736196, -18.73940110268397, 0.9))
    posFichas[53]=((8.130656582404836, -19.1636651713959, 0.9), (5.585072170133263, -16.618080759124325, 0.9))
    posFichas[54]=((10.251976925964478, -17.042344827836256, 0.9), (7.706392513692905, -14.496760415564685, 0.9))
    posFichas[55]=((12.37329726952412, -14.921024484276614, 0.9), (9.827712857252546, -12.375440072005043, 0.9))
    posFichas[56]=((14.494617613083765, -12.799704140716969, 0.9), (11.949033200812192, -10.2541197284454, 0.9))
    posFichas[57]=((16.615937956643407, -10.678383797157327, 0.9), (14.070353544371837, -8.132799384885756, 0.9))
    posFichas[58]=((18.73725830020305, -8.557063453597685, 0.9), (16.191673887931476, -6.011479041326114, 0.9))
    posFichas[59]=((20.35857864376269, -5.935743110038042, 0.9), (18.312994231491118, -3.890158697766471, 0.9))
    posFichas[60]=((23.2, -7.198484809834994, 0.9), (26.3, -7.198484809834994, 0.9))
    posFichas[61]=((22.7, -10.198484809834994, 0.9), (26.3, -10.198484809834994, 0.9))
    posFichas[62]=((22.7, -13.198484809834994, 0.9), (26.3, -13.198484809834994, 0.9))
    posFichas[63]=((22.7, -16.198484809834994, 0.9), (26.3, -16.198484809834994, 0.9))
    posFichas[64]=((22.7, -19.198484809834994, 0.9), (26.3, -19.198484809834994, 0.9))
    posFichas[65]=((22.7, -22.198484809834994, 0.9), (26.3, -22.198484809834994, 0.9))
    posFichas[66]=((22.7, -25.198484809834994, 0.9), (26.3, -25.198484809834994, 0.9))
    posFichas[67]=((22.7, -28.198484809834994, 0.9), (26.3, -28.198484809834994, 0.9))
    posFichas[68]=((29.7, -28.198484809834994, 0.9), (33.3, -28.198484809834994, 0.9))
    posFichas[69]=((36.7, -28.198484809834994, 0.9), (40.3, -28.198484809834994, 0.9))
    posFichas[70]=((36.7, -25.198484809834994, 0.9), (40.3, -25.198484809834994, 0.9))
    posFichas[71]=((36.7, -22.198484809834994, 0.9), (40.3, -22.198484809834994, 0.9))
    posFichas[72]=((36.7, -19.198484809834994, 0.9), (40.3, -19.198484809834994, 0.9))
    posFichas[73]=((36.7, -16.198484809834994, 0.9), (40.3, -16.198484809834994, 0.9))
    posFichas[74]=((36.7, -13.198484809834994, 0.9), (40.3, -13.198484809834994, 0.9))
    posFichas[75]=((36.7, -10.198484809834994, 0.9), (40.3, -10.198484809834994, 0.9))
    posFichas[76]=((36.7, -7.198484809834994, 0.9), (39.8, -7.198484809834994, 0.9))
    posFichas[77]=((44.687005768508875, -3.890158697766471, 0.9), (42.6414213562373, -5.935743110038042, 0.9))
    posFichas[78]=((46.80832611206852, -6.011479041326114, 0.9), (44.26274169979695, -8.557063453597685, 0.9))
    posFichas[79]=((48.929646455628166, -8.132799384885757, 0.9), (46.38406204335659, -10.678383797157327, 0.9))
    posFichas[80]=((51.050966799187805, -10.2541197284454, 0.9), (48.50538238691623, -12.79970414071697, 0.9))
    posFichas[81]=((53.17228714274745, -12.375440072005041, 0.9), (50.62670273047588, -14.921024484276614, 0.9))
    posFichas[82]=((55.29360748630709, -14.496760415564683, 0.9), (52.748023074035515, -17.042344827836256, 0.9))
    posFichas[83]=((57.414927829866734, -16.618080759124325, 0.9), (54.86934341759516, -19.1636651713959, 0.9))
    posFichas[84]=((59.53624817342638, -18.73940110268397, 0.9), (56.990663761154806, -21.284985514955544, 0.9))
    posFichas[85]=((64.4859956417322, -13.789653634378137, 0.9), (61.940411229460636, -16.33523804664971, 0.9))
    posFichas[86]=((69.43574311003803, -8.839906166072307, 0.9), (66.89015869776647, -11.385490578343877, 0.9))
    posFichas[87]=((67.3144227664784, -6.7185858225126625, 0.9), (64.76883835420684, -9.264170234784235, 0.9))
    posFichas[88]=((65.19310242291876, -4.5972654789530205, 0.9), (62.64751801064719, -7.142849891224592, 0.9))
    posFichas[89]=((63.07178207935912, -2.4759451353933777, 0.9), (60.526197667087544, -5.021529547664949, 0.9))
    posFichas[90]=((60.95046173579947, -0.35462479183373485, 0.9), (58.4048773235279, -2.9002092041053062, 0.9))
    posFichas[91]=((58.82914139223983, 1.766695551725908, 0.9), (56.28355697996826, -0.7788888605456634, 0.9))
    posFichas[92]=((56.70782104868019, 3.888015895285551, 0.9), (54.162236636408615, 1.3424314830139794, 0.9))
    posFichas[93]=((54.08650070512054, 5.509336238845194, 0.9), (52.04091629284897, 3.4637518265736222, 0.9))
    posFichas[94]=((55.3492424049175, 8.350757595082502, 0.9), (55.3492424049175, 11.450757595082504, 0.9))
    posFichas[95]=((58.3492424049175, 7.850757595082502, 0.9), (58.3492424049175, 11.450757595082504, 0.9))
    posFichas[96]=((61.3492424049175, 7.850757595082502, 0.9), (61.3492424049175, 11.450757595082504, 0.9))
    posFichas[97]=((64.3492424049175, 7.850757595082502, 0.9), (64.3492424049175, 11.450757595082504, 0.9))
    posFichas[98]=((67.3492424049175, 7.850757595082502, 0.9), (67.3492424049175, 11.450757595082504, 0.9))
    posFichas[99]=((70.3492424049175, 7.850757595082502, 0.9), (70.3492424049175, 11.450757595082504, 0.9))
    posFichas[100]=((73.3492424049175, 7.850757595082502, 0.9), (73.3492424049175, 11.450757595082504, 0.9))
    posFichas[101]=((76.3492424049175, 7.850757595082502, 0.9), (76.3492424049175, 11.450757595082504, 0.9))
    posFichas[102]=((76.3492424049175, 14.850757595082502, 0.9), (76.3492424049175, 18.450757595082504, 0.9))
    posFichas[103]=((76.3492424049175, 21.850757595082502, 0.9), (76.3492424049175, 25.4507575950825, 0.9))
    posFichas[104]=((73.3492424049175, 21.850757595082502, 0.9), (73.3492424049175, 25.4507575950825, 0.9))
    posFichas[105]=((70.3492424049175, 21.850757595082502, 0.9), (70.3492424049175, 25.4507575950825, 0.9))
    posFichas[106]=((67.3492424049175, 21.850757595082502, 0.9), (67.3492424049175, 25.4507575950825, 0.9))
    posFichas[107]=((64.3492424049175, 21.850757595082502, 0.9), (64.3492424049175, 25.4507575950825, 0.9))
    posFichas[108]=((61.3492424049175, 21.850757595082502, 0.9), (61.3492424049175, 25.4507575950825, 0.9))
    posFichas[109]=((58.3492424049175, 21.850757595082502, 0.9), (58.3492424049175, 25.4507575950825, 0.9))
    posFichas[110]=((55.3492424049175, 21.850757595082502, 0.9), (55.3492424049175, 24.9507575950825, 0.9))
    posFichas[111]=((52.040916292848976, 29.83776336359138, 0.9), (54.08650070512055, 27.79217895131981, 0.9))
    posFichas[112]=((54.16223663640862, 31.959083707151024, 0.9), (56.707821048680195, 29.41349929487945, 0.9))
    posFichas[113]=((56.28355697996827, 34.08040405071067, 0.9), (58.82914139223984, 31.534819638439096, 0.9))
    posFichas[114]=((58.404877323527906, 36.20172439427031, 0.9), (60.95046173579948, 33.656139981998734, 0.9))
    posFichas[115]=((60.52619766708755, 38.32304473782995, 0.9), (63.071782079359124, 35.77746032555839, 0.9))
    posFichas[116]=((62.6475180106472, 40.4443650813896, 0.9), (65.19310242291877, 37.89878066911803, 0.9))
    posFichas[117]=((64.76883835420684, 42.56568542494924, 0.9), (67.3144227664784, 40.02010101267767, 0.9))
    posFichas[118]=((66.89015869776648, 44.68700576850888, 0.9), (69.43574311003805, 42.141421356237316, 0.9))
    posFichas[119]=((61.94041122946064, 49.63675323681472, 0.9), (64.48599564173222, 47.09116882454315, 0.9))
    posFichas[120]=((56.99066376115481, 54.58650070512055, 0.9), (59.53624817342639, 52.04091629284898, 0.9))
    posFichas[121]=((54.86934341759517, 52.465180361560904, 0.9), (57.41492782986674, 49.91959594928934, 0.9))
    posFichas[122]=((52.74802307403552, 50.34386001800126, 0.9), (55.293607486307096, 47.79827560572969, 0.9))
    posFichas[123]=((50.626702730475884, 48.22253967444162, 0.9), (53.17228714274746, 45.676955262170054, 0.9))
    posFichas[124]=((48.50538238691624, 46.101219330881975, 0.9), (51.05096679918781, 43.55563491861041, 0.9))
    posFichas[125]=((46.3840620433566, 43.979898987322336, 0.9), (48.92964645562817, 41.43431457505077, 0.9))
    posFichas[126]=((44.262741699796955, 41.85857864376269, 0.9), (46.80832611206853, 39.312994231491125, 0.9))
    posFichas[127]=((42.64142135623731, 39.237258300203045, 0.9), (44.68700576850888, 37.19167388793148, 0.9))
    posFichas[128]=((36.7, 40.5, 0.9), (39.8, 40.5, 0.9))
    posFichas[129]=((36.7, 43.5, 0.9), (40.3, 43.5, 0.9))
    posFichas[130]=((36.7, 46.5, 0.9), (40.3, 46.5, 0.9))
    posFichas[131]=((36.7, 49.5, 0.9), (40.3, 49.5, 0.9))
    posFichas[132]=((36.7, 52.5, 0.9), (40.3, 52.5, 0.9))
    posFichas[133]=((36.7, 55.5, 0.9), (40.3, 55.5, 0.9))
    posFichas[134]=((36.7, 58.5, 0.9), (40.3, 58.5, 0.9))
    posFichas[135]=((36.7, 61.5, 0.9), (40.3, 61.5, 0.9))
    posFichas[136]=((29.7, 61.5, 0.9), (33.3, 61.5, 0.9))
    posFichas[137]=((29.7, 58.5, 0.9), (33.3, 58.5, 0.9))
    posFichas[138]=((29.7, 55.5, 0.9), (33.3, 55.5, 0.9))
    posFichas[139]=((29.7, 52.5, 0.9), (33.3, 52.5, 0.9))
    posFichas[140]=((29.7, 49.5, 0.9), (33.3, 49.5, 0.9))
    posFichas[141]=((29.7, 46.5, 0.9), (33.3, 46.5, 0.9))
    posFichas[142]=((29.7, 43.5, 0.9), (33.3, 43.5, 0.9))
    posFichas[143]=((29.7, 40.5, 0.9), (33.3, 40.5, 0.9))
    posFichas[144]=((26.099999999999998, 37.5, 0.9), (29.7, 37.5, 0.9), (33.3, 37.5, 0.9), (36.9, 37.5, 0.9))
    posFichas[145]=((0.6353247018274308, 44.9698484809835, 0.9), (3.180909114099002, 47.51543289325507, 0.9))
    posFichas[146]=((2.756645045387073, 42.84852813742386, 0.9), (5.302229457658644, 45.39411254969543, 0.9))
    posFichas[147]=((4.877965388946715, 40.72720779386422, 0.9), (7.423549801218287, 43.27279220613578, 0.9))
    posFichas[148]=((6.999285732506358, 38.60588745030457, 0.9), (9.54487014477793, 41.15147186257614, 0.9))
    posFichas[149]=((9.120606076066, 36.48456710674493, 0.9), (11.666190488337572, 39.0301515190165, 0.9))
    posFichas[150]=((11.241926419625644, 34.36324676318529, 0.9), (13.787510831897215, 36.908831175456854, 0.9))
    posFichas[151]=((13.363246763185288, 32.24192641962564, 0.9), (15.908831175456859, 34.787510831897215, 0.9))
    posFichas[152]=((12.96456710674493, 27.600606076066, 0.9), (15.48456710674493, 30.120606076066, 0.9), (18.030151519016503, 32.66619048833757, 0.9), (20.550151519016502, 35.18619048833757, 0.9))
    posFichas[153]=((-10.349242404917497, 14.850757595082502, 0.9), (-10.349242404917497, 18.450757595082504, 0.9))
    posFichas[154]=((-7.349242404917497, 14.850757595082502, 0.9), (-7.349242404917497, 18.450757595082504, 0.9))
    posFichas[155]=((-4.349242404917497, 14.850757595082502, 0.9), (-4.349242404917497, 18.450757595082504, 0.9))
    posFichas[156]=((-1.3492424049174971, 14.850757595082502, 0.9), (-1.3492424049174971, 18.450757595082504, 0.9))
    posFichas[157]=((1.6507575950825029, 14.850757595082502, 0.9), (1.6507575950825029, 18.450757595082504, 0.9))
    posFichas[158]=((4.650757595082503, 14.850757595082502, 0.9), (4.650757595082503, 18.450757595082504, 0.9))
    posFichas[159]=((7.650757595082503, 14.850757595082502, 0.9), (7.650757595082503, 18.450757595082504, 0.9))
    posFichas[160]=((10.650757595082503, 11.250757595082503, 0.9), (10.650757595082503, 14.850757595082502, 0.9), (10.650757595082503, 18.450757595082504, 0.9), (10.650757595082503, 22.050757595082505, 0.9))
    posFichas[161]=((3.1809091140990047, -14.213917703090065, 0.9), (0.6353247018274333, -11.668333290818495, 0.9))
    posFichas[162]=((5.302229457658647, -12.092597359530423, 0.9), (2.756645045387075, -9.547012947258853, 0.9))
    posFichas[163]=((7.423549801218289, -9.97127701597078, 0.9), (4.877965388946717, -7.4256926036992095, 0.9))
    posFichas[164]=((9.544870144777931, -7.849956672411139, 0.9), (6.999285732506361, -5.3043722601395675, 0.9))
    posFichas[165]=((11.666190488337577, -5.728636328851496, 0.9), (9.120606076066004, -3.1830519165799247, 0.9))
    posFichas[166]=((13.787510831897219, -3.6073159852918533, 0.9), (11.241926419625646, -1.0617315730202819, 0.9))
    posFichas[167]=((15.90883117545686, -1.4859956417322104, 0.9), (13.363246763185288, 1.059588770539361, 0.9))
    posFichas[168]=((12.96456710674493, 5.700909114099003, 0.9), (15.48456710674493, 3.180909114099004, 0.9), (18.030151519016503, 0.6353247018274324, 0.9), (20.550151519016502, -1.8846752981725676, 0.9))
    posFichas[169]=((29.7, -25.198484809834994, 0.9), (33.3, -25.198484809834994, 0.9))
    posFichas[170]=((29.7, -22.198484809834994, 0.9), (33.3, -22.198484809834994, 0.9))
    posFichas[171]=((29.7, -19.198484809834994, 0.9), (33.3, -19.198484809834994, 0.9))
    posFichas[172]=((29.7, -16.198484809834994, 0.9), (33.3, -16.198484809834994, 0.9))
    posFichas[173]=((29.7, -13.198484809834994, 0.9), (33.3, -13.198484809834994, 0.9))
    posFichas[174]=((29.7, -10.198484809834994, 0.9), (33.3, -10.198484809834994, 0.9))
    posFichas[175]=((29.7, -7.198484809834994, 0.9), (33.3, -7.198484809834994, 0.9))
    posFichas[176]=((26.099999999999998, -4.198484809834994, 0.9), (29.7, -4.198484809834994, 0.9), (33.3, -4.198484809834994, 0.9), (36.9, -4.198484809834994, 0.9))
    posFichas[177]=((62.36467529817257, -11.668333290818495, 0.9), (59.819090885901, -14.213917703090065, 0.9))
    posFichas[178]=((60.24335495461293, -9.547012947258853, 0.9), (57.69777054234136, -12.092597359530423, 0.9))
    posFichas[179]=((58.12203461105329, -7.4256926036992095, 0.9), (55.576450198781714, -9.97127701597078, 0.9))
    posFichas[180]=((56.00071426749364, -5.304372260139567, 0.9), (53.45512985522207, -7.849956672411138, 0.9))
    posFichas[181]=((53.879393923934, -3.183051916579924, 0.9), (51.33380951166243, -5.728636328851495, 0.9))
    posFichas[182]=((51.75807358037436, -1.061731573020281, 0.9), (49.212489168102785, -3.6073159852918524, 0.9))
    posFichas[183]=((49.63675323681471, 1.0595887705393618, 0.9), (47.09116882454314, -1.4859956417322095, 0.9))
    posFichas[184]=((50.03543289325507, 5.700909114099005, 0.9), (47.51543289325507, 3.1809091140990047, 0.9), (44.969848480983494, 0.6353247018274333, 0.9), (42.44984848098349, -1.8846752981725667, 0.9))
    posFichas[185]=((73.3492424049175, 14.850757595082502, 0.9), (73.3492424049175, 18.450757595082504, 0.9))
    posFichas[186]=((70.3492424049175, 14.850757595082502, 0.9), (70.3492424049175, 18.450757595082504, 0.9))
    posFichas[187]=((67.3492424049175, 14.850757595082502, 0.9), (67.3492424049175, 18.450757595082504, 0.9))
    posFichas[188]=((64.3492424049175, 14.850757595082502, 0.9), (64.3492424049175, 18.450757595082504, 0.9))
    posFichas[189]=((61.3492424049175, 14.850757595082502, 0.9), (61.3492424049175, 18.450757595082504, 0.9))
    posFichas[190]=((58.3492424049175, 14.850757595082502, 0.9), (58.3492424049175, 18.450757595082504, 0.9))
    posFichas[191]=((55.3492424049175, 14.850757595082502, 0.9), (55.3492424049175, 18.450757595082504, 0.9))
    posFichas[192]=((52.3492424049175, 11.250757595082503, 0.9), (52.3492424049175, 14.850757595082502, 0.9), (52.3492424049175, 18.450757595082504, 0.9), (52.3492424049175, 22.050757595082505, 0.9))
    posFichas[193]=((59.819090885901, 47.515432893255074, 0.9), (62.36467529817257, 44.96984848098351, 0.9))
    posFichas[194]=((57.69777054234135, 45.39411254969543, 0.9), (60.243354954612926, 42.84852813742386, 0.9))
    posFichas[195]=((55.576450198781714, 43.27279220613579, 0.9), (58.12203461105329, 40.727207793864224, 0.9))
    posFichas[196]=((53.45512985522207, 41.151471862576145, 0.9), (56.00071426749364, 38.60588745030458, 0.9))
    posFichas[197]=((51.33380951166243, 39.030151519016506, 0.9), (53.879393923934, 36.48456710674494, 0.9))
    posFichas[198]=((49.212489168102785, 36.90883117545686, 0.9), (51.75807358037436, 34.363246763185295, 0.9))
    posFichas[199]=((47.09116882454314, 34.787510831897215, 0.9), (49.63675323681471, 32.24192641962564, 0.9))
    posFichas[200]=((42.44984848098349, 35.18619048833757, 0.9), (44.969848480983494, 32.66619048833757, 0.9), (47.51543289325507, 30.120606076066, 0.9), (50.03543289325507, 27.600606076066, 0.9))
    posFichas[201]=((17.7, 49.5, 0.9), (16.49, 52.5, 0.9), (15.279999999999998, 55.5, 0.9), (14.069999999999997, 58.5, 0.9))
    posFichas[202]=((-1.3492424049174971, 30.450757595082504, 0.9), (-4.349242404917497, 31.660757595082504, 0.9), (-7.349242404917497, 32.8707575950825, 0.9), (-10.349242404917497, 34.0807575950825, 0.9))
    posFichas[203]=((-1.3492424049174971, 2.850757595082503, 0.9), (-4.349242404917497, 1.640757595082503, 0.9), (-7.349242404917497, 0.4307575950825031, 0.9), (-10.349242404917497, -0.7792424049174969, 0.9))
    posFichas[204]=((17.7, -16.198484809834994, 0.9), (16.49, -19.198484809834994, 0.9), (15.279999999999998, -22.198484809834994, 0.9), (14.069999999999997, -25.198484809834994, 0.9))
    posFichas[205]=((45.3, -16.198484809834994, 0.9), (46.51, -19.198484809834994, 0.9), (47.72, -22.198484809834994, 0.9), (48.93, -25.198484809834994, 0.9))
    posFichas[206]=((64.3492424049175, 2.850757595082502, 0.9), (67.3492424049175, 1.6407575950825022, 0.9), (70.3492424049175, 0.4307575950825022, 0.9), (73.3492424049175, -0.7792424049174977, 0.9))
    posFichas[207]=((64.3492424049175, 30.4507575950825, 0.9), (67.3492424049175, 31.6607575950825, 0.9), (70.3492424049175, 32.8707575950825, 0.9), (73.3492424049175, 34.0807575950825, 0.9))
    posFichas[208]=((45.3, 49.5, 0.9), (46.51, 52.5, 0.9), (47.72, 55.5, 0.9), (48.93, 58.5, 0.9))
        
    return posFichas
