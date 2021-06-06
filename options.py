import pygame
import edit_control

class Options:

    def __init__(self,joc,ll_fnames):
        self.screens=[]
        for scr in ll_fnames:
            self.screens.append(edit_control.Changes(joc,scr,self,len(ll_fnames)>1))
        self.index=0
        self.current_scr=self.screens[self.index]

    def executa_iteracio(self,Volume):
        return self.current_scr.executa_iteracio(Volume)

    def go_forward(self):
        self.index+=1
        #print(self.index,len(self.screens),sep=" / ")
        if self.index>=len(self.screens):
            self.index=0
        self.current_scr=self.screens[self.index]
        """i=self.current_scr.index
        if i//2==0:
            self.current_scr.index=0
        else:
            if len(self.current_scr.ll_botons)>1:
                self.current_scr.index=1
            else:
                self.current_scr.index=0"""
        self.current_scr.index=0
