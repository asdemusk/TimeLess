import pygame

def decod():
    pressed=pygame.key.get_pressed()
    noms=[]
    for i in range(len(pressed)):
        if pressed[i]:
            noms.append(pygame.key.name(i))
    return noms
