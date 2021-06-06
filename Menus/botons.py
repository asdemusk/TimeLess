import pygame

class Boto(pygame.sprite.Sprite):

    def __init__(self,menu,central_pos,text,tll,c_lletra,c_fons,n,active=True,c_res="yellow"):
        super().__init__()
        self.name=text
        self.active=active
        self.n=n
        self.menu=menu
        #self.tll=tll
        self.font=pygame.font.Font(None,tll)
        self.c_lletra=pygame.color.Color(c_lletra)
        self.c_fons=pygame.color.Color(c_fons)
        self.c_res=pygame.color.Color(c_res)
        b_t=self.font.render(text,True,self.c_lletra)
        rect_b_t=b_t.get_rect()
        a,h=rect_b_t.size
        self.image=pygame.surface.Surface((a+10,h+10))
        self.image.fill(self.c_fons)
        self.rect=self.image.get_rect()
        self.image.blit(b_t,(5,5))
        self.rect.center=central_pos
        w,he=self.rect.size
        self.res=pygame.sprite.Sprite()
        self.res.image=pygame.surface.Surface((w+10,he+10))
        self.res.image.fill(self.c_res)
        self.res.rect=self.res.image.get_rect()
        self.res.rect.center=central_pos
        self.res.image.set_alpha(0)
        self.resaltat=False

    def update(self,changing=False):
        mouse_pos=pygame.mouse.get_pos()
        if self.menu.ll_botons[self.menu.index]==self:
            self.res.image.set_alpha(255)
            self.resaltat=True
        else:
            self.res.image.set_alpha(0)
            self.resaltat=False

    def change(self,text,central_pos):
        self.name=text
        b_t=self.font.render(text,True,self.c_lletra)
        rect_b_t=b_t.get_rect()
        a,h=rect_b_t.size
        self.image=pygame.surface.Surface((a+10,h+10))
        self.image.fill(self.c_fons)
        self.rect=self.image.get_rect()
        self.image.blit(b_t,(5,5))
        self.rect.center=central_pos
        w,he=self.rect.size
        self.res=pygame.sprite.Sprite()
        self.res.image=pygame.surface.Surface((w+10,he+10))
        self.res.image.fill(self.c_res)
        self.res.rect=self.res.image.get_rect()
        self.res.rect.center=central_pos
        self.res.image.set_alpha(0)

class SoundB(pygame.sprite.Sprite):

    def __init__(self,pos,color,alpha,tipus):
        super().__init__()
        self.image=pygame.surface.Surface((500,30))
        self.rect=self.image.get_rect()
        self.rect.center=pos
        self.color=pygame.color.Color(color)
        self.image.fill(self.color)
        self.image.set_alpha(alpha)
        self.tipus=tipus

        def update(self):
            pass

class SoundI(pygame.sprite.Sprite):

    def __init__(self,color,b):
        super().__init__()
        w,h=b.rect.size
        self.ample=w
        self.x0=b.rect.left
        mides=round(w/20),h+20
        self.image=pygame.surface.Surface(mides)
        self.rect=self.image.get_rect()
        self.rect.centery=b.rect.centery
        self.tipus=b.tipus
        self.volum=troba_vol(self.tipus)
        self.pos()
        self.color=pygame.color.Color(color)
        self.image.fill(self.color)

    def update(self):
        self.pos()
        
    def pos(self):
        v=self.volum/100
        self.rect.centerx=round(self.x0+self.ample*v)

class BotoW(pygame.sprite.Sprite):

    def __init__(self,menu,central_pos,text,tll,c_lletra,c_fons,c_fons2,n,active=True,c_res="yellow"):
        super().__init__()
        self.name=text
        self.active=active
        self.n=n
        self.menu=menu
        self.font=pygame.font.Font(None,tll)
        self.c_lletra=pygame.color.Color(c_lletra)
        self.c_fons=pygame.color.Color(c_fons)
        self.c_res=pygame.color.Color(c_res)
        self.c_fons2=pygame.color.Color(c_fons2)
        b_t=self.font.render(text,True,self.c_lletra)
        rect_b_t=b_t.get_rect()
        a,h=rect_b_t.size
        im1=pygame.surface.Surface((a+10,h+10))
        im1.fill(self.c_fons)
        im2=pygame.surface.Surface((a+10,h+10))
        im2.fill(self.c_fons2)
        im1.blit(b_t,(5,5))
        im2.blit(b_t,(5,5))
        self.im=[im1,im2]
        self.i=0
        self.image=self.im[self.i]
        self.rect=self.image.get_rect()
        self.rect.center=central_pos
        w,he=self.rect.size
        self.res=pygame.sprite.Sprite()
        self.res.image=pygame.surface.Surface((w+10,he+10))
        self.res.image.fill(self.c_res)
        self.res.rect=self.res.image.get_rect()
        self.res.rect.center=central_pos
        self.res.image.set_alpha(0)
        self.resaltat=False

    def update(self,changing=False):
        self.image=self.im[self.i]
        if not changing:
            if self.menu.ll_botons[self.menu.index]==self:
                self.res.image.set_alpha(255)
                self.resaltat=True
            else:
                self.res.image.set_alpha(0)
                self.resaltat=False

def dins(pos,rect):
    xmin,ymin=rect.topleft
    xmax,ymax=rect.bottomright
    x,y=pos
    return xmin<=x<=xmax and ymin<=y<=ymax

def troba_vol(tipus):
    #print(tipus)
    fin=open("Music/Saves.txt","r")
    for line in fin:
        line=line.strip()
        tip,vol=line.split(": ")
        if tip==tipus:
            fin.close()
            return int(vol)
    raise Exception("No existe el volumen")
