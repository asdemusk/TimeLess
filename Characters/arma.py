import pygame
import projectil
import imaging
import pos_rel
#import character
import ch_p
#import character_atributes as ch_a
import escalado
import math

class Arma(pygame.sprite.Sprite):

    def __init__(self,personatge,dany,d_pos,imatges,projectil,im_projectil,
                 d_orient,temps):
        super().__init__()
        self.im_list=imatges
        self.d_pos=d_pos[:2]
        self.d_disparar=d_pos[2]
        self.p=personatge
        self.projectil=projectil
        self.temps=temps
        if projectil:
            self.d_orient=0
        else:
            self.d_orient=d_orient
        if projectil:
            self.image=self.im_list[0]
        else:
            self.image=self.im_list[1]
        self.rect=self.image.get_rect()
        if projectil:
            self.rel0=d_pos[1][0]
        else:
            self.rel0=d_pos[1][1]
        self.rel1=d_pos[0][self.p.ifi[1]][-1]
        #self.rect.topleft=pos_rel.pos_rel(rel0,rel1,self.p)
        if projectil:
            self.im_projectil=im_projectil
            self.pos_disparar=self.d_disparar
            #print(self.pos_disparar)
        else:
            self.pos_disparar=self.im_projectil=None
        #self.dir=personatge.dir
        self.dany=dany
        self.atacant=False
        if isinstance(self.p,ch_p.Principal):
            self.n_atacs=2
        else:
            self.n_atacs=1
        #self.rect=self.image.get_rect
        #self.rect.topleft=pos_rel.pos_rel(self.rel0,self.rel1,self.p)
        #self.disparar=ch_a.disparar
        self.disparar=escalado.drop_Arma(self.p.factor)
        #print(self.disparar)
        
    def update(self,screen_size):#,g_sprites):
        d_o={"D":0,"E":1}
        if self.p.estat in (5,8):
            self.atacant=True
        else:
            self.atacant=False
        if not self.atacant:
            if isinstance(self.p,ch_p.Principal):
                self.n_atacs=2
            else:
                self.n_atacs=1
        e,o=self.p.ifi
        count=self.p.count//self.p.n
        d_ma,d_arma=self.d_pos
        if self.projectil:
            rel0=d_arma[d_o[o]]
            self.image=self.im_list[d_o[o]]
        else:
            if e in (5,8):
                orientacio=self.d_orient[o][count]
                self.image=self.im_list[self.d_orient[o][count]]
            else:
                orientacio=1
                self.image=self.im_list[1]
            rel0=d_arma[orientacio]
        self.rect=self.image.get_rect()
        if e in d_ma[o]:
            rel1=d_ma[o][e][count]
        else:
            rel1=d_ma[o][-1]
        #print(rel0,rel1)
        self.rect=self.image.get_rect()
        self.rect.topleft=pos_rel.pos_rel(rel0,rel1,self.p)

    '''def tallant_a(self,penya,AI,character,g_armes,sprites):
        AI.update(character,self,penya,g_armes,sprites)
        if self.atacant and self.n_atacs>0:
            #self.n_atacs-=1
            sprites=pygame.sprite.spritecollide(self,penya,False,pygame.sprite.collide_mask)
            #print(g_sprites.sprites())
            for sp in sprites:
                #print(sp)
                if sp!=self.p:
                    self.n_atacs-=1
                    sp.impacte(self.dany)'''

    def dispara(self,g_armes,sprites,v,current_level_time,armes_time_list):
        d_o={"D":0,"E":1}
        e,o=self.p.ifi
        #print(d_o[o])
        #print(self.temps)
        pos=self.pos_disparar[d_o[o]]
        #print(self.im_projectil)
        im=self.im_projectil[d_o[o]]
        vx,vy=v
        proj=projectil.Projectil(pos,im,(vx,vy),self.dany,self.p)
        g_armes.add(proj)
        armes_time_list[current_level_time].add(proj)
        sprites.add(proj,layer=1)

def crea_punt_disparar(time):
    return d_disparar[time]
