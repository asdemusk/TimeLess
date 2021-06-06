vh=10
vs=25*1

veloChStats={0:[[vh,0],[None,None]], #dreta
             1:[[None,None],[-vh,0]], #esquerra
             2:[[0,0],[0,0]], #quiet
             3:[[0,0],[0,0]], #salta
             4:[[0,0],[0,0]], #ajup
             #5:[], #ataca
             6:[[0,0],[0,0]], #mort
             7:[[0,0],[0,0]], #aterra
             #8:[],#[[None,None],[None,None]], #atac_salt
             9:[[None,0],[None,0]], #aire
             10:[[0,0],[0,0]], #ajupit
             11:[[0,0],[0,0]]} #aixecant

veloStats={0:[[vh,None],[None,None]], #dreta
           1:[[None,None],[-vh,None]], #esquerra
           2:[[None,None],[None,None]], #quiet
           3:[[None,None],[None,None]], #salta
           4:[[None,None],[None,None]], #ajup
           5:[[None,None],[None,None]], #ataca
           6:[[None,None],[None,None]], #mort
           7:[[None,None],[None,None]], #aterra
           8:[[None,None],[None,None]], #atac_salt
           9:[[vh,vs],[-vh,vs]], #aire
           10:[[None,None],[None,None]], #ajupit
           11:[[None,None],[None,None]]} #aixecant

gravetat=[0,-1]


ori={"D":0,"E":1}

ataca={True:{5:[[0,0],[0,0]],
             8:[[None,None],[None,None]]},
       False:{5:[[None,None],[None,None]],
              8:[[None,None],[None,None]]}}

def completa_Ch(estatic,veloChStats):
    d=ataca[estatic]
    for key in d:
        veloChStats[key]=d[key]
    #print(veloChStats)
    return veloChStats

def canvia_v(self):
    estat,direcc=self.ifi
    vx,vy=self.velTrans[estat][ori[direcc]]
    #print(vx,vy,ori[direcc],sep="/")
    if vx!=None:
        self.vx=vx
    if vy!=None:
        self.vy=vy
    #print("actua",self.current_state,sep="/")

#tipo={"v":[veloStats,veloChStats],"a":[gravetat]}

convertir=(veloChStats,gravetat,ataca,veloStats)

disparar={"D":[15,15],
          "E":[-15,15]}
