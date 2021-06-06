
import pygame
import state_machine
from SpriteSheets import *


class BaseSprite(pygame.sprite.Sprite):
    def __init__(self, ImFile, MatDim, frame_speed, screen_size, ColRect=[]):

        if (ColRect != []) and (len(ColRect[0]) != len(ColRect[1])):
            raise Exception('Rectangle dimensions and positions dont match')
        
        pygame.sprite.Sprite.__init__(self)

        self.layer = 0
        self.fila = 0
        self.count = 0
        self.screen_size = screen_size
        self.nframes = MatDim[1]
        
        sf = pygame.image.load('Image/'+ImFile)
        self.im = crea_matriu_imatges(sf,MatDim[0],MatDim[1])
        self.num_temps = MatDim[0]
        self.image = self.im[self.estats.index(self.current_state)][0]
        self.rect = self.image.get_rect()
        self.ColRect = ColRect
        self.frame_speed = frame_speed

    def update(self):

        self.count = self.count + 1
        if self.count == self.nframes * self.frame_speed:
            self.count = 0
        fila = self.fila
        columna = self.count // self.frame_speed
        self.image = self.im[fila][columna]
