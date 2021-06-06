
import pygame
import sys
import math

def create_level_ColRect(level_name,section_width,order_list,mf,screen_size):
    time_rectangles = [1,2,3]
    times = ['past','present','future']
    group_past = pygame.sprite.LayeredUpdates()
    group_present = pygame.sprite.LayeredUpdates()
    group_future = pygame.sprite.LayeredUpdates()
    time_groups = [group_past,group_present,group_future]
    for i in range(3):
        fn = level_name[:-4]+'_'+times[i]+'.txt'
        time_rectangles[i] = create_rectObj_list(fn,section_width,order_list,mf,screen_size)
        time_groups[i].add(time_rectangles[i])
    #return time_rectangles
    return time_groups

def create_rectObj_list(fn,section_width,order_list,zoom_factor,screen_size):
    l = []
    Ordered_ColRect = []
    ColRect_Sections = rect_Sections(fn)
    screen_width,screen_height = screen_size
    #print(fn,order_list,len(ColRect_Sections))
    for i in order_list:
        Ordered_ColRect.append(ColRect_Sections[i])

    for i in range(len(Ordered_ColRect)):
        for e in range(len(Ordered_ColRect[i][0])):
            DIM = Ordered_ColRect[i][0][e]
            POS = Ordered_ColRect[i][1][e]
            zfx = zoom_factor[0]
            rectObj = ColRectObj(DIM,POS,zoom_factor,screen_size)
            rectObj.rect.move_ip(section_width*i*zfx,0)
            l.append(rectObj)
    return l

def rect_Sections(fn):
    f = open(fn,'r')
    sections = []
    get_data = False
    DIM = None
    POS = None
    for line in f:
        data = section_data(line)
        if data != None:
            if data[0] == 'New section':
                current_section = data[1]
                get_data = True
            if get_data and data[0] == 'RDIM':
                DIM = data[1]
            if get_data and data[0] == 'RPOS':
                POS = data[1]
                get_data = False
                if len(DIM) != len(POS):
                    raise Exception(str(abs(len(DIM)-len(POS))) + ' rectangles missing in section ' + str(current_section) + ' of ' + fn)
                sections.append((DIM,POS))
    f.close()
    return sections

def section_data(s):
    s=s.replace('\n','')
    if 'RDIM' in s:
        l = reformat_sizes(s)
        return ('RDIM',l)
    elif 'RPOS' in s:
        l = reformat_sizes(s)
        return ('RPOS',l)
    elif 'Section' in s:
        l = s.split()
        return ('New section',l[1])

def reformat_sizes(s):
    l = s.split('-')
    l = l[1].split(',')
    for i in range(len(l)):
        a = l[i].split('x')
        x = int(a[0])
        y = int(a[1])
        l[i] = (x,y)
    return l


#==========================================================================

class ColRectObj(pygame.sprite.Sprite):
    def __init__(self,DIM,POS,zoom_factor,screen_size):
        super().__init__()
        sc_width, sc_height = screen_size
        x1, y1 = DIM
        x2, y2 = POS
        xf, yf = zoom_factor
        #xf, yf = 1, 1
        dim = (round(x1 * xf), round(y1 * yf))
        pos = [round(x2 * xf), round(y2 * yf)]
        pos[1] = sc_height -(dim[1]+pos[1])

        self.layer = 1
        
        self.image = pygame.Surface(dim,flags=pygame.SRCALPHA)
        self.image.fill((0,0,0))
        #self.image.set_alpha(0)
        self.rect = self.image.get_rect()
        self.rect.move_ip(pos)
        self.previous_pos = self.rect

        

    def update(self,speed):
        self.previous_pos = self.rect
        self.rect.move_ip(speed,0)
