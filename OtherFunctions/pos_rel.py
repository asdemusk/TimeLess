import pygame

def pos_rel(punt_arma,punt_pers,pers):
    xa,ya=punt_arma
    xp,yp=punt_pers
    x=pers.rect.x + xp - xa
    y=pers.rect.y + yp - ya
    return x,y
