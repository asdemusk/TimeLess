import pygame
import state_machine
import imaging
import arma
import canvi_estat
import vectors
import teclat
import escalado
import pos_rel
import copy
import character_atributes as ch_a
import random

@state_machine.acts_as_state_machine
class Character(pygame.sprite.Sprite):
    
    ESQUERRA=state_machine.State()
    DRETA=state_machine.State()
    QUIET=state_machine.State()#initial=True)
    SALTA=state_machine.State()
    AJUP=state_machine.State()
    #AIXECA=state_machine.State()
    ATACA=state_machine.State()
    MORT=state_machine.State()
    ATERRA=state_machine.State()
    ATAC_SALT=state_machine.State()
    AIRE=state_machine.State(initial=True)
    AJUPIT=state_machine.State()
    AIXECANT=state_machine.State()
    
    
    estats={"DRETA":0,"ESQUERRA":1,"QUIET":2,"SALTA":3,"AJUP":4,"ATACA":5,
            "MORT":6,"ATERRA":7,"ATAC_SALT":8,"AIRE":9,"AJUPIT":10,
            "AIXECANT":11}#,"AIXECA":10}

    ves_esquerra=state_machine.Event(from_states=(QUIET,DRETA,ATACA,ATERRA,AIXECANT)
                                     ,to_state=ESQUERRA)
    ves_dreta=state_machine.Event(from_states=(QUIET,ESQUERRA,ATACA,ATERRA,AIXECANT)
                                  ,to_state=DRETA)
    para=state_machine.Event(from_states=(ESQUERRA,ATACA,DRETA,ATERRA,AIXECANT,AIRE),
                             to_state=QUIET)
    salta=state_machine.Event(from_states=(QUIET,ESQUERRA,DRETA),to_state=SALTA)
    aterra=state_machine.Event(from_states=(AIRE,ATAC_SALT),to_state=ATERRA)
    atac_salt=state_machine.Event(from_states=(AIRE),to_state=ATAC_SALT)
    ajupir=state_machine.Event(from_states=(ATERRA,ESQUERRA,DRETA,QUIET),
                               to_state=AJUP)
    ajupit=state_machine.Event(from_states=AJUP,to_state=AJUPIT)
    aixecant=state_machine.Event(from_states=AJUPIT,to_state=AIXECANT)
    #aixecat=state_machine.Event(from_states=AIXECANT,to_satate=QUIET)
    ataca=state_machine.Event(from_states=(QUIET,ESQUERRA,DRETA,ATERRA),
                              to_state=ATACA) 
    mort=state_machine.Event(from_states=(QUIET,ESQUERRA,DRETA),
                             to_state=MORT)
    aire=state_machine.Event(from_states=(SALTA,ATAC_SALT,QUIET,ESQUERRA,DRETA,AJUPIT,AJUP,ATACA,ATERRA,AIXECANT,MORT),to_state=AIRE)    


    def __init__(self,pos_bottomleft,im_arma,dany,vida,projectil,files_imatges,
                 a_pers,d_pos_arma,screen_size,*imatges,**keyargs):
        pygame.sprite.Sprite.__init__(self)
        #print(imatges,files_imatges)
        self.s_c=screen_size
        self.do_kill = False
        self.speed = 0 #velocitat anviada a Scenery
        self.count=0
        self.im_list=imaging.crea_mat_gen(list(imatges),a_pers)
        self.estat=self.estats[self.current_state]
        self.files_imatges=files_imatges
        self.ifi=(2,"D")
        self.fila=self.files_imatges.index(self.ifi)
        #print(self.fila,imatges[13])
        #self.image=self.im_list[self.fila][self.count//self.n]
        self.nframes=len(self.im_list[self.fila])
        if projectil:
            if "im_projectil" in keyargs:
                im_projectil=keyargs["im_projectil"]
            else:
                raise Exception("'Projectil' image required")
        else:
            im_projectil=None
        if "temps" in keyargs:
            self.temps=keyargs["temps"]
        else:
            raise Exception("'temps' required")
        #self.rect=self.image.get_rect()
        #self.rect.bottomleft=pos_bottomleft
        self.vida=vida
        #self.dir=[0,0]
        self.orientacio=1
        #self.vel=-1
        self.vx=0 #velocitat speed
        self.vy=0 #velocitat vertical
        self.n=5 #numero de frames per passar imatge
        #self.vel=self.vy
        self.terra=False
        self.atac_estatic=not projectil
        if "ColRect" in keyargs:
            self.ColRect=keyargs["ColRect"]
        else:
            self.ColRect=None
        """if "principal" in keyargs:
            prin=keyargs["principal"]
            if isinstance(prin,bool):
                self.principal=prin
            else:
                raise Exception("'pricipal' atribute must be a boolean")
        else:
            self.principal=False"""
        self.factor=screen_size[1]/1280
        if not projectil:
            self.arma=arma.Arma(self,dany,d_pos_arma,im_arma,projectil,im_projectil,
                            d_orientacio,self.temps)
        else:
            self.arma=arma.Arma(self,dany,d_pos_arma,im_arma,projectil,im_projectil,
                            {"D":0,"E":1},self.temps)
        escalado.zoom(self,screen_size)
        self.image=self.im_list[self.fila][self.count//self.n]
        self.rect=self.image.get_rect()
        self.rect.bottomleft=pos_bottomleft
        self.arma.rect.topleft=pos_rel.pos_rel(self.arma.rel0,self.arma.rel1,self)
        self.rect_antiga=self.rect
        self.vel,self.velTrans,self.gravetat=escalado.drop_Character(screen_size,self.atac_estatic)
        self.ori=ch_a.ori

        self.max_temps_atac = 50
        self.temps_atac = random.randint(0,self.max_temps_atac)

        self.screen_speed=0

        self.colisioned_rect = self.rect


    def update(self,screen_size,speed):
        #n=3 #numero de frames per passar imatge
        width,height = screen_size
        if self.vida==0:
            if self.estat in (0,1,2):
                self.mort()
        if self.rect.top > height:
            self.do_kill = True
        self.count+=1
        #tec_events=teclat.decod()
        """if self.principal:
            #if self.estat==10 and "s" not in tec_events:
                #self.aixecant()
            if self.estat==2:
                if "d" in tec_events:
                    self.ves_dreta()
                elif "a" in tec_events:
                    self.ves_esquerra()
        if self.estat==9 and self.principal:
            #print("estat 9",end=" / ")
            if "d" in tec_events:
                #pers.vx=1
                self.vx=self.vel[9][0][0]
                #print("funciona 'dreta'")
            elif "a" in tec_events:
                #pers.vx=-1
                self.vx=self.vel[9][1][0]
                #print("funciona 'esquerra'")
            else:
                self.vx=0
                #print("ja no")
        if self.estat in (0,1,2) and self.principal:
            if "w" in tec_events:
                self.salta()"""
        #print(self.estat)
        if self.count>=self.nframes*self.n:
            if self.estat==6:
                self.count=0
                self.do_kill=True
            elif self.estat==4:
                self.ajupit()
            elif self.estat==3:
                self.aire()
                #self.dir[1]=-3
                #self.vy=-25
                self.vy=self.vel[9][0][1]
                #self.vel=25
            elif self.estat==8:
                vy=self.vy
                self.aire()
                self.vy=vy
            elif self.estat==11:
                #print("Fuck yeah lml")
                self.para()
            elif self.estat==5:
                self.para()
            elif self.estat==7:
                self.para()
            else:
                self.count=0
        self.rect_antiga=copy.deepcopy(self.rect)       
        if self.estat in (9,8):
            aplica_gravetat(self)
        #vx,vy=vectors.esc_vect(self.vel,self.dir)
        vy=self.vy
        """if self.principal:
            vx=0
            s=0
        else:"""
        vx=self.vx
        s=speed
        self.rect.move_ip(round(vx+s),round(vy))
        #print(self.rect_antiga.right)#,self.rect.right)
        if not self.terra:
            #if self.vy==0:
            #if self.vel==0:
               #self.vel=3
                #self.vy=1
            #if self.dir[1]==0:
                #self.dir[1]=-1
                #self.vy=-1
            if self.estat not in (9,8):
                self.aire()
        self.fila=self.files_imatges.index(self.ifi)
        #print(self.count,self.nframes*3,self.estat)
        self.image=self.im_list[self.fila][self.count//self.n]
        self.arma.update(screen_size)
        #print(self.vel*self.dir[0])
        self.speed = round(self.vx)
        #print(self.vel,self.dir,self.current_state)
        #print(self.vx,self.current_state)
        #print(self.current_state)
        #print(self.vx,self.principal,sep="/")
        #if not self.principal:
            #print(vx,s,sep="/")
        #print(self.vida)
        self.screen_speed=speed
            
    @state_machine.after("ves_esquerra")
    @state_machine.after("ves_dreta")
    @state_machine.after("para")
    @state_machine.after("salta")
    @state_machine.after("aterra")
    @state_machine.after("atac_salt")
    @state_machine.after("ajupir")
    @state_machine.after("ataca")
    @state_machine.after("mort")
    @state_machine.after("aire")
    @state_machine.after("ajupit")
    @state_machine.after("aixecant")
    #@state_machine.after("aixecat")
    def transicio(self):
        estat_i=self.current_state
        self.count=0
        self.estat=self.estats[estat_i]
        canvi_estat.canvi(self)
        #print(self.orientacio)
        ch_a.canvia_v(self)
        #print("funciona")
        self.fila=self.files_imatges.index(self.ifi)
        self.nframes=len(self.im_list[self.fila])

    def impacte(self,dany):
        self.vida-=dany
        if self.vida<0:
            self.vida=0

def aplica_gravetat(self):
    g=self.gravetat
    self.vy+=g[1]
    self.vx+=g[0]

d_orientacio={"D":(1,1,2,1,0,0,1,1),
              "E":(1,1,0,1,2,2,1,1)}
