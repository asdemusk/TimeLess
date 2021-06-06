import pygame
import escalado
import copy

class Live(pygame.sprite.Sprite):

    def __init__(self,personatge):
        super().__init__()
        self.image=pygame.image.load("Image/Others/Heart.png")
        self.rect=self.image.get_rect()
        self.rect.center=personatge.rect.center
        self.g=True
        self.vy=0
        self.vx=0
        self.gravetat=escalado.drop_Live(personatge.s_c)
        self.rect_antiga=self.rect
        self.sc=personatge.s_c

    def update(self,s):
        self.rect_antiga=copy.deepcopy(self.rect)
        if self.g:
            aplica_gravetat(self)
        vy=self.vy
        self.rect.move_ip(round(s),round(vy))
        if self.rect.top<0 or self.rect.bottom>self.sc[1]:
            self.kill()

def aplica_gravetat(self):
    g=self.gravetat
    self.vy+=g[1]
    self.vx+=g[0]
