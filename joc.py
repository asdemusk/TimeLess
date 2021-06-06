import pygame
import nivell
import personatges

class Game:

    def __init__(self,joc,pantalla,screen_size,intermediate_size,Volume):#,personatges_nivell):
        self.nivells=[]
        self.joc=joc
        personatges.act_principal()
        personatges_nivell=personatges.p_n
        for el in personatges_nivell:
            pers,lvl=el
            self.nivells.append(nivell.Nivell(joc,pantalla,screen_size,intermediate_size,lvl,pers))
        self.actualitza_n()
        self.current_lvl=self.nivells[self.n]
        #self.vides=self.current_lvl.principal.ini_vides
        for lvl in self.nivells:
            lvl.principal.vides=self.vides
        self.Volume = Volume

    def update(self):
        self.actualitza_n()
        self.current_lvl=self.nivells[self.n]

    def executa_iteracio(self,Volume):
        return self.current_lvl.executa_iteracio(Volume)

    def go_forward(self):
        self.n+=1
        if self.n>=len(self.nivells):
            self.Volume.stop_background()
            self.joc.to_main_menu()
        else:
            self.current_lvl=self.nivells[self.n]
            self.Volume.stop_background()
            self.Volume.play_background(False)
            self.current_lvl.reini_sprites()
            self.current_lvl.principal.vides=self.vides

    def actualitza_n(self):
        fin=open("save.txt","r")
        for line in fin:
            #print(line)
            line=line.strip()
            tipus,num=line.split(" / ")
            if tipus=="Nivell":
                self.n=int(num)-1
            elif tipus=="Vides":
                self.vides=int(num)
            #self.n=int(line.strip())-1
        fin.close()
        for lvl in self.nivells:
            lvl.principal.vides=self.vides

    def resta_vida(self):
        for lvl in self.nivells:
            lvl.principal.vides-=1

    def cor(self):
        self.vides+=1
        for lvl in self.nivells:
            lvl.principal.vides=self.vides
