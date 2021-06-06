import pygame
import botons
import motor
import control
import personatges

class Weap(motor.Etapa):

    def __init__(self,joc,fname):
        super().__init__()
        self.joc=joc
        self.g_botons,self.c_fons,self.alpha,self.ll_botons,self.g_temps,self.g_dist=crea_botons(self,fname,joc)
        self.image=pygame.surface.Surface(self.joc.screen_size)
        self.image.fill(self.c_fons)
        self.image.set_alpha(self.alpha)
        self.index=0
        self.act=[None,None]
        import_i(self)
        #print(len(self.ll_botons))

    def executa_iteracio(self,Volume):
        #print("asdasd")
        self.joc.pantalla.blit(self.image,(0,0))
        final,click=self.tracta_events()
        self.g_botons.update()
        boto=None
        for bot in self.g_botons:
            if click and bot.resaltat:
                boto=bot
            self.joc.pantalla.blit(bot.res.image,bot.res.rect)
        self.g_botons.draw(self.joc.pantalla)
        if boto!=None and boto.name=="Back":
            save(self)
            self.joc.to_options()
        elif boto!=None:
            if boto.name in ("Melee","Distance"):
                grup=self.g_dist
                if boto.name=="Distance":
                    numero_t=1
                else:
                    numero_t=0
                self.act[1]=numero_t
            else:
                grup=self.g_temps
                self.act[0]=boto.name.lower()
            for b in grup:
                b.i=0
            boto.i=1
        return final

    def tracta_events(self):
        final=False
        click=False
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                final=True
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    #self.act_saves()
                    save(self)
                    self.joc.to_options()
                elif event.key in control.c_menu["intro"]:
                    click=True
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
                click=True
        return final,click
        
def crea_botons(self,fname,joc):
    #print_file(fname)
    ll=[]
    lt=0
    #count=0
    titol=""
    bot=pygame.sprite.Group()
    temps=pygame.sprite.Group()
    dist=pygame.sprite.Group()
    fin=open(fname,"r")
    for line in fin:
        #count+=1
        #print(countx)
        line=line.strip()
        #print(line)
        if line[:3]=="===":
            lt+=1
        else:
            if lt==1:
                titol=line.strip(":")
            elif lt in (0,2):
                lt=0
                info1,info2=line.split(" / ")
                #print(info1,titol,sep=" / ",end="\n\n")
                if titol=="Char":
                    #print("|")
                    if info1[0]=="#":
                        pass
                    elif info1=="Marge":
                        info2=info2.split(",")
                        h,v=int(info2[0]),int(info2[1])
                    elif info1=="Numero":
                        #print("sdasd")
                        info2=info2.split(",")
                        #print("")
                        vT,hT=int(info2[0]),int(info2[1])
                        #print(vT,hT)
                    elif info1=="Lletra":
                        lletra=int(info2)
                elif titol=="Fons Menu":
                    if info1[0]=="#":
                        pass
                    elif info1=="Color":
                        color=pygame.color.Color(info2)
                    elif info1=="Alpha":
                        alpha=int(info2)
                elif titol=="Botons":
                    #print(info2)
                    if info1=="None":
                        pass
                    elif info1[0]=="#":
                        pass
                    elif info2[:4]=="Back":
                        text,c_ll,c_b=info2.split("-")
                        info1=info1.split(",")
                        fila,columna=int(info1[0]),int(info1[1])
                        pos=calcula_pos(fila,columna,joc,vT,hT,h,v)
                        button=botons.Boto(self,pos,text,lletra,c_ll,c_b,(columna-3)+(fila-1))
                    else:
                        text,c_ll,c_b1,c_b2=info2.split("-")
                        info1=info1.split(",")
                        fila,columna=int(info1[0]),int(info1[1])
                        pos=calcula_pos(fila,columna,joc,vT,hT,h,v)
                        button=botons.BotoW(self,pos,text,lletra,c_ll,c_b1,c_b2,(columna-3)+(fila-1))
                        if text in ("Melee","Distance"):
                            dist.add(button)
                        else:
                            temps.add(button)
                    bot.add(button)
                    ll.append(button)
                    #print(len(ll))
    return bot,color,alpha,ll,temps,dist

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

def print_file(fname):
    fin=open(fname,"r")
    print(fin.read())
    fin.close()

def import_i(self):
    fin=open("Characters/Weapon_save.txt","r")
    for line in fin:
        line=line.strip()
        t,dist=line.split()
    for b in self.g_temps:
        if b.name.lower()==t:
            b.i=1
            self.act[0]=b.name.lower()
    for b in self.g_dist:
        if b.name=="Distance" and dist=="1":
            b.i=1
            self.act[1]="1"
        elif b.name=="Melee" and dist=="0":
            b.i=1
            self.act[1]="0"
    fin.close()

def save(self):
    fout=open("Characters/Weapon_save.txt","w")
    t,dist=self.act
    fout.write("{} {}".format(t,dist))
    fout.close()
    personatges.act_principal()
