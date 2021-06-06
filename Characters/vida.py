import pygame
import copy

class Vida(pygame.sprite.Sprite):

    def __init__(self,ch,pos=(10,10),font=None):
        super().__init__()
        self.ch=ch
        self.vida=self.ch.vida
        if font==None:
            font=pygame.font.Font(None,32)
        self.font=font
        self.color=pygame.color.Color("white")
        self.image=self.font.render(str(self.vida),True,self.color)
        self.rect=self.image.get_rect()
        self.pos=pos
        self.rect.topleft=pos

    def update(self,ch,joc):
        self.vida=self.ch.vida
        self.image=self.font.render(str(self.vida),True,self.color)
        self.rect=self.image.get_rect()
        self.rect.topleft=self.pos

class Vida_2(pygame.sprite.Sprite):

    def __init__(self,ch,pos=(10,10)):
        super().__init__()
        self.ch=ch
        self.vida=self.ch.vida
        self.ini_vida=copy.deepcopy(self.vida)
        self.color_fons=pygame.color.Color("grey")
        self.color_vida=pygame.color.Color("red")
        self.mides=a,h=(350,15)
        self.image=pygame.surface.Surface(self.mides)
        self.fons=pygame.surface.Surface(self.mides)
        self.fons.fill(self.color_fons)
        self.fons.set_alpha(255//3)
        self.image.blit(self.fons,(0,0))
        self.v=pygame.surface.Surface((int(a*self.vida/self.ini_vida),h))
        self.v.fill(self.color_vida)
        self.image.blit(self.v,(0,0))
        self.rect=self.image.get_rect()
        self.pos=pos
        self.rect.topleft=pos

    def update(self,ch,joc):
        a,h=self.mides
        self.vida=self.ch.vida
        self.image=pygame.surface.Surface(self.mides)
        self.fons=pygame.surface.Surface(self.mides)
        self.fons.fill(self.color_fons)
        self.fons.set_alpha(255//2)
        self.image.blit(self.fons,(0,0))
        self.v=pygame.surface.Surface((int(a*self.vida/self.ini_vida),h))
        self.v.fill(self.color_vida)
        self.image.blit(self.v,(0,0))
        self.rect.topleft=self.pos

"""class Vides(pygame.sprite.Sprite):

    def __init__(self,ch):
        super().__init__()
        self.sep=5
        self.ch=ch
        self.font=pygame.font.Font(None,30)
        self.vides=self.ch.vides
        self.c_ll=pygame.color.Color("white")
        self.h=pygame.sprite.Sprite()
        self.h.image=pygame.image.load("Image/Others/Heart.png")
        self.h.rect=self.h.image.get_rect()
        self.ll=pygame.sprite.Sprite()
        self.ll.image=self.font.render("x "+str(self.vides),True,self.c_ll)
        self.ll.rect=self.ll.image.get_rect()

    def update(self):
        print("entra")
        self.vides=self.ch.vides
        print(self.vides)
        self.ll.image=self.font.render("x "+str(self.vides),True,self.c_ll)
        self.ll.rect=self.ll.image.get_rect()
        x,y=self.h.rect.midright
        self.ll.rect.midleft=(x+self.sep,y)"""

class Vides_h(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("Image/Others/Heart.png")
        self.rect=self.image.get_rect()

    def update(self,ch,joc):
        pass

class Vides_ll(pygame.sprite.Sprite):

    def __init__(self,ch):
        super().__init__()
        #self.ch=ch
        self.vides=0#ch.joc.etapa_estat["Game"].vides
        self.sep=5
        self.font=pygame.font.Font(None,30)
        self.c_ll=pygame.color.Color("white")
        self.image=self.font.render("x "+str(self.vides),True,self.c_ll)
        self.rect=self.image.get_rect()

    def update(self,ch,joc):
        #self.vides=self.ch.vides
        #print(joc.vides)
        self.vides=joc.vides
        self.image=self.font.render("x "+str(self.vides),True,self.c_ll)
        self.rect=self.image.get_rect()
        self.rect.topleft=self.pos

def crea_vida(ch,n,pos=(0,0),font=None):
    if n==1:
        vida=Vida(ch)#,pos=(0,0),font=None)
    elif n==2:
        vida=Vida_2(ch)#,pos=(0,0))
    else:
        raise Exception("Type of 'vida' incorrect")
    vides_h=Vides_h()
    vides_ll=Vides_ll(ch)
    x=vida.rect.right
    y=vida.rect.centery
    vides_h.rect.midleft=(x+5,y)
    xll=vides_h.rect.right
    vides_ll.rect.midleft=(xll+vides_ll.sep,y)
    vides_ll.pos=vides_ll.rect.topleft
    g_vida=pygame.sprite.Group(vida,vides_h,vides_ll)
    return g_vida
