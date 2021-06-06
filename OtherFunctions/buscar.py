import pygame
#import ch_p

def busca(lista,tipo):
    for el in lista:
        if isinstance(el,tipo):
            return el
    raise Exception("Any type in this lista")
