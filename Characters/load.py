import pygame
from os import listdir
from copy import deepcopy

d_temps={"past":("Templario","Temp",("Espasa","Ballesta","Fletxa")),
         "present":("SWAT","Swat",("Porra","AK","Bala")),
         "future":("Future","FS",("Sable","Blaster","Laser"))}

d_noms={"Ajup":4,"Ataca":5,"Ataca_S":8,"Aterra":7,"Camina":(0,1),"Mort":6,
        "Quiet_Salta":(2,9),"Salta":3,"Aixecant":11,"Ajupit":10}

prefix="Image/"

def load_images_personatge(temps,projectil,principal):
    if principal:
        carpeta,pref="Principal","Principal"
    else:
        carpeta,pref=d_temps[temps][0:2]
    files_imatges=[]
    im_personatge=[]
    for imatge in listdir(prefix+carpeta):
        s=imatge[:-4]
        lon_i=len(pref)+1
        direccio=s[-1]
        nom=s[lon_i:-2]
        decod=d_noms[nom]
        if isinstance(decod,int) or decod==None:
            if projectil and decod in (8,5):
                imatge="{}-Quiet_Salta-{}.png".format(pref,direccio)
            path=prefix+carpeta+"/"+imatge
            im_personatge.append(pygame.image.load(path))
            tup=(decod,direccio)
            files_imatges.append(tup)         
        else:
            path=prefix+carpeta+"/"+imatge
            if decod==(0,1):
                im_personatge.append(pygame.image.load(path))
                if direccio=="D":
                    files_imatges.append((0,"D"))
                else:
                    files_imatges.append((1,"E"))
            else:
                for estat in decod:
                    im_personatge.append(pygame.image.load(path))
                    tup=(estat,direccio)
                    files_imatges.append(tup)
    return im_personatge,files_imatges

def load_arma(temps,projectil):
    carpeta="Armas"
    path=prefix+carpeta+"/"
    if projectil:
        arma,proj=d_temps[temps][2][1:]
        im_arma=[]
        im_proj=[]
        direccions_a=["D","E"]
        for i in range(2):
            im_a=pygame.image.load(path+"{}_{}.png".format(arma,direccions_a[i]))
            im_arma.append(im_a)
            im_p=pygame.image.load(path+"{}_{}.png".format(proj,direccions_a[i]))
            im_proj.append(im_p)
    else:
        im_arma=[]
        #print(temps)
        arma=d_temps[temps][2][0]
        im_proj=None
        for i in range(3):
            im=pygame.image.load(path+"{}_{}.png".format(arma,i))
            im_arma.append(im)
    return im_arma,im_proj

d_armes={"past":[[[4,7],[7,49],[49,7]],[[32,47],[94,47]]],
         "present":[[[5,7],[7,48],[48,7]],[[28,14],[51,14]]],
         "future":[[[6,7],[7,47],[47,7]],[[35,21],[44,21]]]}

