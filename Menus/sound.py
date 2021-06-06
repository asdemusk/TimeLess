import pygame
import motor
import botons
import control

count_max=9

class Sounds(motor.Etapa):

    def __init__(self,joc,fname):
        super().__init__()
        self.joc=joc
        self.g_botons,self.c_fons,self.alpha,self.ll_botons,self.g_bar,self.g_barI=crea_botons(self,fname,joc)
        self.image=pygame.surface.Surface(self.joc.screen_size)
        self.image.fill(self.c_fons)
        self.image.set_alpha(self.alpha)
        self.index=0
        self.mant=False
        self.count=count_max

    def executa_iteracio(self,Volume):
        self.joc.pantalla.blit(self.image,(0,0))
        final,click=self.tracta_events(Volume)
        self.g_botons.update()
        boto=None
        for bot in self.g_botons:
            if self.mant and bot.resaltat and self.count==count_max:
                boto=bot
            self.joc.pantalla.blit(bot.res.image,bot.res.rect)
        if self.mant:
            #print("Fuck Yeah lml")
            self.count-=1
            if self.count<0:
                self.count=count_max
        self.g_botons.draw(self.joc.pantalla)
        self.g_bar.update()
        self.g_bar.draw(self.joc.pantalla)
        if boto!=None:
            if boto.name=="Back":
                self.act_saves(Volume)
                if self.joc.current_state=="Sound":
                    self.joc.to_options()
                else:
                    self.joc.to_pause()
            elif boto.name in ("+","-"):
                self.act_vol(boto.name,boto.tipus)
        #print(self.count)
        return final

    def tracta_events(self,volume):
        final=False
        click=False
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                final=True
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    self.act_saves(volume)
                    if self.joc.current_state=="Sound":
                        self.joc.to_options()
                    else:
                        self.joc.to_pause()
                elif event.key in control.c_menu["intro"]:
                    click=True
                    self.mant=True
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
                    self.mant=False
                    self.count=count_max
        return final,click

    def act_vol(self,accio,tipus):
        for volum in self.g_barI:
            if volum.tipus==tipus:
                break
        if accio=="+":
            volum.volum+=5
        else:
            volum.volum-=5
        if volum.volum>100:
            volum.volum=100
        elif volum.volum<0:
            volum.volum=0

    def act_vols(self):
        for el in self.g_barI:
            el.volum=botons.troba_vol(el.tipus)

    def act_saves(self,volume):
        fout=open("Music/Saves.txt","w")
        for volum in self.g_barI:
            fout.write("{}: {}\n".format(volum.tipus,volum.volum))
            if volum.tipus == "general":
                volume.set_general_volume(float(volum.volum)/100)
            elif volum.tipus == "backg":
                volume.set_background_volume(float(volum.volum)/100)
            elif volum.tipus == "enemy":
                volume.set_weapon_volume(float(volum.volum)/100)
        fout.close()
        
def crea_botons(self,fname,joc):
    ll=[]
    lt=0
    titol=""
    bot=pygame.sprite.Group()
    bar=pygame.sprite.LayeredUpdates()
    barI=pygame.sprite.Group()
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
                    elif info2[0] in ("-","+","."):
                        info2,tipus=info2.split("_")
                        f,c=info1.split(",")
                        f=int(f)
                        c=int(c)
                        pos=calcula_pos(f,c,joc,vT,hT,h,v)
                        if info2[0]==".":
                            r,ci,alpha,cb=info2.split("*")
                            alpha=int(alpha)
                            SB=botons.SoundB(pos,cb,alpha,tipus)
                            SI=botons.SoundI(ci,SB)
                            bar.add(SB,layer=0)
                            bar.add(SI,layer=1)
                            barI.add(SI)
                        else:
                            text,c_ll,c_b,active_b=info2.split("*")
                            #pos=calcula_pos(f,c,joc,vT,hT,h,v)
                            button=botons.Boto(self,pos,text,lletra,c_ll,c_b,(columna-3)+(fila-1),active=True)
                            button.tipus=tipus
                            ll.append(button)
                            bot.add(button)
                    else:
                        text,c_ll,c_b,active_b=info2.split("*")
                        if active_b=="0":
                            active=False
                        else:
                            active=True
                        info1=info1.split(",")
                        fila,columna=int(info1[0]),int(info1[1])
                        pos=calcula_pos(fila,columna,joc,vT,hT,h,v)
                        if text=="Back":
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
                elif titol=="Fons Menu":
                    if info1[0]=="#":
                        pass
                    elif info1=="Color":
                        color=pygame.color.Color(info2)
                    elif info1=="Alpha":
                        alpha=int(info2)
    #fin.close()
    return bot,color,alpha,ll,bar,barI

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
