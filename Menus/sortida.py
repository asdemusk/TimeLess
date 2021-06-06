import pygame
import motor

class Exit(motor.Etapa):

    def executa_iteracio(self,Volume):
        #print("GAME OVER")
        return True
