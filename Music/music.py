import pygame
import botons
pygame.mixer.init()

class Volume():
    def __init__(self):
        self.background = pygame.mixer.music.load("Music/"+"prueba_sonido.ogg")
        shoot_past = pygame.mixer.Sound("Music/Sonidos sin copyright/"+"arrows.ogg")
        shoot_present = pygame.mixer.Sound("Music/Sonidos sin copyright/"+"gun-shot.ogg")
        shoot_future = pygame.mixer.Sound("Music/Sonidos sin copyright/"+"laser-sound.ogg")

        punch_past = pygame.mixer.Sound("Music/Sonidos sin copyright/"+"sword.ogg")#punch.ogg")
        punch_present = pygame.mixer.Sound("Music/Sonidos sin copyright/"+"punch.ogg")#sword.ogg")
        punch_future = pygame.mixer.Sound("Music/Sonidos sin copyright/"+"lightsaber.ogg")
        
        self.weapon_sounds = [shoot_past, shoot_present, shoot_future, punch_past, punch_present, punch_future]
        
        self.general_volume = float(botons.troba_vol("general"))/100
        self.background_volume = float(botons.troba_vol("backg"))/100
        self.weapon_volume = float(botons.troba_vol("enemy"))/100
        self.set_general_volume(self.general_volume)

    def set_background_volume(self,n):
        pygame.mixer.music.set_volume(n*self.general_volume)
        self.background_volume = n

    def set_weapon_volume(self,n):
        for i in self.weapon_sounds:
            i.set_volume(n*self.general_volume)
        self.weapon_volume = n
        
    def set_general_volume(self,n):
        self.general_volume = n
        self.set_background_volume(self.background_volume)
        self.set_weapon_volume(self.weapon_volume)


    def get_volumes(self):
        return self.general_volume,pygame.mixer.music.get_volume(),self.weapon_sounds[0].get_volume()
        
    def play_background(self,paused):
        if paused:
            pygame.mixer.music.unpause()
        else:
            pygame.mixer.music.play(-1)
        return False
    def pause_background(self):
        pygame.mixer.music.pause()
    def stop_background(self):
        pygame.mixer.music.stop()
        
    def shoot(self,character_time,enemy_type):
        if enemy_type: #Cuerpo a cuerpo
            enemy_type = "cuerpo a cuerpo"
        else:
            enemy_type = "distancia"
        if enemy_type == "distancia":
            shoot_past, shoot_present, shoot_future = self.weapon_sounds[0:3]
        elif enemy_type == "cuerpo a cuerpo":
            shoot_past, shoot_present, shoot_future = self.weapon_sounds[3:]
            
        if character_time == "past":
            shoot_past.play()
        elif character_time == "present":
            shoot_present.play()
        elif character_time == "future":
            shoot_future.play()
        
#pygame.mixer.quit()
