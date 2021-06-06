import pygame

import character
import load
import canvi_estat
import events
import colision
import personatges
import ch_p
import escalado
import vida
import motor
import dany

import Scenery
import state_machine
import ColRect
from level_loading import *

from AI_it_hurts import *

#AI = AI()
mostra_ColRect = False
CRP = 'Scenery/'

def load_image(temps,proj,pantalla,principal=False):
    im_personatge,files_imatges=load.load_images_personatge(temps,proj,principal)
    #print(temps)
    im_arma,projectil=load.load_arma(temps,proj)
    #print(type(projectil[1]))
    d_pos_arma=load.carrega_d(temps,proj,principal)
    if proj:
        if temps=="past":
            escalado.zoom(im_arma,pantalla,fact=3/8,especial="im_arma")
            escalado.zoom(d_pos_arma,pantalla,fact=5/8,especial="pos_arma")
            escalado.zoom(d_pos_arma,pantalla,fact=5/8,especial="dispara")
            escalado.zoom(projectil,pantalla,fact=1/2,especial="projectil")
        elif temps=="present":
            escalado.zoom(projectil,pantalla,fact=3/4,especial="projectil")
        elif temps=="future":
            escalado.zoom(projectil,pantalla,fact=1.5,especial="projectil")
    return im_personatge,im_arma,projectil,files_imatges,d_pos_arma

def inicia_personatges(screen_size,joc,*personatges):
    g_pers=pygame.sprite.LayeredUpdates()
    g_armes=pygame.sprite.LayeredUpdates()
    g_projectils=pygame.sprite.LayeredUpdates()
    sprites=pygame.sprite.LayeredUpdates()
    penya=pygame.sprite.LayeredUpdates()
    penya_past=pygame.sprite.LayeredUpdates()
    penya_present=pygame.sprite.LayeredUpdates()
    penya_future=pygame.sprite.LayeredUpdates()
    armes_past=pygame.sprite.LayeredUpdates()
    armes_present=pygame.sprite.LayeredUpdates()
    armes_future=pygame.sprite.LayeredUpdates()
    #g_principal=pygame.sprite.Group()
    for i in range(len(personatges)):
        #print(i)
        el=personatges[i]
        temps,pos,dany,vida,projectil,a_pers=el
        #pers,arma,proj,files,d_pos_arma=load_image(temps,projectil,screen_size,True)
        if i==0:
            pers,arma,proj,files,d_pos_arma=load_image(temps,projectil,screen_size,True)
            #print("principal",temps)
            if projectil:
                char=ch_p.Principal(pos,arma,dany,vida,True,files,a_pers
                                    ,d_pos_arma,screen_size,joc,*pers,im_projectil=proj,temps=temps)
            else:
                char=ch_p.Principal(pos,arma,dany,vida,False,files,a_pers
                                    ,d_pos_arma,screen_size,joc,*pers,temps=temps)#,principal=True)
                g_armes.add(char.arma)
            principal=char
            g_pers.add(char)
            #print(char.principal)
        else:
            pers,arma,proj,files,d_pos_arma=load_image(temps,projectil,screen_size)
            #print("secundari",temps)
            if projectil:
                char=character.Character(pos,arma,dany,vida,True,files,a_pers,
                                         d_pos_arma,screen_size,
                                         *pers,im_projectil=proj,temps=temps)
            else:
                char=character.Character(pos,arma,dany,vida,False,files,a_pers
                                         ,d_pos_arma,screen_size,*pers,temps=temps)
                g_armes.add(char.arma)
            g_pers.add(char)
        penya.add(char)
        if isinstance(char,ch_p.Principal) or char.temps == "past":
            #print(isinstance(char,ch_p.Principal),"past")
            penya_past.add(char)
            armes_past.add(char.arma)
        if isinstance(char,ch_p.Principal) or char.temps == "present":
            #print(isinstance(char,ch_p.Principal),"present")
            penya_present.add(char)
            armes_present.add(char.arma)
        if isinstance(char,ch_p.Principal) or char.temps == "future":
            #print(isinstance(char,ch_p.Principal),"future")
            penya_future.add(char)
            armes_future.add(char.arma)
        sprites.add(char,layer=2)
        sprites.add(char.arma,layer=0)
    penya_time_list = [penya_past,penya_present,penya_future]
    armes_time_list = [armes_past,armes_present,armes_future]
    return g_pers,g_armes,g_projectils,principal,sprites,penya,penya_time_list,armes_time_list

def ini_sprites(screen_size,joc,nivell,*personatges):
    Levels_group = pygame.sprite.GroupSingle() # grup de Sprites
    #Test_block_group = pygame.sprite.LayeredUpdates()

    g_pers,g_armes,g_projectils,g_principal,sprites,penya, penya_time_list,armes_time_list = inicia_personatges(screen_size,joc,*personatges)
    
    levels_sprites = load_levels(nivell,screen_size)#'Level_data.txt',screen_size)
    for i in range(len(levels_sprites)):
        level = levels_sprites[i]
        level_group = pygame.sprite.GroupSingle()
        #Levels_group.add(level)
        level_group.add(level)
        levels_sprites[i] = level_group

    #Test_block = ColRect.ColRectObj((1,1),(32,10),(20,20),screen_size)
    #Test_block_group.add(Test_block)
    t_vida=vida.crea_vida(g_principal,2)

    blood=pygame.sprite.Group(dany.Blood(screen_size))
    
    return levels_sprites, Levels_group, g_pers,g_armes,g_projectils,g_principal,sprites,penya,t_vida,penya_time_list,armes_time_list,blood

