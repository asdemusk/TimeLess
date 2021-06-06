import pygame
import motor
import botons
import control

class Menu(motor.Etapa):

    def __init__(self,joc,fname):
        super().__init__()
        self.joc=joc
        self.g_botons,self.c_fons,self.alpha,self.ll_botons=crea_botons(self,fname,joc)
        self.image=pygame.surface.Surface(self.joc.screen_size)
        self.image.fill(self.c_fons)
        self.image.set_alpha(self.alpha)
        self.index=0
        
    def executa_iteracio(self,Volume):
        if self.joc.current_state=="Pause":
            game=self.joc.etapa_estat["Game"].current_lvl
            game.levels_sprites[game.current_level_index].draw(self.joc.pantalla)
            game.armes_time_list[game.current_level_time].draw(game.pantalla)
            game.penya_time_list[game.current_level_time].draw(game.pantalla)
            game.vida.draw(self.joc.pantalla)
        self.joc.pantalla.blit(self.image,(0,0))
        final,click=self.tracta_events()
        self.g_botons.update()
        boto=None
        for bot in self.g_botons:
            if click and bot.resaltat:
                boto=bot.name
            self.joc.pantalla.blit(bot.res.image,bot.res.rect)
        self.g_botons.draw(self.joc.pantalla)
        if boto=="EXIT":
            self.joc.to_exit()
        elif boto=="Load Game":
            self.joc.etapa_estat["Game"].update()
            self.joc.to_game()
            self.joc.etapa.current_lvl.reini_sprites()
        elif boto=="Play Game":
            self.joc.to_play_game()
        elif boto=="Continue":
            self.joc.to_game()
        elif boto=="Main Menu":
            self.joc.to_main_menu()
        elif boto=="Game Menu":
            self.joc.to_play_game()
        elif boto=="Back":
            self.come_back()
        elif boto=="Options":
            self.joc.to_options()
        elif boto=="Save":
            actualitza_save(self.joc.etapa_estat["Game"])
            self.joc.to_game()
        elif boto=="New Game":
            level1(self.joc.etapa_estat["Game"])
            self.joc.etapa_estat["Game"].update()
            self.joc.to_game()
            self.joc.etapa.current_lvl.reini_sprites()
            self.joc.etapa.actualitza_n()
        elif boto=="Controls":
            self.joc.to_controls()
        elif boto=="Sound":
            if self.joc.current_state=="Options":
                self.joc.to_sound()
            else:
                self.joc.to_sound2()
            self.joc.etapa.act_vols()
        elif boto=="Weapon":
            self.joc.to_weapon()
        return final

    def tracta_events(self):
        final=False
        click=False
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                final=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    self.come_back()
                elif event.key in control.c_menu["down"]:
                    self.index+=1
                    if self.index>=len(self.ll_botons):
                        self.index=0
                elif event.key in control.c_menu["up"]:
                    self.index-=1
                    if self.index<0:
                        self.index=len(self.ll_botons)-1
                elif event.key in control.c_menu["intro"]:
                    click=True
            if event.type==pygame.MOUSEBUTTONDOWN:
                click=True
        return final,click

    def come_back(self):
        if self.joc.current_state=="MainMenu":
            self.joc.to_exit()
        elif self.joc.current_state=="PlayGame":
            self.joc.to_main_menu()
        elif self.joc.current_state=="Pause":
            self.joc.to_game()
        elif self.joc.current_state=="Options":
            self.joc.to_main_menu()


def crea_botons(self,fname,joc):
    ll=[]
    lt=0
    titol=""
    bot=pygame.sprite.Group()
    fin=open(fname,"r")
    for line in fin:
        line=line.strip()
        if line[:3]=="===":
            lt+=1
        else:
            if lt==1:
                titol=line.strip(":")
            elif lt in (0,2):
                lt=0
                info1,info2=line.split(" / ")
                if titol=="Botons":
                    if info1=="Marge":
                        marge=int(info2)
                    elif info1=="Numero":
                        nT=int(info2)
                    elif info1=="Lletra":
                        tll=int(info2)
                    else:
                        n,info=info1,info2
                        pos=calcula_pos(n,joc,nT,marge)
                        text,c_lletra,c_boto=info.split("-")
                        button=botons.Boto(self,pos,text,tll,c_lletra,c_boto,n)
                        bot.add(button)
                        ll.append(button)
                elif titol=="Fons Menu":
                    if info1=="Color":
                        c_fons=pygame.color.Color(info2)
                    elif info1=="Alpha":
                        alpha=int(info2)
    fin.close()
    return bot,c_fons,alpha,ll
                    
            
def calcula_pos(n,joc,nT,marge):
    n=int(n)
    a,h=joc.screen_size
    h-=2*marge
    x=a//2
    amplada=h/nT
    y=round(marge+amplada/2+amplada*(n-1))
    return x,y

def level1(self):
    fout=open("save.txt","w")
    fout.write("Nivell / 1\n")
    fout.write("Vides / "+ str(self.current_lvl.principal.ini_vides))
    fout.close()

def actualitza_save(self):
    fout=open("save.txt","w")
    fout.write("Nivell / " + str(self.n+1) + "\n")
    fout.write("Vides / " + str(self.vides))
    fout.close()

def ordena(self):
    ll=[]
    for boto in self.g_botons:
        ll.append((boto.n,boto))
    ll.sort()
    return ll

def act_bot_tec(g_botons,boto):
    for bot in g_botons:
        if bot==boto:
            boto.res.image.set_alpha(255)
            boto.resaltat=True
        else:
            boto.res.image.set_alpha(0)
            boto.resaltat=False
