screen_size=0,0

sc_width,sc_height = screen_size

de=20

ordr="past present future".split()

A=[[0,(335,541),1],[0,(335,381),1],[0,(535,661),0],[0,(535,661),0],
   [0,(1584,381),1],[0,(1854,381),1],[0,(2010,541),1],[0,(2496,661),0],
   [0,(2748,541),1],[0,(3468,661),0],[0,(4086,541),1],[0,(5196,661),0],
   [0,(5268,381),1],[0,(5454,381),1],[0,(5838,381),1],[0,(6186,381),1],
   [0,(6522,541),0],[0,(6570,541),0],[0,(6630,541),0],[0,(6690,541),0],
   [0,(6726,541),0],[0,(7368,541),1],[0,(7800,541),1],[0,(9348,661),0],
   [0,(9540,661),0],[0,(9690,661),1],[0,(9822,661),0],[0,(10524,479),1],
   [0,(10542,381),1],[0,(10992,661),0],[0,(11682,541),0],[0,(12396,661),1],
   [0,(12948,541),0],[0,(13002,541),0],[0,(13068,541),0],[0,(13116,541),0],
   [0,(13920,661),1],[0,(14568,661),1],[0,(15010,661),0],[0,(15085,661),0],
   [0,(15035,661),0],[0,(15165,661),0],[0,(15275,661),0]]

B=[[2,(960,181),1],[2,(1794,301),1],[2,(3192,301),1],[2,(4500,421),1],
   [2,(5280,61),1],[2,(7044,301),1],[2,(7980,661),0],[2,(8634,661),0],
   [2,(9882,181),1],[2,(10200,-64),1],[2,(12018,61),1],[2,(14148,181),1],
   [2,(15120,61),1],[2,(15075,61),1],[2,(15025,61),1],[2,(15200,61),1],
   [2,(15020,301),1],[2,(15155,421),1],[2,(14955,661),0],[2,(15105,661),0],
   [1,(918,421),1],[1,(1362,421),1],[1,(1878,321),1],[1,(1716,661),0],
   [1,(1266,661),0],[1,(2358,421),1],[1,(3072,541),1],[1,(3426,161),1],
   [1,(4038,661),0],[1,(4362,541),1],[1,(4494,541),1],[1,(4920,311),1],
   [1,(5244,421),1],[1,(6486,321),1],[1,(6348,661),0],[1,(7338,421),1],
   [1,(7494,541),1],[1,(8388,661),0],[1,(8718,661),0],[1,(9048,661),0],
   [1,(9522,661),0],[1,(10800,541),1],[1,(10908,541),1],[1,(11238,541),1],
   [1,(11298,321),1],[1,(12504,421),1],[1,(13446,321),1],[1,(13950,541),1],
   [1,(15195,541),1],[1,(15195,374),1],[1,(15125,661),0]]

C=[[0,(485,661),0],[0,(1464,661),0],[0,(2652,661),0],[0,(3756,661),0],
   [0,(5226,661),0],[0,(6486,661),0],[0,(7355,661),0],[0,(936,661),1],
   [0,(1470,661),1],[0,(2058,661),1],[0,(2640,661),1],[0,(3876,661),1],
   [0,(4632,661),1],[0,(5250,661),1],[0,(5862,661),1],[0,(6510,661),1],
   [0,(7235,661),1],[0,(440,661),0],[0,(1026,661),0],[0,(1674,661),0],
   [0,(2310,661),0],[0,(2976,661),0],[0,(3552,661),0],[0,(4254,661),0],
   [0,(4938,661),0],[0,(5544,661),0],[0,(6138,661),0],[0,(6726,661),0],
   [0,(7315,661),0],[1,(240,521),1],[1,(882,421),1],[1,(1176,661),0],
   [1,(1674,421),1],[1,(2154,421),1],[1,(2154,421),0],[1,(2850,661),1],
   [1,(3000,661),0],[1,(3462,561),1],[1,(4098,661),0],[1,(4560,498),1],
   [1,(5352,498),0],[1,(5778,421),1],[1,(5484,421),1],[1,(5436,421),1],
   [1,(5364,421),1],[1,(5274,421),1],[1,(5226,421),1],[1,(7375,521),1],
   [1,(7535,381),1],[2,(480,241),1],[2,(654,501),1],[2,(912,341),1],
   [2,(1332,541),1],[2,(1506,381),1],[2,(1728,241),1],[2,(1974,121),1],
   [2,(3012,241),1],[2,(3444,341),1],[2,(3888,541),1],[2,(4290,241),1],
   [2,(4476,501),1],[2,(4722,341),1],[2,(5868,121),1],[2,(6054,341),1],
   [2,(6378,561),1]]

O=[]

principal=["present",(0,sc_height/3),50,100,True,96]

def ll_p(lvl):
    l=[]
    for el in lvl:
        t,pos,d=el
        x,y=pos
        p=[ordr[t],(x,y-1),de,100,d==1,96]
        l.append(p)
    return l

def pers(*args):
    l=[]
    for el in args:
        l.append(ll_p(el))
    return l

A,B,C=pers(A,B,C)

p_n=[[[principal]+A,"I??aki/Level1_data.txt"],[[principal]+B,"I??aki/Level2_data.txt"],[[principal]+C,"I??aki/Level3_data.txt"]]

def act_principal():
    fin=open("Characters/Weapon_save.txt","r")
    for line in fin:
        line=line.strip()
        t,dist=line.split()
    principal[0]=t
    principal[4]=dist=="1"
    fin.close()

act_principal()