'''def tracta_events(heroi):
    speed = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            return True
        elif event.type == pygame.KEYDOWN:
            Scenery.change_time(heroi,event)
            if event.key == pygame.K_ESCAPE:
                return True
            
    return False'''

#@state_machine.acts_as_state_machine
class Nivell(motor.Joc):

    def __init__(self,joc,pantalla,screen_size,inetmediate_size,nivell,pers):
        super(Nivell,self).__init__()
        self.joc=joc
        self.screen_size=screen_size
        self.personatges=pers
        self.nivell=nivell
        #print(type(self.screen_size))
        self.sc_width,self.sc_height = self.screen_size
        personatges.screen_size=screen_size
        self.levels_sprites, self.Levels_group, self.g_pers,self.g_armes,self.g_projectils,self.principal,self.sprites,self.penya,self.vida, self.penya_time_list, self.armes_time_list,self.blood = ini_sprites(self.screen_size,joc,nivell,*pers)#personatges.principal,*personatges.ll_pers)
        self.current_level_index=0
        self.AI=AI()
        self.pantalla=pantalla
        self.Lives=pygame.sprite.Group()
        #for el in self.vida:
            #print(type(el))

    def executa_iteracio(self,Volume):
        self.current_level = self.levels_sprites[self.current_level_index].sprite
        self.current_level_time = self.current_level.time
        all_ColRects = self.current_level.ColRect_times
        final= events.tracta_events(self.principal,self.current_level,self.g_armes,self.sprites,self.joc,self.current_level_time,self.armes_time_list,Volume)
        ColRect_current_level = self.current_level.ColRect
        if not final:
            self.penya.update(self.screen_size,self.current_level.speed)
            speed,character,final=colision.colisions(self.penya,all_ColRects,self.current_level,self.screen_size,final,self.current_level_time,self.joc,self.Lives)
            #ColRect_current_level = current_level.update(speed,character)
            ColRect_current_level = all_ColRects[self.current_level_time]
            self.current_level.update(speed,character)
            #print(type(self.principal))
            tallant(self.penya,self.AI,character,self.armes_time_list,self.sprites,self.g_pers,self.current_level_time, self.penya_time_list,self.screen_size,Volume)
            ColRect_current_level.draw(self.pantalla)
            #self.g_armes.update(self.screen_size)
            for armes in self.armes_time_list:
                armes.update(self.screen_size)
            #self.blood.update(self.principal)
            self.levels_sprites[self.current_level_index].draw(self.pantalla)
            #self.penya_time_list[self.current_level_time].draw(self.pantalla)
            self.Lives.update(self.current_level.speed)
            self.Lives.draw(self.pantalla)
            self.armes_time_list[self.current_level_time].draw(self.pantalla)
            self.penya_time_list[self.current_level_time].draw(self.pantalla)
            #self.sprites.draw(self.pantalla)
            if mostra_ColRect:
                ColRect_current_level.draw(self.pantalla)
            self.vida.update(self.principal,self.joc.etapa_estat["Game"])
            self.vida.draw(self.pantalla)
            #print(self.blood.sprites()[0].iniciar,self.blood.sprites()[0].acabar)
            #if self.blood.sprites()[0].iniciar or self.blood.sprites()[0].acabar:
                #print("Fuck yeah lml")
                #self.blood.draw(self.pantalla)  
            #for sp in self.blood:
                #print(sp.image.get_alpha())
        return final

    def reini_sprites(self):
        vides=kill_sprites(self.sprites)
        self.levels_sprites, self.Levels_group, self.g_pers,self.g_armes,self.g_projectils,self.principal,self.sprites,self.penya,self.vida, self.penya_time_list, self.armes_time_list,self.blood = ini_sprites(self.screen_size,self.joc,self.nivell,*self.personatges)#personatges.principal,*personatges.ll_pers)
        if vides<=0:
            self.joc.to_pause()
            self.joc.to_main_menu()
            self.joc.etapa_estat["Game"].vides=self.principal.ini_vides
        else:
            self.principal.vides=vides
            self.joc.etapa_estat["Game"].vides=vides
        self.vida.update(self.principal,self.joc.etapa_estat["Game"])
        #self.vida.ch=self.principal
        #self.vida.update()

def tallant(penya,AI,character,armes_time_list,sprites,g_pers,current_level_time, penya_time_list,screen_size,Volume):
    g_armes = armes_time_list[current_level_time]
    for enemy in g_pers:
        #print(arma)
        #arma.tallant_a(penya,AI,character,g_armes,sprites)
        AI.update(character,enemy,penya,g_armes,sprites,current_level_time,armes_time_list,screen_size,Volume)
    for gun in g_armes:
        AI.dany(gun,penya_time_list[current_level_time])

def kill_sprites(g):
    for sp in g:
        if isinstance(sp,ch_p.Principal):
            vides=sp.vides
            #print(vides)
        sp.kill()
    return vides

def troba_vides(g):
    for sp in g:
        if isinstance(sp,vida.Vides):
            return sp
