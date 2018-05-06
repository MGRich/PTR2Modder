import os, sys
from msvcrt import getch
try:
    m = sys.argv[1]
    fl = sys.argv[2]
except IndexError:
    m = raw_input("You seem to have opened this in standalone.\nWhat mod do you want to edit?> ")
    fl = raw_input("What is your WIP mod folder's name?> ")
tls = os.getcwd() + "\\tools"
while True:
    try:
        if not os.path.isdir(fl + "/" + m + "/iso"):
            os.mkdir(fl + "/" + m + "/iso")
        os.chdir(fl + "/" + m + "/iso")
    except WindowsError:
        m = raw_input("That didn't work, try again.\n\nWhat is your mod's name?> ")
        fl = raw_input("What is your WIP mod folder's name?> ")
    else:
        break

n = False
x = 0
#HERE WE GOOOOOOOO
while True:
    if n:
        break
    os.system("cls")
    while True:
        odir = os.listdir(".")
        dir = odir
        for y, z in enumerate(dir):
            dir[y] = " " + z
        try:
            ob = list(dir[x])
        except IndexError:
            dir = [" "]
            dir[0] = " Nothing to show."
            ob = list(dir[x])
        ob[0] = ">"
        ob = "".join(ob)
        try:
            for y, z in enumerate(dir):
                if y == x:
                    dir[x] = ob
                else:
                    dir[x] = odir[x]     
        except IndexError:
            pass
        for z in dir:
            print(z)
        print("-------")
        #print available options
        #while True: #to sort for eas y
        #    pass
        opc = ord(getch())
        if opc == 224:
            opd = ord(getch())
            if opd == 80:    
                x = x + 1
                if x > len(dir) - 1:
                    x = len(dir) - 1
            if opd == 72:
                x = x - 1
                if x < 0:
                    x = 0
        elif opc == 27:
            n = True
        break
