import pygame
import ch_p
import buscar
import random
import extra_live

def colisions(g_pers,all_ColRects,current_level,screen_size,final,current_level_time,joc,Lives):
    for p in g_pers:
        if isinstance(p,ch_p.Principal):
            principal=p
            for live in pygame.sprite.spritecollide(p,Lives,True,pygame.sprite.collide_mask):
                joc.etapa_estat["Game"].cor()
        if p.do_kill:
            p.arma.kill()
            if isinstance(p,ch_p.Principal):
                joc.etapa_estat["Game"].resta_vida()
                joc.etapa_estat["Game"].current_lvl.reini_sprites()
                speed=p=None
                break
            else:
                if random.random()<.1:
                    l=extra_live.Live(p)
                    Lives.add(l)
                    joc.etapa_estat["Game"].current_lvl.sprites.add(l)
                p.kill()
        if not isinstance(p,ch_p.Principal):
            if p.temps == "past":
                colision_list = pygame.sprite.spritecollide(p,all_ColRects[0],False)
            elif p.temps == "present":
                colision_list = pygame.sprite.spritecollide(p,all_ColRects[1],False)
            elif p.temps == "future":
                colision_list = pygame.sprite.spritecollide(p,all_ColRects[2],False)
        else:
            colision_list = pygame.sprite.spritecollide(p,all_ColRects[current_level_time],False)#,pygame.sprite.collide_mask)
        for live in Lives:
            for rect in colision_list:
                if live.rect.bottom >= rect.rect.top and live.rect_antiga.bottom <= rect.rect.top:
                    live.g=False
                    live.rect.bottom=rect.rect.top-1
                    live.vy=0
        if len(colision_list) >= 1:
            no_terra=True
            '''if not isinstance(p,ch_p.Principal):
                p.colisioned_rect = []'''
            for rect in colision_list:
                colision_point = pygame.sprite.collide_mask(rect,p)
                if p.rect.bottom >= rect.rect.top and p.rect_antiga.bottom <= rect.rect.top:
                    if colision_point != None:
                        if not p.terra:
                            if p.vida==0:
                                p.para()
                            else:
                                p.aterra()
                        
                        p.terra = True
                        p.rect.bottom=rect.rect.top+1
                        p.update(screen_size,current_level.speed)
                        p.arma.update(screen_size)

                        
                        if not isinstance(p,ch_p.Principal):
                            if abs(p.rect.centerx - rect.rect.centerx) <= screen_size[0] / 2:
                                #print(rect.rect.centerx)
                                p.colisioned_rect = rect.rect
                else:
                    if colision_point == None and p.rect.bottom < round((screen_size[1]*(11/12)-2)):
                        if p.current_state == "QUIET" or p.current_state == "ESQUERRA" or p.current_state == "DRETA":
                            p.terra = False
                        if p.estat==10:
                            p.aire()               
        else:
            p.terra = False
            if p.estat==10:
                p.aire()
    speed=principal.speed
    return speed, principal, final
