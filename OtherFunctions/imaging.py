import pygame
import vectors
import SpriteSheets

"""def escala(matriu,escala):
    for i in range(len(matriu)):
        for j in range(len(matriu[i])):
            a,h=matriu[i][j].get_size()
            matriu[i][j]=pygame.transform.scale(matriu[i][j],vectors.esc_vect(escala,[a,h]))
    return matriu"""

def crea_mat_gen(l_args,amplada):
    im=[]
    for el in l_args:
        #n_ima=el
        #ima=pygame.image.load(n_ima)
        im+=crea_matriu_imatges_1(el,1,amplada)
    return im

def crea_matriu_imatges_1(spritesheet, nfils, amplada):
    mides = ( amplada,spritesheet.get_height() // nfils )
    ncols = spritesheet.get_width() // amplada
    matriu = [[] for i in range(nfils)]
    for fila in range(nfils):
        for columna in range(ncols):
            tros = pygame.Rect( (mides[0] * columna, mides[1] * fila), mides )
            matriu[fila].append(spritesheet.subsurface(tros))
    return matriu
