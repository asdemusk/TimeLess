import pygame
import vectors
import character
import Scenery
import ColRect
import character_atributes as ch_a
import ch_p
import copy
import arma
import projectil

d_especial={"pos_arma":1,"dispara":2}

def zoom(sprite,pantalla,**keyargs):#fact=1/9):
    width,height=pantalla
    if "especial" in keyargs:
        especial=keyargs["especial"]
    else:
        especial=False
    if (isinstance(sprite,character.Character) or isinstance(sprite,ch_p.Principal)) and not especial:
        if "fact" in keyargs:
            fact=keyargs["fact"]
        else:
            fact=1/9
        for i in range(len(sprite.im_list)):
            for j in range(len(sprite.im_list[i])):
                sp=sprite.im_list[i][j]
                ws,hs=sp.get_size()
                tupy=fact*height
                escala=tupy/hs
                tup=(round(escala*ws),round(tupy))
                #print(tup,sprite.files_imatges[i])
                sprite.im_list[i][j]=pygame.transform.scale(sp,tup)
        for i in range(len(sprite.arma.im_list)):
            #for j in range(len(sprite.arma.im_list[i])):
            sp=sprite.arma.im_list[i]
            ws,hs=sp.get_size()
            tup=(round(escala*ws),round(escala*hs))
            sprite.arma.im_list[i]=pygame.transform.scale(sp,tup)
        for i in range(len(sprite.arma.d_pos)):
            d=sprite.arma.d_pos[i]
            if isinstance(d,list):
                for j in range(len(d)):
                    sprite.arma.d_pos[i][j]=vectors.esc_vect(escala,d[j])
            else:
                for dir in d:
                    for est in d[dir]:
                        if est!=-1:
                            for j in range(len(d[dir][est])):
                                #print(d[dir][est],dir,est,sep="/")
                                sprite.arma.d_pos[i][dir][est][j]=vectors.esc_vect(escala,d[dir][est][j])
                        else:
                            sprite.arma.d_pos[i][dir][est]=vectors.esc_vect(escala,d[dir][est])


    elif isinstance(sprite,Scenery.scenery) and not especial:
        if 'order_list' and 'ColRect_fn':
            order_list = keyargs['order_list']
            ColRect_fn = keyargs['ColRect_fn']
        n = len(order_list)
        im2 = [[0],[1],[2]]
        section_width, section_height = sprite.rect.size
        screen_width, screen_height = pantalla

        zfx = screen_width/section_width
        zfy = screen_height/section_height
        zoom_factor = (zfx,zfy)
        rz = screen_height / 36
        rect_zoom_factor = (rz,rz)
        #self.speed = self.speed * mf
        sprite.ColRect_times = ColRect.create_level_ColRect(ColRect_fn,section_width,order_list,rect_zoom_factor,pantalla)

        
        ipast = pygame.Surface((section_width*n,section_height))
        ipresent = pygame.Surface((section_width*n,section_height))
        ifuture = pygame.Surface((section_width*n,section_height))
        im3 = [ipast,ipresent,ifuture]
        for i in range(n):
            for e in range(sprite.num_temps):
                im3[e].blit(sprite.im[e][order_list[i]], (i*section_width,0)) #para la version final ha que cambiar el orden fila columna
            #ipresent.blit(sprite.im[1][order_list[i]], (i*section_width,0))
            #ifuture.blit(sprite.im[2][order_list[i]], (i*section_width,0))
           #print(i)
           #print(i*width)
        #print(sprite.rect.size)
        xi = section_width*zfy*n/20
        yi = screen_height/20
        #for i in range(1,21):
            #print(i)
        tup = (round(xi*20),round(yi*20))
        im2[0][0] = pygame.transform.scale(im3[0],tup)
        im2[1][0] = pygame.transform.scale(im3[1],tup)
        im2[2][0] = pygame.transform.scale(im3[2],tup)

        sprite.im = im2

    elif especial=="im_arma" or especial=="projectil":
        if "fact" in keyargs:
            fact=keyargs["fact"]
        else:
            fact=1/9
        for i in range(len(sprite)):
            sp=sprite[i]
            ws,hs=sp.get_size()
            tup=(round(fact*ws),round(fact*hs))
            sprite[i]=pygame.transform.scale(sp,tup)

    elif especial in d_especial:
        #print(especial)
        k=d_especial[especial]
        est=sprite[k]
        if "fact" in keyargs:
            fact=keyargs["fact"]
        else:
            fact=1/9
        #print(est)
        for i in range(len(est)):
            for j in range(len(est[i])):
                sprite[k][i]=vectors.esc_vect(fact,est[i])
    

def dropTheBase(vect,type_vect,fact,pantalla=None,sprite=None):
    x,y=vect
    if type_vect=="vel" or type_vect=="acc":
        if x!=None:
            newx=x*fact
        else:
            newx=x
        if y!=None:
            newy=-y*fact
        else:
            newy=y
        return [newx,newy]
    elif type_vect=="pos":
        if pantalla==None:
            raise Exception("'pantalla' required")
        if sprite==None:
            raise Exception("'sprite' required")
        return [x*fact,(pantalla[1]-(sprite.height+y))*fact]
    else:
        raise Exception("Type of vector not correct")

def drop_Character(screen_size,estatic):
    fact=screen_size[1]/1280
    vel=copy.deepcopy(ch_a.veloStats)
    vel_trans=copy.deepcopy(ch_a.veloChStats)
    vel_trans=ch_a.completa_Ch(estatic,vel_trans)
    g=dropTheBase(copy.deepcopy(ch_a.gravetat),"acc",fact)
    for estat in vel:
        for dire in range(len(vel[estat])):
            #print(estat,dire,sep="/")
            vel[estat][dire]=dropTheBase(vel[estat][dire],"vel",fact)
            vel_trans[estat][dire]=dropTheBase(vel_trans[estat][dire],"vel",fact)
    return vel,vel_trans,g

def drop_Arma(fact):
    d=copy.deepcopy(ch_a.disparar)
    for key in d:
        d[key]=dropTheBase(d[key],"vel",fact)
    return d

def drop_Live(screen_size):
    fact=screen_size[1]/1280
    g=dropTheBase(copy.deepcopy(ch_a.gravetat),"acc",fact)
    return g
