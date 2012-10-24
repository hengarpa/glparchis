# -*- coding: utf-8 -*-
import math
def posfichas8(maxcasillas, posCasillas):
    """La posici´on de fichas de radio 1.4 es decir diametro 2.8 se colocan centradas en 1.5 de alto
    En lo ancho ser´a a 0.3 de los extremos , es dicir a 1.7 el centro y a 5,3
    
    En las oblicuas se mete 0.5 del lado en el que est´a oblicuo
    """
    def n(id):
        """Para horizontales"""
        return ((posCasillas[id][0]+1.7, posCasillas[id][1]+1.5, 0.9), (posCasillas[id][0]+5.3, posCasillas[id][1]+1.5, 0.9))
    def w(id):
        """Para verticales"""
        return ((posCasillas[id][0]+1.5-3, posCasillas[id][1]+1.7, 0.9), (posCasillas[id][0]+1.5-3, posCasillas[id][1]+5.3, 0.9))
    def nw(id):
        return ((posCasillas[id][0]+r1*math.cos(alfa1), posCasillas[id][1]+r1*math.sin(alfa1), 0.9), (posCasillas[id][0]+r2*math.cos(alfa2), posCasillas[id][1]+r2*math.sin(alfa2), 0.9))
    def e(id):
        """Para verticales y giradas"""
        return ((posCasillas[id][0]+1.5, posCasillas[id][1]+1.7-7, 0.9), (posCasillas[id][0]+1.5, posCasillas[id][1]+5.3-7, 0.9))
    """Para nw
    C1 hace un angulo con el centro  0 de arctag 1.5/1.7+pi/4 =1.5083775167989393 rad
    y el radio es raix de 1.5^2+1.7^2= 2.2671568097509267
    
    c2 hace un angulo con el centro O de arctag 1.5/5.3 + pi/4 =1.0612040619859708
    y el radio es raix de 1.5^2+5.3^2= 5.508175741568165
    
    C3 recortando por 1.7
    
    C4 recortando por 5.3"""
    alfa1=math.atan(1.5/1.7)+math.pi/4
    r1=math.sqrt(1.5*1.5+1.7*1.7)
    alfa2=math.atan(1.5/5.3)+math.pi/4
    r2=math.sqrt(1.5*1.5+5.3*5.3)
    alfa3=math.atan(1.5/2.2)+math.pi/4
    r3=math.sqrt(2.2*2.2+5.3*5.3)
    alfa4=math.atan(1.5/4.8)+math.pi/4
    r4=math.sqrt(1.5*1.5+4.8*4.8)
    a=7*math.sqrt(2)/2
    b=3*math.sqrt(2)/2

    posFichas=[None]*maxcasillas
    posFichas[0]=((0, 0, 0.9), (0, 0, 0.9))
    posFichas[1]=n(1)
    posFichas[2]=n(2)
    posFichas[3]=n(3)
    posFichas[4]=n(4)
    posFichas[5]=n(5)
    posFichas[6]=n(6)
    posFichas[7]=n(7)
    posFichas[8]=((23.4, 40.5, 0.9), (26.3, 40.5, 0.9))

    posFichas[9]=((posCasillas[9][0]+r1*math.cos(alfa1)-a+b, posCasillas[9][1]+r1*math.sin(alfa1)-a-b, 0.9), (posCasillas[9][0]+r4*math.cos(alfa4)-a+b, posCasillas[9][1]+r4*math.sin(alfa4)-a-b, 0.9))
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
    posFichas[25]=((posCasillas[25][0]+r3*math.cos(alfa3)-a+b, posCasillas[25][1]+r3*math.sin(alfa3)-a-b-3, 0.9), (posCasillas[25][0]+r2*math.cos(alfa2)-a+b, posCasillas[25][1]+r2*math.sin(alfa2)-a-b, 0.9))
    posFichas[26]=((7.650757595082503, 21.850757595082502, 0.9), (7.650757595082503, 24.950757595082504, 0.9))
    posFichas[27]=w(27)
    posFichas[28]=w(28)
    posFichas[29]=w(29)
    posFichas[30]=w(30)
    posFichas[31]=w(31)
    posFichas[32]=w(32)
    posFichas[33]=w(33)
    posFichas[34]=w(34)
    posFichas[35]=w(35)
    posFichas[36]=w(36)
    posFichas[37]=w(37)
    posFichas[38]=w(38)
    posFichas[39]=w(39)
    posFichas[40]=w(40)
    posFichas[41]=w(41)
    posFichas[42]=((7.650757595082503, 8.350757595082503, 0.9), (7.650757595082503, 11.450757595082504, 0.9))

    posFichas[43]=((0, 0, 0.9), (0, 0, 0.9))
    posFichas[44]=((0, 0, 0.9), (0, 0, 0.9))
    posFichas[45]=((0, 0, 0.9), (0, 0, 0.9))
    posFichas[46]=((0, 0, 0.9), (0, 0, 0.9))
    posFichas[47]=((0, 0, 0.9), (0, 0, 0.9))
    posFichas[48]=((0, 0, 0.9), (0, 0, 0.9))
    posFichas[49]=((0, 0, 0.9), (0, 0, 0.9))
    posFichas[50]=((0, 0, 0.9), (0, 0, 0.9))
    posFichas[51]=((0, 0, 0.9), (0, 0, 0.9))
    posFichas[52]=((0, 0, 0.9), (0, 0, 0.9))
    posFichas[53]=((0, 0, 0.9), (0, 0, 0.9))
    posFichas[54]=((0, 0, 0.9), (0, 0, 0.9))
    posFichas[55]=((0, 0, 0.9), (0, 0, 0.9))
    posFichas[56]=((0, 0, 0.9), (0, 0, 0.9))
    posFichas[57]=((0, 0, 0.9), (0, 0, 0.9))
    posFichas[58]=((0, 0, 0.9), (0, 0, 0.9))
    posFichas[59]=((0, 0, 0.9), (0, 0, 0.9))
    posFichas[60]=((23.2, -7.198484809834994, 0.9), (26.3, -7.198484809834994, 0.9))
    posFichas[61]=n(61)
    posFichas[62]=n(62)
    posFichas[63]=n(63)
    posFichas[64]=n(64)
    posFichas[65]=n(65)
    posFichas[66]=n(66)
    posFichas[67]=n(67)
    posFichas[68]=n(68)
    posFichas[69]=n(69)
    posFichas[70]=n(70)
    posFichas[71]=n(71)
    posFichas[72]=n(72)
    posFichas[73]=n(73)
    posFichas[74]=n(74)
    posFichas[75]=n(75)
    posFichas[76]=((36.7, -7.198484809834994, 0.9), (39.8, -7.198484809834994, 0.9))
    posFichas[77]=((0, 0, 0.9), (0, 0, 0.9))
    posFichas[78]=((0, 0, 0.9), (0, 0, 0.9))
    posFichas[79]=((0, 0, 0.9), (0, 0, 0.9))
    posFichas[80]=((0, 0, 0.9), (0, 0, 0.9))
    posFichas[81]=((0, 0, 0.9), (0, 0, 0.9))
    posFichas[82]=((0, 0, 0.9), (0, 0, 0.9))
    posFichas[83]=((0, 0, 0.9), (0, 0, 0.9))
    posFichas[84]=((0, 0, 0.9), (0, 0, 0.9))
    posFichas[85]=((0, 0, 0.9), (0, 0, 0.9))
    posFichas[86]=((0, 0, 0.9), (0, 0, 0.9))
    posFichas[87]=((0, 0, 0.9), (0, 0, 0.9))
    posFichas[88]=((0, 0, 0.9), (0, 0, 0.9))
    posFichas[89]=((0, 0, 0.9), (0, 0, 0.9))
    posFichas[90]=((0, 0, 0.9), (0, 0, 0.9))
    posFichas[91]=((0, 0, 0.9), (0, 0, 0.9))
    posFichas[92]=((0, 0, 0.9), (0, 0, 0.9))
    posFichas[93]=((0, 0, 0.9), (0, 0, 0.9))
    posFichas[94]=((55.3492424049175, 8.350757595082502, 0.9), (55.3492424049175, 11.450757595082504, 0.9))
    posFichas[95]=e(95)
    posFichas[96]=e(96)
    posFichas[97]=e(97)
    posFichas[98]=e(98)
    posFichas[99]=e(99)
    posFichas[100]=e(100)
    posFichas[101]=e(101)
    posFichas[102]=e(102)
    posFichas[103]=e(103)
    posFichas[104]=e(104)
    posFichas[105]=e(105)
    posFichas[106]=e(106)
    posFichas[107]=e(107)
    posFichas[108]=e(108)
    posFichas[109]=e(109)
    posFichas[110]=((55.3492424049175, 21.850757595082502, 0.9), (55.3492424049175, 24.9507575950825, 0.9))
    posFichas[111]=((0, 0, 0.9), (0, 0, 0.9))
    posFichas[112]=((0, 0, 0.9), (0, 0, 0.9))
    posFichas[113]=((0, 0, 0.9), (0, 0, 0.9))
    posFichas[114]=((0, 0, 0.9), (0, 0, 0.9))
    posFichas[115]=((0, 0, 0.9), (0, 0, 0.9))
    posFichas[116]=((0, 0, 0.9), (0, 0, 0.9))
    posFichas[117]=((0, 0, 0.9), (0, 0, 0.9))
    posFichas[118]=((0, 0, 0.9), (0, 0, 0.9))
    posFichas[119]=((0, 0, 0.9), (0, 0, 0.9))
    posFichas[120]=((0, 0, 0.9), (0, 0, 0.9))
    posFichas[121]=((0, 0, 0.9), (0, 0, 0.9))
    posFichas[122]=((0, 0, 0.9), (0, 0, 0.9))
    posFichas[123]=((0, 0, 0.9), (0, 0, 0.9))
    posFichas[124]=((0, 0, 0.9), (0, 0, 0.9))
    posFichas[125]=((0, 0, 0.9), (0, 0, 0.9))
    posFichas[126]=((0, 0, 0.9), (0, 0, 0.9))
    posFichas[127]=((0, 0, 0.9), (0, 0, 0.9))
    posFichas[128]=((36.7, 40.5, 0.9), (39.8, 40.5, 0.9))
    posFichas[129]=n(129)
    print (posFichas[129])
    posFichas[130]=n(130)
    posFichas[131]=n(131)
    posFichas[132]=n(132)
    posFichas[133]=n(133)
    posFichas[134]=n(134)
    posFichas[135]=n(135)
    posFichas[136]=n(136)
    posFichas[137]=n(137)
    posFichas[138]=n(138)
    posFichas[139]=n(139)
    posFichas[140]=n(140)
    posFichas[141]=n(141)
    posFichas[142]=n(142)
    posFichas[143]=n(143)
    posFichas[144]=((0, 0, 0.9), (0, 0, 0.9), (0, 0, 0.9), (0, 0, 0.9))
    posFichas[145]=((0, 0, 0.9), (0, 0, 0.9))
    posFichas[146]=((0, 0, 0.9), (0, 0, 0.9))
    posFichas[147]=((0, 0, 0.9), (0, 0, 0.9))
    posFichas[148]=((0, 0, 0.9), (0, 0, 0.9))
    posFichas[149]=((0, 0, 0.9), (0, 0, 0.9))
    posFichas[150]=((0, 0, 0.9), (0, 0, 0.9))
    posFichas[151]=((0, 0, 0.9), (0, 0, 0.9))
    posFichas[152]=((0, 0, 0.9), (0, 0, 0.9), (0, 0, 0.9), (0, 0, 0.9))
    posFichas[153]=w(153)
    posFichas[154]=w(154)
    posFichas[155]=w(155)
    posFichas[156]=w(156)
    posFichas[157]=w(157)
    posFichas[158]=w(158)
    posFichas[159]=w(159)
    posFichas[160]=((0, 0, 0.9), (0, 0, 0.9), (0, 0, 0.9), (0, 0, 0.9))
    posFichas[161]=((0, 0, 0.9), (0, 0, 0.9))
    posFichas[162]=((0, 0, 0.9), (0, 0, 0.9))
    posFichas[163]=((0, 0, 0.9), (0, 0, 0.9))
    posFichas[164]=((0, 0, 0.9), (0, 0, 0.9))
    posFichas[165]=((0, 0, 0.9), (0, 0, 0.9))
    posFichas[166]=((0, 0, 0.9), (0, 0, 0.9))
    posFichas[167]=((0, 0, 0.9), (0, 0, 0.9))
    posFichas[168]=((0, 0, 0.9), (0, 0, 0.9), (0, 0, 0.9), (0, 0, 0.9))
    posFichas[169]=((0, 0, 0.9), (0, 0, 0.9))
    posFichas[170]=((0, 0, 0.9), (0, 0, 0.9))
    posFichas[171]=((0, 0, 0.9), (0, 0, 0.9))
    posFichas[172]=((0, 0, 0.9), (0, 0, 0.9))
    posFichas[173]=((0, 0, 0.9), (0, 0, 0.9))
    posFichas[174]=((0, 0, 0.9), (0, 0, 0.9))
    posFichas[175]=((0, 0, 0.9), (0, 0, 0.9))
    posFichas[176]=((0, 0, 0.9), (0, 0, 0.9), (0, 0, 0.9), (0, 0, 0.9))
    posFichas[177]=((0, 0, 0.9), (0, 0, 0.9))
    posFichas[178]=((0, 0, 0.9), (0, 0, 0.9))
    posFichas[179]=((0, 0, 0.9), (0, 0, 0.9))
    posFichas[180]=((0, 0, 0.9), (0, 0, 0.9))
    posFichas[181]=((0, 0, 0.9), (0, 0, 0.9))
    posFichas[182]=((0, 0, 0.9), (0, 0, 0.9))
    posFichas[183]=((0, 0, 0.9), (0, 0, 0.9))
    posFichas[184]=((0, 0, 0.9), (0, 0, 0.9), (0, 0, 0.9), (0, 0, 0.9))
    posFichas[185]=e(185)
    posFichas[186]=e(186)
    posFichas[187]=e(187)
    posFichas[188]=e(188)
    posFichas[189]=e(189)
    posFichas[190]=e(190)
    posFichas[191]=e(191)
    posFichas[192]=((0, 0, 0.9), (0, 0, 0.9), (0, 0, 0.9), (0, 0, 0.9))
    posFichas[193]=((0, 0, 0.9), (0, 0, 0.9))
    posFichas[194]=((0, 0, 0.9), (0, 0, 0.9))
    posFichas[195]=((0, 0, 0.9), (0, 0, 0.9))
    posFichas[196]=((0, 0, 0.9), (0, 0, 0.9))
    posFichas[197]=((0, 0, 0.9), (0, 0, 0.9))
    posFichas[198]=((0, 0, 0.9), (0, 0, 0.9))
    posFichas[199]=((0, 0, 0.9), (0, 0, 0.9))
    posFichas[200]=((0, 0, 0.9), (0, 0, 0.9), (0, 0, 0.9), (0, 0, 0.9))
    posFichas[201]=((10, 10, 0.9), (11, 11, 0.9), (12, 12, 0.9), (13, 13, 0.9))
    posFichas[202]=((0, 0, 0.9), (0, 0, 0.9), (0, 0, 0.9), (0, 0, 0.9))
    posFichas[203]=((0, 0, 0.9), (0, 0, 0.9), (0, 0, 0.9), (0, 0, 0.9))
    posFichas[204]=((0, 0, 0.9), (0, 0, 0.9), (0, 0, 0.9), (0, 0, 0.9))
    posFichas[205]=((0, 0, 0.9), (0, 0, 0.9), (0, 0, 0.9), (0, 0, 0.9))
    posFichas[206]=((0, 0, 0.9), (0, 0, 0.9), (0, 0, 0.9), (0, 0, 0.9))
    posFichas[207]=((0, 0, 0.9), (0, 0, 0.9), (0, 0, 0.9), (0, 0, 0.9))
    posFichas[208]=((0, 0, 0.9), (0, 0, 0.9), (0, 0, 0.9), (0, 0, 0.9))

    return posFichas
