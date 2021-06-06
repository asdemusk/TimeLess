import pygame
import motor
import botons
import control
import shutil
import teclat
import copy

path="Controls/"

tabu="numlock-caps lock-scroll lock".split("-")

#especial={"up":"up arrow","down":"down arrow","left":"left arrow","right":"right arrow"}

class Changes(motor.Etapa):

    def __init__(self,joc,fname,menu,more):
        self.joc=joc
        self.menu=menu
        self.g_botons,self.c_fons,self.alpha,self.ll_botons=crea_botons(self,fname,joc,more)
        self.image=pygame.surface.Surface(self.joc.screen_size)
        self.image.fill(self.c_fons)
        #print(type(self.alpha))
        self.image.set_alpha(self.alpha)
        #self.ordre=ordena(self)
        self.index=0
        self.changing=False
        self.l=[]
        self.proced=False
        #print(len(self.ll_botons))

    def executa_iteracio(self,Volume):
        #print(teclat.decod())
        self.joc.pantalla.blit(self.image,(0,0))
        final,click=self.tracta_events()
        self.g_botons.update(self.changing)
        boto=None
        for bot in self.g_botons:
            if click and bot.resaltat:
                boto=bot
            self.joc.pantalla.blit(bot.res.image,bot.res.rect)
        self.g_botons.draw(self.joc.pantalla)
        if boto!=None and boto.ch:
            i=boto.i
            typ=boto.typ
            tipus=boto.tipus
            self.l=[i,typ,tipus,boto]
            #print(self.l)
            self.changing=True
        elif boto!=None:
            if boto.name=="Back":
                self.joc.to_options()
            elif boto.name=="More":
                self.menu.go_forward()
            elif boto.name=="RESET":
                for el in self.menu.screens:
                    resset(el)
                self.menu.go_forward()
        #for bot in self.ll_botons:
        #print(bot.name)
        if self.changing:
            tec_events=teclat.decod()
            tec_events=treu(tec_events,tabu)
            if len(tec_events)>0:
                #print("Fuck Yeah lml")
                #self.changing=False
                tecla=tec_events[0]
                #if tecla in especial:
                    #tecla=especial[tecla]
                if self.proced:# and tecla not in tabu:
                    self.changing=False
                    self.actualtza_controls(tecla)
                #self.count-=1
        #print(self.proced)
        return final

    def tracta_events(self):
        final=False
        click=False
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                final=True
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    self.joc.to_options()
                elif event.key in control.c_menu["intro"]:
                    click=True
                    self.proced=False
                elif event.key in control.c_menu["up"]:
                    self.index-=2
                    if self.index<0:
                        diff=abs(self.index)
                        self.index=len(self.ll_botons)-diff
                elif event.key in control.c_menu["down"]:
                    self.index+=2
                    if self.index>=len(self.ll_botons):
                        diff=abs(self.index-len(self.ll_botons))
                        self.index=-1+diff
                elif event.key in control.c_menu["right"]:
                    self.index+=1
                    if self.index>=len(self.ll_botons):
                        self.index=0
                elif event.key in control.c_menu["left"]:
                    self.index-=1
                    if self.index<0:
                        self.index=len(self.ll_botons)-1
            elif event.type==pygame.MOUSEBUTTONDOWN:
                click=False
            elif event.type==pygame.KEYUP:
                if event.key in control.c_menu["intro"]:
                    self.proced=True
        return final,click

    def actualtza_controls(self,tecla):
        #self.count=1
        i,typ,tipus,boto=self.l
        d={}
        if typ=="menu":
            typ="menus"
        fin=open(path+"controls_"+typ+".txt","r")
        for line in fin:
            line=line.strip()
            accio,tec=line.split(": ")
            tec=tec.split(",")
            d[accio]=tec
        fin.close()
        #print(tecla)
        #subst=control.th[tecla]
        if i==0:
            d[tipus][0]=tecla
        else:
            if len(d[tipus])==1:
                d[tipus].append(tecla)
            else:
                d[tipus][1]=tecla
        #print(d)
        fout=open(path+"controls_"+typ+".txt","w")
        for key in d:
            fout.write(key+": "+",".join(d[key])+"\n")
        fout.close()
        print_file(path+"controls_"+typ+".txt")
        control.c_game,control.edit_game,control.c_menu,control.edit_menu=control.edita()
        #for boto in self.ll_botons:
        #print("Fuck Yeah lml")
        #if boto.ch:
        if boto.typ=="game":
            ref=control.edit_game
        elif boto.typ=="menu":
            ref=control.edit_menu
        tecles=ref[boto.tipus]
        if boto.i==0:
            name=tecles[0]
        else:
            if len(tecles)>1:
                name=tecles[1]
            else:
                name="*"
            #if boto.name!=name:
        boto.change(name,boto.rect.center)

