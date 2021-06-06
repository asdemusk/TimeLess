import pygame

d_legal={"ves_esquerra":(2,0,5,7,11),
         "ves_dreta":(2,1,5,7,11),
         "para":(0,1,5,7,11),
         "salta":(0,1,2),
         "aterra":(9,),
         "atac_salt":(9,),
         "ajupir":(7,1,0,2),
         "ajupit":(4,),
         "aixecant":(10,),
         "ataca":(2,1,0,7),
         "mort":(2,1,0),
         "aire":(3,8,2,1,0,10,4,5,7,11,6)}#,
         #"aixecat":()}

def canvi(self):
    if self.estat==0: #D
        #self.vel=3
        #self.vx=10
        #self.dir=[1,0]
        self.orientacio=1
        self.ifi=(0,"D")
        #self.arma.n_atacs=1
    elif self.estat==1: #E
        #self.vel=3
        #self.vx=-10
        #self.dir=[-1,0]
        self.orientacio=-1
        self.ifi=(1,"E")
        #self.arma.n_atacs=1
    elif self.estat==2: #quiet
        #self.vel=0
        #self.vx=0
        #self.vy=0
        #self.dir=[0,0]
        #self.arma.n_atacs=1
        if self.orientacio==1:
            self.ifi=(2,"D")
        else:
            self.ifi=(2,"E")
    elif self.estat==3: #salta
        if self.orientacio==1:
            self.ifi=(3,"D")
        else:
            self.ifi=(3,"E")
    elif self.estat==4: #ajup
        #self.vel=0
        #self.vx=0
        if self.orientacio==1:
            self.ifi=(4,"D")
        else:
            self.ifi=(4,"E")
    elif self.estat==5: #ataca
        if self.atac_estatic:
            #self.vel=0
            self.vx=0
        if self.orientacio==1:
            self.ifi=(5,"D")
        else:
            self.ifi=(5,"E")
    elif self.estat==6: #mort
        #self.vel=0
        #self.vx=self.vy=0
        if self.orientacio==1:
            self.ifi=(6,"D")
        else:
            self.ifi=(6,"E")
    elif self.estat==7: #aterra
        #self.vel=0
        #self.vx=self.vy=0
        #self.dir[1]=0
        #self.vx=0
        #self.arma.n_atacs=1
        if self.orientacio==1:
            self.ifi=(7,"D")
        else:
            self.ifi=(7,"E")
    elif self.estat==8: #atac_salta
        if self.orientacio==1:
            self.ifi=(8,"D")
        else:
            self.ifi=(8,"E")
    elif self.estat==9: #aire
        #self.arma.n_atacs=1
        self.terra=False
        #self.vel=1
        #self.dir[1]=0
        #self.vy=0
        if self.orientacio==1:
            self.ifi=(9,"D")
        else:
            self.ifi=(9,"E")
    elif self.estat==10: #ajupit
        if self.orientacio==1:
            self.ifi=(10,"D")
        else:
            self.ifi=(10,"E")
    elif self.estat==11:
        if self.orientacio==1:
            self.ifi=(11,"D")
        else:
            self.ifi=(11,"E")

def legal(canvi,personatge):
    from_legal=d_legal[canvi]
    actual=personatge.estat
    #print(from_legal,actual)
    return (actual in from_legal)
