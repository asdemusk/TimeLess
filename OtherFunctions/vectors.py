import math

def esc_vect(esc,vect):
    return esc_vect_i(esc,vect,0)

def esc_vect_i(esc,vect,i):
    if i>=len(vect):
        v=[]
    else:
        v=[int(vect[i]*esc)]
        v+=(esc_vect_i(esc,vect,i+1))
    return v

def normalitza(v):
    x,y=v
    #norma=math.sqrt(x**2+y**2)
    norma = modul(v)
    return x/norma,y/norma

def modul(v):
    x,y=v
    return math.sqrt(x**2+y**2)

def distx(v1,v2):
    v1x = v1[0]
    v2x = v2[0]
    return v2x-v1x

def disty(v1,v2):
    v1y = v1[1]
    v2y = v2[1]
    return v2y-v1y

def dist(v1,v2):
    v = dif(v1,v2)
    return modul(v)

def dif(v1,v2):
    return distx(v1,v2), disty(v1,v2)
