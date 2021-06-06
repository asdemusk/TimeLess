import pygame

class Blood(pygame.sprite.Sprite):

    def __init__(self,screen_size):
        super().__init__()
        imatge=pygame.image.load("Image/Others/Blood.png")
        self.image=pygame.transform.scale(imatge,screen_size)
        self.rect=self.image.get_rect()
        self.rect.topleft=(0,0)
        #self.image.set_alpha(0)
        self.iniciar=False
        self.alpha=0
        self.image.set_alpha(self.alpha)
        self.acabar=False
        #print("Init",self.alpha,sep=": ")

    def update(self,ch):
        if self.iniciar:
            self.alpha=round(255*(1-ch.vida/100))
            self.image.set_alpha(self.alpha)
            self.iniciar=False
            self.acabar=True
        else:
            #act_alpha=self.image.get_alpha()
            if self.alpha>0:
                #print("Fuck yeah lml")
                self.alpha-=5
                if self.alpha<0:
                    self.alpha=0
                self.image.set_alpha(self.alpha)
            elif self.alpha==0:
                #print("Fuck yeah lml")
                self.acabar=False
        #print("Update",self.alpha,sep=": ")
        #print("Inicia: ",self.iniciar," / ", "Acabar: ",self.acabar,sep="")
