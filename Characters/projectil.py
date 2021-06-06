import pygame
import vectors
import pos_rel

class Projectil(pygame.sprite.Sprite):

    def __init__(self,pos,imatge,v,dany,ch):
        super().__init__()
        self.image=imatge
        self.rect=self.image.get_rect()
        rel0=self.rect.center
        rel1=pos
        self.rect.topleft=pos_rel.pos_rel(rel0,rel1,ch.arma)
        self.dany=dany
        self.count=0
        self.v=v
        self.p=ch

    def update(self,screen_size):#,g_sprites):
        scx,scy = screen_size
        self.count+=1
        vx,vy=self.v
        if self.p.temps == "past":
            vy += self.p.gravetat[1]
        self.v = (vx,vy)
        #print(vx,vy,sep="/")
        #vx,vy=esc_vect(self.vel,self.dir)
        self.rect.move_ip(round(vx+self.p.screen_speed),round(vy))

        if self.rect.top >= scy or self.rect.left >= scx or self.rect.right <= 0:
            self.kill()



        
        """sprites=pygame.sprite.spritecollide(self,g_sprites,False)
        for sp in sprites:
            sp.impacte(self.dany)
            self.kill()"""

    '''def tallant_a(self,g_sprites,AI,character,g_armes,sprites):
        sprites=pygame.sprite.spritecollide(self,g_sprites,False)
        for sp in sprites:
            if pygame.sprite.collide_mask(sp,self)!=None:
                sp.impacte(self.dany)
                self.kill()'''
