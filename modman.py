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
#HERE WE GOOOOOOOO
while True:
    if n:
        break
    x = 0
    os.system("cls")
    while True:
        dir = os.listdir(".")
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
            dir[x] = ob
        except IndexError:
            pass
        for z in dir:
            print(z + "\n")
        opc = ord(getch())
        if opc == 224:
            x = int(x)
            opd = ord(getch())
            if opd == 80:    
                x = x + 1
                if x > 1:
                    x = 1
            if opd == 72:
                x = x - 1
                if x < len(dir):
                    x = len(dir)
        elif opc == 27:
            n = True
        x = str(x)
        break
