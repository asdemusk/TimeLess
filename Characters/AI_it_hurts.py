import pygame
import sys
import character
import ch_p
import vectors
import character_atributes
import arma
import music


class AI:
    def __init__(self):
        pass

    def update(self,character,enemy,penya,g_armes,sprites,current_level_time,armes_time_list,screen_size,Volume):
        if current_level_time == 0:
            current_time = "past"
        elif current_level_time == 1:
            current_time = "present"
        elif current_level_time == 2:
            current_time = "future"
        gun = enemy.arma
        if not isinstance(enemy,ch_p.Principal):
            character_center = character.rect.center
            enemy_center = enemy.rect.center
            eps = enemy.rect.width# + gun.rect.width
            distx = vectors.distx(character_center,enemy_center)
            dist = vectors.dist(character_center,enemy_center)
            if enemy.estat not in [0,1]:
                if distx > 0 and enemy.ifi[1] == "D":
                    enemy.ifi = (enemy.estat,"E")
                elif distx < 0 and enemy.ifi[1] == "E":
                    enemy.ifi = (enemy.estat,"D")
                
            if enemy.atac_estatic == False  and enemy.temps == current_time: # a distancia
                if enemy.temps_atac == enemy.max_temps_atac:
                    ColRect = None
                    #print(abs(distx)-screen_size[0]//2)
                    if abs(distx) <= screen_size[0]//2:
                        shoot(enemy,character,ColRect,g_armes,sprites,current_level_time,armes_time_list)
                        Volume.shoot(enemy.temps,enemy.atac_estatic)
                    enemy.temps_atac = 0
                else:
                    enemy.temps_atac += 1
                
                
            elif enemy.atac_estatic == True: #cuerpo a cuerpo
                #print(enemy.current_state,distx,arma.n_atacs,enemy.temps_atac,enemy.ifi)
                if abs(distx) <= eps and dist <= eps and enemy.current_state != "ATACA" and enemy.temps == current_time:
                    if enemy.current_state != "MORT":
                        #print(enemy.current_state,enemy.temps_atac,enemy.max_temps_atac)
                        if enemy.temps_atac == enemy.max_temps_atac and enemy.temps == current_time :
                            Volume.shoot(enemy.temps,enemy.atac_estatic)
                            if enemy.current_state == "AIRE":
                                enemy.atac_salt()
                            else:
                                enemy.ataca()
                            enemy.temps_atac = 0
                        elif enemy.current_state != "QUIET":
                            if enemy.current_state == "ATAC_SALT":
                                enemy.aire()
                            else:
                                enemy.para()
                        enemy.temps_atac += 1
                #elif dist > eps and enemy_center[1] == character_center[1] and enemy.current_state not in ["ATACA","AIRE","MORT"] and enemy.temps == current_time and dist <= eps + screen_size[0]/3 and has_hole(enemy):
                elif is_at_correct_distance(enemy,dist,eps,character_center,current_time,screen_size) and not has_hole(enemy):
                    #enemy.colisioned_rect = []
                    if enemy.ifi[1] == "D" and enemy.current_state != "DRETA":
                        enemy.ves_dreta()
                    elif enemy.ifi[1] == "E" and enemy.current_state != "ESQUERRA":
                        enemy.ves_esquerra()
                elif enemy.current_state not in ["QUIET","AIRE","MORT"] and has_hole(enemy): #and enemy.temps != current_time:
                #elif not is_at_correct_distance(enemy,dist,eps,character_center,current_time,screen_size):
                    enemy.para()
                elif enemy.current_state != "QUIET" and enemy.temps != current_time and has_hole(enemy):
                    enemy.para()
                    
    def dany(self,gun,penya):
        enemy=gun.p
        #print(type(gun))
        if isinstance(gun,arma.Arma):
            if gun.atacant and gun.n_atacs>0:
                #self.n_atacs-=1
                sprites=pygame.sprite.spritecollide(gun,penya,False,pygame.sprite.collide_mask)
                #print(g_sprites.sprites())
                for sp in sprites:
                    #print(sp)
                    if sp!=enemy and pygame.sprite.collide_mask(sp,gun)!=None:
                        gun.n_atacs-=1
                        sp.impacte(gun.dany)

        else:
            sprites=pygame.sprite.spritecollide(gun,penya,False)
            for sp in sprites:
                if sp!=enemy and pygame.sprite.collide_mask(sp,gun)!=None:
                    sp.impacte(gun.dany)
                    gun.kill()

def shoot(Shooter,Player,ColRect,g_armes,sprites,current_level_time,armes_time_list):
    plc = Player.rect.center
    shc = Shooter.arma.rect.center
    #print(plc,shc)
    '''vect0 = ColRect.rect.topleft
    vect1 = ColRect.rect.bottomleft
    vect2 = ColRect.rect.bottomright
    vect3 = ColRect.rect.topright'''
    straight_dist = vectors.dif(shc,plc)
    '''dist0 = vectors.dif(shc,v0)
    dist1 = vectors.dif(shc,v1)
    dist2 = vectors.dif(shc,v2)
    dist3 = vectors.dif(shc,v3)'''

    arma = Shooter.arma
    if Shooter.temps == "past":
        frames_alive = 50
        g = Shooter.gravetat
        vx0 = round((plc[0]-shc[0])/frames_alive)
        vy0 = round((plc[1]-shc[1]-0.5*g[1]*frames_alive**2)/frames_alive)

        '''vx0 = -5
        vy0 = -10'''

        vel = vx0,vy0
    else:
        frames_alive = 8
        vel = vectors.esc_vect(frames_alive,vectors.normalitza(straight_dist))
    arma.dispara(g_armes,sprites,vel,current_level_time,armes_time_list)
    
def has_hole(enemy):
    colisioned_rect = enemy.colisioned_rect
    enemy_rect = enemy.rect
    enemy_rect_left = enemy_rect.left
    enemy_rect_right = enemy_rect.right
    #print(colisioned_rect)
    colisioned_rect_left = colisioned_rect.left
    colisioned_rect_right = colisioned_rect.right
    if (enemy_rect_right > colisioned_rect_right and enemy.ifi[1] == "D") or (enemy_rect_left < colisioned_rect_left and enemy.ifi[1] == "E"):
        #print(True)
        #print(enemy_rect_right > colisioned_rect_right and enemy.ifi[1] == "D",enemy_rect_left < colisioned_rect_left and enemy.ifi[1] == "E")
        return True
    #print(False)
    return False
def is_at_correct_distance(enemy,dist,eps,character_center,current_time,screen_size):
    if enemy.temps == current_time:
        if dist > eps and dist < eps + screen_size[0] / 3:
            if enemy.current_state not in ["ATACA","AIRE","MORT"]:
                return True
    return False
