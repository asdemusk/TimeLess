
import pygame
import sys
Ifol = 'Image/'
sys.path.insert(0,'NotOurFunctions')
from SpriteSheets import *
import state_machine
from Generic_Sprite import *
import ColRect
import escalado
import ch_p
import control


@state_machine.acts_as_state_machine
class scenery(BaseSprite):

#=================================================    

    PAST = state_machine.State(initial=True)
    PRESENT = state_machine.State()
    FUTURE = state_machine.State()

    

    estats = [PAST, PRESENT, FUTURE]

    go_past = state_machine.Event(from_states=(PRESENT), to_state=PAST)
    go_present = state_machine.Event(from_states=(PAST, FUTURE), to_state=PRESENT)
    go_future = state_machine.Event(from_states=(PRESENT), to_state=FUTURE)


#=================================================
    
    def __init__(self, ImFile, MatDim, ColRect_fn,order_list,screen_size):
        BaseSprite.__init__(self, ImFile, MatDim, 1,screen_size)

        self.speed = -10
        escalado.zoom(self,screen_size,order_list=order_list,ColRect_fn=ColRect_fn)
        
        self.image = self.im[self.estats.index(self.current_state)][0]
        #print(self.im)
        self.rect = self.image.get_rect()
        self.time = self.estats.index(self.current_state)
        self.alowed_times = self.estats[0:self.num_temps]
        if "Level_C" in ColRect_fn:
            self.alowed_times = self.estats[1:]
            #print(self.alowed_times)
            self.go_present()

#=============================================================        
    @state_machine.after('go_past')
    @state_machine.after('go_present')
    @state_machine.after('go_future')


#============================================================
    def canvia_imatge(self):
        self.count = 0
        self.fila = self.estats.index(self.current_state)

    def update(self,speed,character):

        self.speed = -speed
        
        time = self.estats.index(self.current_state)
        self.time = time
        self.image = self.im[time][0]
        self.ColRect = self.ColRect_times[time]
        if isinstance(character,ch_p.Principal):
            self.scroll(self.screen_size,character)
        #for i in self.ColRect_times:
        #    i.update(self.speed)
        return self.ColRect
        #print(self.rect.center)

    def scroll(self,screen_size,character):
        width, height = screen_size
        if character.vx > 0: #personatge va a la dreta
            if self.rect.right <= width: #xoca per la dreta
                self.rect.right = width
                character.rect.move_ip(character.vx,0)
                self.speed = 0
                if character.rect.right > width:
                    character.rect.right = width
            elif self.rect.left >= 0:#xoca per la esquerra
                if character.rect.centerx < width//2:
                    character.rect.move_ip(character.vx,0)
                    self.speed = 0
                else:
                    character.rect.centerx = width//2
                    self.rect.move_ip(self.speed,0)
                    self.move_ColRect(self.speed)
            else:
                self.rect.move_ip(self.speed,0)
                self.move_ColRect(self.speed)
        elif character.vx < 0: #personatge va a la esquerra
            if self.rect.left >= 0: #xoca per la esquerra
                self.rect.left = 0
                character.rect.move_ip(character.vx,0)
                self.speed = 0
                if character.rect.left < 0:
                    character.rect.left = 0
            elif self.rect.right >= 0:#xoca per la dreta
                if character.rect.centerx > width//2:
                    character.rect.move_ip(character.vx,0)
                    self.speed = 0
                else:
                    character.rect.centerx = width//2
                    self.rect.move_ip(self.speed,0)
                    self.move_ColRect(self.speed)
            else:
                self.rect.move_ip(self.speed,0)
                self.move_ColRect(self.speed)
        #print(self.speed)
        
    def move_ColRect(self,speed):
        for i in self.ColRect_times:
            i.update(speed)
    
    def resize(self, order_list,ColRect_fn,screen_size):
        n = len(order_list)
        self.im2 = [[0],[1],[2]]
        section_width, section_height = self.rect.size
        screen_width, screen_height = screen_size

        zfx = screen_width/section_width
        zfy = zfx
        zoom_factor = (zfx,zfy)
        #self.speed = self.speed * mf
        self.ColRect_times = ColRect.create_level_ColRect(ColRect_fn,section_width,order_list,zoom_factor,screen_size)

        
        ipast = pygame.Surface((section_width*n,section_height))
        ipresent = pygame.Surface((section_width*n,section_height))
        ifuture = pygame.Surface((section_width*n,section_height))
        for i in range(n):
            ipast.blit(self.im[0][order_list[i]], (i*section_width,0)) #para la version final ha que cambiar el orden fila columna
            ipresent.blit(self.im[1][order_list[i]], (i*section_width,0))
            ifuture.blit(self.im[2][order_list[i]], (i*section_width,0))
           #print(i)
           #print(i*width)

        self.im2[0][0] = pygame.transform.scale(ipast,(screen_width*n,screen_height))
        #print(self.im2[0][0].get_rect().size)
        self.im2[1][0] = pygame.transform.scale(ipresent,(screen_width*n,screen_height))
        self.im2[2][0] = pygame.transform.scale(ifuture,(screen_width*n,screen_height))

        self.im = self.im2
        
        

def change_time(obj,event):
    if event.key in control.c_game["avanç"]:
        if obj.current_state=="PRESENT" and "FUTURE" in obj.alowed_times:
            obj.go_future()
        elif obj.current_state=="PAST" and "PRESENT" in obj.alowed_times:
            obj.go_present()
    elif event.key in control.c_game["retro"]:
        if obj.current_state=="PRESENT" and "PAST" in obj.alowed_times:
            obj.go_past()
        elif obj.current_state=="FUTURE" and "PRESENT" in obj.alowed_times:
            obj.go_present()


