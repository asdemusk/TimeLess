import pygame

especial={"up":"up arrow","down":"down arrow","left":"left arrow","right":"right arrow"}

tc={"backspace":pygame.K_BACKSPACE,
    "tab":pygame.K_TAB,
    "clear":pygame.K_CLEAR,
    "return":pygame.K_RETURN,
    "pause":pygame.K_PAUSE,
    "escape":pygame.K_ESCAPE,
    "space":pygame.K_SPACE,
    "exclaim":pygame.K_EXCLAIM,
    "quotedbl":pygame.K_QUOTEDBL,
    "hash":pygame.K_HASH,
    "dollar":pygame.K_DOLLAR,
    "ampersand":pygame.K_AMPERSAND,
    "quote":pygame.K_QUOTE,
    "left parenthesis":pygame.K_LEFTPAREN,
    "right parenthesis":pygame.K_RIGHTPAREN,
    "asterisk":pygame.K_ASTERISK,
    "plus sign":pygame.K_PLUS,
    "comma":pygame.K_COMMA,
    "minus sign":pygame.K_MINUS,
    "period":pygame.K_PERIOD,
    "forward slash":pygame.K_SLASH,
    "0":pygame.K_0,
    "1":pygame.K_1,
    "2":pygame.K_2,
    "3":pygame.K_3,
    "4":pygame.K_4,
    "5":pygame.K_5,
    "6":pygame.K_6,
    "7":pygame.K_7,
    "8":pygame.K_8,
    "9":pygame.K_9,
    "colon":pygame.K_COLON,
    "semicolon":pygame.K_SEMICOLON,
    "less-than sign":pygame.K_LESS,
    "equals sign":pygame.K_EQUALS,
    "greater-than sign":pygame.K_GREATER,
    "question mark":pygame.K_QUESTION,
    "at":pygame.K_AT,
    "left bracket":pygame.K_LEFTBRACKET,
    "backslash":pygame.K_BACKSLASH,
    "right bracket":pygame.K_RIGHTBRACKET,
    "caret":pygame.K_CARET,
    "underscore":pygame.K_UNDERSCORE,
    "grave":pygame.K_BACKQUOTE,
    "a":pygame.K_a,
    "b":pygame.K_b,
    "c":pygame.K_c,
    "d":pygame.K_d,
    "e":pygame.K_e,
    "f":pygame.K_f,
    "g":pygame.K_g,
    "h":pygame.K_h,
    "i":pygame.K_i,
    "j":pygame.K_j,
    "k":pygame.K_k,
    "l":pygame.K_l,
    "m":pygame.K_m,
    "n":pygame.K_n,
    "o":pygame.K_o,
    "p":pygame.K_p,
    "q":pygame.K_q,
    "r":pygame.K_r,
    "s":pygame.K_s,
    "t":pygame.K_t,
    "u":pygame.K_u,
    "v":pygame.K_v,
    "w":pygame.K_w,
    "x":pygame.K_x,
    "y":pygame.K_y,
    "z":pygame.K_z,
    "delete":pygame.K_DELETE,
    "[0]":pygame.K_KP0,
    "[1]":pygame.K_KP1,
    "[2]":pygame.K_KP2,
    "[3]":pygame.K_KP3,
    "[4]":pygame.K_KP4,
    "[5]":pygame.K_KP5,
    "[6]":pygame.K_KP6,
    "[7]":pygame.K_KP7,
    "[8]":pygame.K_KP8,
    "[9]":pygame.K_KP9,
    "[.]":pygame.K_KP_PERIOD,
    "[/]":pygame.K_KP_DIVIDE,
    "[*]":pygame.K_KP_MULTIPLY,
    "[-]":pygame.K_KP_MINUS,
    "[+]":pygame.K_KP_PLUS,
    "enter":pygame.K_KP_ENTER,
    "keypad equals":pygame.K_KP_EQUALS,
    "up":pygame.K_UP,
    "down":pygame.K_DOWN,
    "right":pygame.K_RIGHT,
    "left":pygame.K_LEFT,
    "insert":pygame.K_INSERT,
    "home":pygame.K_HOME,
    "end":pygame.K_END,
    "page up":pygame.K_PAGEUP,
    "page down":pygame.K_PAGEDOWN,
    "F1":pygame.K_F1,
    "F2":pygame.K_F2,
    "F3":pygame.K_F3,
    "F4":pygame.K_F4,
    "F5":pygame.K_F5,
    "F6":pygame.K_F6,
    "F7":pygame.K_F7,
    "F8":pygame.K_F8,
    "F9":pygame.K_F9,
    "F10":pygame.K_F10,
    "F11":pygame.K_F11,
    "F12":pygame.K_F12,
    "F13":pygame.K_F13,
    "F14":pygame.K_F14,
    "F15":pygame.K_F15,
    "numlock":pygame.K_NUMLOCK,
    "caps lock":pygame.K_CAPSLOCK,
    "scroll lock":pygame.K_SCROLLOCK,
    "right shift":pygame.K_RSHIFT,
    "left shift":pygame.K_LSHIFT,
    "right control":pygame.K_RCTRL,
    "left control":pygame.K_LCTRL,
    "right alt":pygame.K_RALT,
    "left alt":pygame.K_LALT,
    "right meta":pygame.K_RMETA,
    "left meta":pygame.K_LMETA,
    "left Windows key":pygame.K_LSUPER,
    "right Windows key":pygame.K_RSUPER,
    "mode shift":pygame.K_MODE,
    "help":pygame.K_HELP,
    "print screen":pygame.K_PRINT,
    "sysrq":pygame.K_SYSREQ,
    "break":pygame.K_BREAK,
    "menu":pygame.K_MENU,
    "power":pygame.K_POWER,
    "Euro":pygame.K_EURO}