d_mele={"past":{"D":{6:[[75,41],[75,44],[75,47],[75,53]],
                     8:[[75,41],[72,29],[65,14],[72,29],[81,32],
                        [72,29],[75,41]],
                     -1:[75,41],
                     4:[[75,41],[75,44],[75,50],[75,56]],
                     7:[[75,41],[75,47],[75,44],[75,41]],
                     5:[[75,41],[72,22],[65,17],[72,32],[81,35],
                        [72,32],[75,41],[75,41]],
                     3:[[75,41],[75,44],[75,47],[75,41]],
                     11:[[75,56],[75,50],[75,54],[75,41]],
                     10:[[75,56]]},
                "E":{6:[[20,41],[20,44],[20,47],[20,53]],
                     8:[[20,41],[23,29],[30,14],[23,29],[14,32],
                        [23,29],[20,41]],
                     -1:[20,41],
                     4:[[20,41],[20,44],[20,50],[20,56]],
                     7:[[20,41],[20,47],[20,44],[20,41]],
                     5:[[20,41],[23,22],[30,17],[23,32],[14,35],
                        [23,32],[20,41],[20,41]],
                     3:[[20,41],[20,44],[20,47],[20,41]],
                     11:[[20,56],[20,50],[20,54],[20,41]],
                     10:[[20,56]]}},
        "present":{"D":{6:[[69,44],[69,47],[69,53],[69,59]],
                        8:[[69,44],[72,32],[65,17],[72,32],[81,35],
                           [72,32],[69,44]],
                        -1:[69,44],
                        4:[[69,44],[69,47],[69,53],[69,62]],
                        7:[[69,44],[69,50],[69,47],[69,44]],
                        5:[[69,44],[72,32],[66,20],[72,35],[81,38],
                           [72,35],[69,44],[69,44]],
                        3:[[69,44],[69,47],[69,50],[69,44]],
                        11:[[69,62],[69,53],[69,47],[69,44]],
                        10:[[69,62]]},
                   "E":{6:[[26,44],[26,47],[26,53],[26,59]],
                        8:[[26,44],[23,32],[29,17],[23,32],[14,35],
                           [23,32],[26,44]],
                        -1:[26,44],
                        4:[[26,44],[26,47],[26,53],[26,62]],
                        7:[[26,44],[26,50],[26,47],[26,44]],
                        5:[[26,44],[23,32],[30,20],[23,35],[14,38],
                           [23,35],[26,44],[26,44]],
                        3:[[26,44],[26,47],[26,50],[26,44]],
                        11:[[26,62],[26,53],[26,47],[26,44]],
                        10:[[26,62]]}},
        "future":{"D":{6:[[69,44],[69,47],[69,56],[69,62]],
                      8:[[69,44],[75,29],[65,17],[75,29],[78,35]
                         ,[75,29],[69,44]],
                       -1:[69,44],
                       4:[[69,44],[69,47],[69,56],[69,68]],
                       7:[[69,44],[69,50],[69,47],[69,44]],
                       5:[[69,44],[75,29],[65,20],[75,32],[78,38],
                          [75,32],[69,44],[69,44]],
                       3:[[69,44],[69,47],[69,50],[69,44]],
                       11:[[69,68],[69,56],[69,47],[69,44]],
                       10:[[69,68]]},
                 "E":{6:[[26,44],[26,47],[26,56],[26,62]],
                      8:[[26,44],[20,29],[30,17],[20,29],[17,35]
                         ,[20,29],[26,44]],
                      -1:[26,44],
                      4:[[26,44],[26,47],[26,56],[26,68]],
                      7:[[26,44],[26,50],[26,47],[26,44]],
                      5:[[26,44],[20,29],[29,20],[20,32],[17,38],
                          [20,32],[26,44],[26,44]],
                      3:[[26,44],[26,47],[26,50],[26,44]],
                      11:[[26,68],[26,56],[26,47],[26,44]],
                      10:[[26,68]]}}}

"""d_disparar={"past":[[92,32],[35,32]],
            "present":[[75,8],[4,8]],
            "future":[[],[]]}"""

def delete_dict(dic,*keys):
    for k in keys:
        del dic[k]

d_distancia=deepcopy(d_mele)
for el in ["past","future","present"]:
    for elem in ["D","E"]:
        d=d_distancia[el][elem]
        delete_dict(d,8,5)

d_dicc={"mele":(d_mele,0),"dist":(d_distancia,1)}

disparar={"past":[[92,32],[35,32]],
            "present":[[75,8],[4,8]],
            "future":[[79,12],[0,12]]}

def carrega_d(temps,projectil,principal):
    #print(d_disparar)
    if projectil:
        dicc="dist"
        if principal:
            d_ma=deepcopy(d_dicc[dicc][0]["future"])
        else:
            d_ma=deepcopy(d_dicc[dicc][0][temps])
        punt_arma=deepcopy(d_armes[temps][d_dicc[dicc][1]])
        d_dispara=deepcopy(disparar[temps])
    else:
        dicc="mele"
        if principal:
            d_ma=deepcopy(d_dicc[dicc][0]["future"])
        else:
            d_ma=deepcopy(d_dicc[dicc][0][temps])
        punt_arma=deepcopy(d_armes[temps][d_dicc[dicc][1]])
        d_dispara=None
    #print(d_ma,punt_arma,sep="/")
    return [d_ma,punt_arma,d_dispara]
