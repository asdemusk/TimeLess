import pygame
import state_machine
import motor
import joc
import sortida
import menu
import options
import sound
import weap

path="Menus/"

changes=[path+"Changes1.txt",path+"Changes2.txt",path+"Changes3.txt",path+"Reset.txt"]

@state_machine.acts_as_state_machine
class Joc(motor.Joc):

    MainMenu=state_machine.State(initial=True)
    Options=state_machine.State()
    Sound=state_machine.State()
    Controls=state_machine.State()
    Game=state_machine.State()#initial=True)
    PlayGame=state_machine.State()
    Exit=state_machine.State()#initial=True)
    Pause=state_machine.State()
    Weapon=state_machine.State()
    Sound2=state_machine.State()

    to_exit=state_machine.Event(from_states=(MainMenu,Pause),to_state=Exit)
    to_main_menu=state_machine.Event(from_states=(Options,PlayGame,Pause,Game),to_state=MainMenu)
    to_options=state_machine.Event(from_states=(MainMenu,Sound,Controls,Weapon),to_state=Options)
    to_sound=state_machine.Event(from_states=(Options),to_state=Sound)
    to_controls=state_machine.Event(from_states=(Options),to_state=Controls)
    to_game=state_machine.Event(from_states=(PlayGame,Pause),to_state=Game)
    to_play_game=state_machine.Event(from_states=(MainMenu,Pause),to_state=PlayGame)
    to_pause=state_machine.Event(from_states=(Game,Sound2),to_state=Pause)
    to_weapon=state_machine.Event(from_states=(Options),to_state=Weapon)
    to_sound2=state_machine.Event(from_states=(Pause),to_state=Sound2)

    @state_machine.after("to_exit")
    @state_machine.after("to_main_menu")
    @state_machine.after("to_options")
    @state_machine.after("to_sound")
    @state_machine.after("to_controls")
    @state_machine.after("to_game")
    @state_machine.after("to_play_game")
    @state_machine.after("to_pause")
    @state_machine.after("to_weapon")
    @state_machine.after("to_sound2")
    def canvia_etapa(self):
        #print(self.current_state,self.paused)
        self.etapa=self.etapa_estat[self.current_state]
        if isinstance(self.etapa,joc.Game):
            pygame.mouse.set_visible(False)
            self.paused = self.Volume.play_background(self.paused)
            #print(self.paused)
        else:
            pygame.mouse.set_visible(True)
            if self.current_state == "Pause":
                self.Volume.pause_background()
            elif self.current_state != "Sound2":
                #print("aaa")
                self.Volume.stop_background()

    @state_machine.before("to_pause")
    def before(self):
        self.paused=True
    @state_machine.before("to_exit")
    @state_machine.before("to_main_menu")
    @state_machine.before("to_options")
    @state_machine.before("to_sound")
    @state_machine.before("to_controls")
    #@state_machine.before("to_game")
    @state_machine.before("to_play_game")
    @state_machine.before("to_weapon")
    #@state_machine.before("to_sound2")
    def before2(self):
        self.paused = False

    def __init__(self,pantalla,screen_size,intermediate_size,Volume):
        super(Joc, self).__init__()
        self.crono=pygame.time.Clock()
        self.screen_size=screen_size
        self.pantalla=pantalla
        self.paused=False

        
        eG=joc.Game(self,pantalla,screen_size,intermediate_size,Volume)
        eE=sortida.Exit()
        eMM=menu.Menu(self,path+"MainMenu.txt")
        ePG=menu.Menu(self,path+"Joc.txt")
        eP=menu.Menu(self,path+"Pause.txt")
        eO=menu.Menu(self,path+"Options.txt")
        eC=options.Options(self,changes)
        eS=sound.Sounds(self,path+"Sound.txt")
        eW=weap.Weap(self,path+"Weap.txt")
        eS2=sound.Sounds(self,path+"Sound.txt")
        
        self.etapa_estat={self.Game.name:eG}
        self.etapa_estat[self.Exit.name]=eE
        self.etapa_estat[self.MainMenu.name]=eMM
        self.etapa_estat[self.PlayGame.name]=ePG
        self.etapa_estat[self.Pause.name]=eP
        self.etapa_estat[self.Options.name]=eO
        self.etapa_estat[self.Controls.name]=eC
        self.etapa_estat[self.Sound.name]=eS
        self.etapa_estat[self.Weapon.name]=eW
        self.etapa_estat[self.Sound2.name]=eS2

        self.Volume = Volume
        
    def inicialitza(self):
        self.canvia_etapa()
        
    def sincronitza(self):
        self.crono.tick(60)
        pygame.display.flip()


    def acaba(self):
        pygame.quit()

    def executa(self,Volume):
        final = False
        self.inicialitza()
        while not final:
            final = self.etapa.executa_iteracio(Volume)
            self.sincronitza()
            pygame.display.set_caption("TimeLess {}".format(int(self.crono.get_fps())))
        self.acaba()


def main(screen_size,pantalla,intermediate_size,Volume):
    j1=Joc(screen_size,pantalla,intermediate_size,Volume)
    j1.executa(Volume)    

