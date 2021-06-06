import pygame
import teclat
import canvi_estat
import control

import Scenery

def tracta_events(pers,current_level,g_armes,sprites,joc,current_level_time,armes_time_list,Volume):#onatges,current_level):
    final=False
    tec_events=teclat.decod()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            final=True
        elif event.type==pygame.KEYDOWN:

            Scenery.change_time(current_level,event)
                
            if event.key in control.c_game["dreta"]:
                if pers.estat in (4,9):
                    pers.ifi=(pers.ifi[0],"D")
                    pers.orientacio=1
                else:
                    if canvi_estat.legal("ves_dreta",pers):
                        pers.ves_dreta()
                if pers.estat==10:
                    pers.orientacio=1
                    pers.ifi=(10,"D")
            elif event.key in control.c_game["esquerra"]:
                if pers.estat in (4,9):
                    pers.ifi=(pers.ifi[0],"E")
                    pers.orientacio=-1
                else:
                    if canvi_estat.legal("ves_esquerra",pers):
                        pers.ves_esquerra()
                if pers.estat==10:
                    pers.orientacio=-1
                    pers.ifi=(10,"E")
            elif event.key in control.c_game["ajup"] and canvi_estat.legal("ajupir",pers):
                pers.ajupir()
            elif event.key in control.c_game["ataca"]:
                Volume.shoot(pers.temps,pers.atac_estatic)
                if pers.atac_estatic:
                    if canvi_estat.legal("ataca",pers):
                        pers.ataca()
                    elif canvi_estat.legal("atac_salt",pers):
                        pers.atac_salt()
                else:
                    if pers.temps=="past":
                        vy=pers.arma.disparar["D"][1]
                    else:
                        vy=0
                    v=(pers.arma.disparar[pers.ifi[1]][0],vy)
                    pers.arma.dispara(g_armes,sprites,v,current_level_time,armes_time_list)
            elif event.key==pygame.K_ESCAPE:
                joc.to_pause()
            elif event.key in control.c_game["salta"]:
                if pers.estat in (0,1) and canvi_estat.legal("aire",pers):
                    pers.aire()
                    pers.vy=pers.vel[9][0][1]
                elif canvi_estat.legal("salta",pers):
                    pers.salta()
            elif event.key in control.c_menu["intro"]:
                if event.key==pygame.K_RETURN:
                    asdf=0
                else:
                    asdf=1
                #print(pers.rect.left - current_level.rect.left,pers.rect.bottom,asdf)
            
        if event.type==pygame.KEYUP:
            if canvi_estat.legal("para",pers) and pers.estat in (0,1):
                pers.para()
            if event.key in control.c_game["dreta"]:
                if quest_in(crea_st(control.edit_game,"esquerra"),tec_events,True) and canvi_estat.legal("ves_esquerra",pers):#"a" in tec_events
                    pers.ves_esquerra()
            elif event.key in control.c_game["esquerra"]:
                if quest_in(crea_st(control.edit_game,"dreta"),tec_events,True) and canvi_estat.legal("ves_dreta",pers):
                    pers.ves_dreta()
            elif event.key in control.c_game["ajup"] and pers.estat==10:
                pers.aixecant()
        
        pers.fila=pers.files_imatges.index(pers.ifi)
    return final

para="right/left/down".split("/")

def no_apretades(comprovar,apretades):
    continua=True
    for tecla in comprovar:
        print(tecla,apretades)
        if tecla in apretades:
            continua=False
            break
    print(continua)
    return continua

def crea_st(d,*keys):
    l=[]
    for key in keys:
        l+=d[key]
    #print(l)
    return l

def quest_in(l,ch,isin):
    if isin:
        resp=False
    else:
        resp=True
    for el in l:
        if el in ch:
            if isin:
                resp=True
            else:
                resp=False
            break
    return resp
