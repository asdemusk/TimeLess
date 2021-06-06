import pygame
import sys
sys.path.insert(0,'Scenery')
sys.path.insert(0,'NotOurFunctions')
sys.path.insert(0,'Image')
sys.path.insert(0,'Scroll_lib')
sys.path.insert(0,'Characters')
sys.path.insert(0,'OtherFunctions')
sys.path.insert(0,'Menus')
sys.path.insert(0,'Controls')
sys.path.insert(0,'Music')

import main
import music

def TimeLess():
    pygame.init()
    screen_size = (1280, 720)
    intermediate_size = (1280, 720)
    #screen_size = (1920,1080)
    #screen_size = (64,36)
    pantalla=pygame.display.set_mode(screen_size)
    pygame.display.set_caption("TimeLess")
    pygame.mouse.set_visible(False)

    Volume = music.Volume()
    #print(Volume.get_volumes())
    main.main(pantalla,screen_size,intermediate_size,Volume)
    pygame.mixer.quit()
    
if __name__=="__main__":
    TimeLess()