#th={v: k for k, v in tc.items()}

#print(th)

def crea_control_game():
    d={}
    di={}
    fin=open("Controls/controls_game.txt","r")
    for line in fin:
        line=line.strip()
        accio,gtecles=line.split(": ")
        if accio=="dreta":
            d["dreta"]=[]
            di["dreta"]=[]
            tecles=gtecles.split(",")
            for tecla in tecles:
                d["dreta"].append(tc[tecla])
                di["dreta"].append(tecla)
        elif accio=="esquerra":
            d["esquerra"]=[]
            di["esquerra"]=[]
            tecles=gtecles.split(",")
            for tecla in tecles:
                d["esquerra"].append(tc[tecla])
                di["esquerra"].append(tecla)
        elif accio=="ajup":
            d["ajup"]=[]
            di["ajup"]=[]
            tecles=gtecles.split(",")
            for tecla in tecles:
                d["ajup"].append(tc[tecla])
                di["ajup"].append(tecla)
        elif accio=="ataca":
            d["ataca"]=[]
            di["ataca"]=[]
            tecles=gtecles.split(",")
            for tecla in tecles:
                d["ataca"].append(tc[tecla])
                di["ataca"].append(tecla)
        elif accio=="salta":
            d["salta"]=[]
            di["salta"]=[]
            tecles=gtecles.split(",")
            for tecla in tecles:
                d["salta"].append(tc[tecla])
                di["salta"].append(tecla)
        elif accio=="avanç":
            d["avanç"]=[]
            di["avanç"]=[]
            tecles=gtecles.split(",")
            for tecla in tecles:
                d["avanç"].append(tc[tecla])
                di["avanç"].append(tecla)
        elif accio=="retro":
            d["retro"]=[]
            di["retro"]=[]
            tecles=gtecles.split(",")
            for tecla in tecles:
                d["retro"].append(tc[tecla])
                di["retro"].append(tecla)
    fin.close()
    return d,di

def crea_control_menu():
    d={}
    di={}
    fin=open("Controls/controls_menus.txt","r")
    for line in fin:
        line=line.strip()
        accio,gtecles=line.split(": ")
        if accio=="intro":
            d["intro"]=[]
            di["intro"]=[]
            tecles=gtecles.split(",")
            for tecla in tecles:
                d["intro"].append(tc[tecla])
                di["intro"].append(tecla)
        elif accio=="up":
            d["up"]=[]
            di["up"]=[]
            tecles=gtecles.split(",")
            #print(tecles)
            for tecla in tecles:
                d["up"].append(tc[tecla])
                di["up"].append(tecla)
        elif accio=="down":
            d["down"]=[]
            di["down"]=[]
            tecles=gtecles.split(",")
            for tecla in tecles:
                d["down"].append(tc[tecla])
                di["down"].append(tecla)
        elif accio=="right":
            d["right"]=[]
            di["right"]=[]
            tecles=gtecles.split(",")
            for tecla in tecles:
                d["right"].append(tc[tecla])
                di["right"].append(tecla)
        elif accio=="left":
            d["left"]=[]
            di["left"]=[]
            tecles=gtecles.split(",")
            for tecla in tecles:
                d["left"].append(tc[tecla])
                di["left"].append(tecla)
    fin.close()
    return d,di

c_game,edit_game=crea_control_game()

c_menu,edit_menu=crea_control_menu()

path="Controls/"

def edita():
    #print_file(path+"controls_game.txt")
    #print(c_game,edit_game,sep=" /  /  /  / ")
    c_game,edit_game=crea_control_game()
    c_menu,edit_menu=crea_control_menu()
    #print(c_game,edit_game,sep=" /  /  /  / ")
    return c_game,edit_game,c_menu,edit_menu

def print_file(fname):
    fin=open(fname,"r")
    print(fin.read())
    fin.close()

def contr():
    print(edit_game)
