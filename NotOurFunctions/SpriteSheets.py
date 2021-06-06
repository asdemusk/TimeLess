
import pygame

def crea_matriu_imatges(spritesheet, nfils, ncols):
        mides = ( spritesheet.get_width() // ncols,
                  spritesheet.get_height() // nfils )
        matriu = [[] for i in range(nfils)]
        for fila in range(nfils):
            for columna in range(ncols):
                tros = pygame.Rect( (mides[0] * columna, mides[1] * fila), mides )
                matriu[fila].append(spritesheet.subsurface(tros))
        return matriu

def amplia(imatge, amplada):
    ample, alt = imatge.get_size()
    nova_im = pygame.Surface((ample+amplada, alt))
    nova_im.blit(imatge, (0, 0))
    nova_im.blit(imatge, (ample, 0))
    return nova_im
