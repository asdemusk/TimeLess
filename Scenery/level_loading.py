import Scenery

CRP = 'Scenery/'

def load_levels(levels_file,screen_size):
    level_data = ['Levl Name','Image file','Matrix Dimensions','ColRect File','section order']
    all_levels = []
    f = open(levels_file,'r')
    for line in f:
        line = line.replace('\n','')
        if '--' not in line:
            level_data[0] = line
        else:
            line = line.replace('--','')
            l = line.split(':')
            if l[0] == 'Image file':
                level_data[1] = l[1][1:]
            elif l[0] == 'Image matrix dimensions':
                level_data[2] = (int(l[1][2]),int(l[1][4]))
            elif l[0] == 'Colisionable rectangles file':
                level_data[3] = l[1][1:]
            elif l[0] == 'Section order':
                line = l[1][1:].split(',')
                for i in range(len(line)):
                    line[i] = int(line[i])
                level_data[4] = line
                lbd = level_data
                level = Scenery.scenery(lbd[1],lbd[2],CRP+lbd[3],lbd[4],screen_size)
                all_levels.append(level)
                level_data = ['Levl Name','Image file','Matrix Dimensions','ColRect File','section order']
    return all_levels