def crea_botons(self,fname,joc,more):
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
                    #info1=info1.split(",")
                    if info1=="None":
                        pass
                    elif info1[0]=="#":
                        pass
                    elif info2[0]=="?":
                        info2,tipus=info2.split("_")
                        tipus,typ=tipus.split("-")
                        if typ=="game":
                            ref=control.edit_game
                        elif typ=="menu":
                            ref=control.edit_menu
                        f,c=info1.split(",")
                        f=int(f)
                        c=int(c)
                        text,c_ll,c_b,active_b=info2.split("-")
                        i=c-3
                        tecles=ref[tipus]
                        pos=calcula_pos(f,c,joc,vT,hT,h,v)
                        if i==0:
                            name=tecles[0]
                        else:
                            if len(tecles)>1:
                                name=tecles[1]
                            else:
                                name="*"
                        button=botons.Boto(self,pos,name,lletra,c_ll,c_b,(columna-3)+(fila-1),active=True)
                        button.ch=True
                        button.i=i
                        button.typ=typ
                        button.tipus=tipus
                        ll.append(button)
                        bot.add(button)
                        #print("|")
                    else:
                        text,c_ll,c_b,active_b=info2.split("-")
                        #active=bool(active_b)
                        #print(active,active_b,sep=" / ")
                        if active_b=="0":
                            active=False
                        else:
                            active=True
                        #print(active_b,active,sep=" / ")
                        info1=info1.split(",")
                        fila,columna=int(info1[0]),int(info1[1])
                        pos=calcula_pos(fila,columna,joc,vT,hT,h,v)
                        if (text=="More" and more) or text!="More":
                            if text=="Back" and not more:
                                pos[0]=joc.screen_size[0]//2
                            button=botons.Boto(self,pos,text,lletra,c_ll,c_b,(columna-3)+(fila-1),active=active)
                            button.descr=button.name
                            button.ch=False
                            if active:
                                ll.append(button)
                            bot.add(button)
                elif titol=="Char":
                    if info1[0]=="#":
                        pass
                    elif info1=="Marge":
                        info2=info2.split(",")
                        h,v=int(info2[0]),int(info2[1])
                    elif info1=="Numero":
                        info2=info2.split(",")
                        vT,hT=int(info2[0]),int(info2[1])
                    elif info1=="Lletra":
                        lletra=int(info2)
                    #elif info1=="Tipus":
                        #if info2=="game":
                            #ref=control.edit_game
                            #print(ref)
                            #typ="game"
                elif titol=="Fons Menu":
                    if info1[0]=="#":
                        pass
                    elif info1=="Color":
                        color=pygame.color.Color(info2)
                    elif info1=="Alpha":
                        alpha=int(info2)
    fin.close()
    return bot,color,alpha,ll

def calcula_pos(f,c,joc,vT,hT,mh,mv):
    a,h=joc.screen_size
    a-=mv*2
    h-=mh*2
    amplada=a/hT
    alcada=h/vT
    x=round(mv+amplada/2+amplada*(c-1))
    y=round(mh+alcada/2+alcada*(f-1))
    #print(x,y,sep=",")
    return [x,y]

def resset(self):
    shutil.copyfile(path+"reset_game.txt",path+"controls_game.txt")
    shutil.copyfile(path+"reset_menus.txt",path+"controls_menus.txt")
    #print_file(path+"controls_game.txt")
    #print_file(path+"controls_menus.txt")
    control.c_game,control.edit_game,control.c_menu,control.edit_menu=control.edita()
    #print(control.edit_game)
    #print(len(self.ll_botons))
    for boto in self.ll_botons:
        #print("Fuck Yeah lml")
        if boto.ch:
            if boto.typ=="game":
                ref=control.edit_game
            elif boto.typ=="menu":
                ref=control.edit_menu
            tecles=ref[boto.tipus]
            if boto.i==0:
                name=tecles[0]
            else:
                if len(tecles)>1:
                    name=tecles[1]
                else:
                    name="*"
                #if boto.name!=name:
            boto.change(name,boto.rect.center)
                    
    #control.contr()

def print_file(fname):
    fin=open(fname,"r")
    #print(fin.read())
    fin.close()

def treu(l,elem):
    for el in elem:
        if el in l:
            l.remove(el)
    return l
