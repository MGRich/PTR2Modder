import os, sys, shutil, linecache
from msvcrt import getch
try:
    m = sys.argv[1]
    fl = sys.argv[2]
except IndexError:
    m = raw_input("You seem to have opened this in standalone.\nWhat mod do you want to edit?> ")
    fl = raw_input("What is your WIP mod folder's name?> ")
tls = os.getcwd() + "\\tools"
og = os.getcwd() + "\\ogiso"
while True:
    try:
        md = open(fl + "/" + m + "/mod.inf", "r+")
        ro = os.getcwd() + "\\" + fl + "\\" + m + "/iso"
        if not os.path.isdir(fl + "/" + m + "/iso"):
            os.mkdir(fl + "/" + m + "/iso")
        os.chdir(fl + "/" + m + "/iso")
    except WindowsError:
        m = raw_input("That didn't work, try again.\n\nWhat is your mod's name?> ")
        fl = raw_input("What is your WIP mod folder's name?> ")
    else:
        break
mnam = m
ms = raw_input("What is your MINGW64 PTR2Tools directory?\n(i didnt bother to put this in config due to pain)\n(msysinstall)/mingw64/bin (KEEP SLASH AT END)> ")
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
        op = ["g"]
        print("G. Global Options")
        while True: #to sort for eas y
            if os.path.split(os.getcwd())[-1] == "DATA":
                print("I. Extract INT")
                op.append("i")
            if os.path.split(os.getcwd())[-1] == "SND":
                print("C. Convert Music")
                op.append("c")
            if os.path.split(os.getcwd())[-1][:3] == "st0":
                print("P. Re-pack INT")
                op.append("p")
            if os.path.split(os.getcwd())[-1][:3] == "st0" and not os.path.isdir("tex"):
                print("T. Extract Textures")
                op.append("t")
            if os.path.split(os.getcwd())[-1][:3] == "st0" and os.path.isdir("tex"):
                print("R. Inject Textures")
                op.append("r")
            break
        opc = ord(getch())
        if opc == 13:
            if os.path.isdir(dir[x][1:]):
                os.chdir(dir[x][1:])
                x = 0
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
        if chr(opc) in op:
            opc = chr(opc)
            if opc == "g":
                opg = ["c", "r"]
                print("=------=")
                print("C. CD Mode (modifying/changing dir)")
                print("R. Recalculate mod.inf")
                opcg = getch()
                if opcg in opg:
                    if opcg == "c":
                        dch = raw_input("--m to make a dir.\n--d to delete a dir.\nName the dir to travel to the dir.\n> ")
                        try:
                            if dch[:3] == "--m":
                                os.mkdir(dch[4:])
                            elif dch[:3] == "--d":
                                shutil.rmtree(dch[4:])
                            else:
                                os.chdir(dch)
                                if dch == ".." and "iso" in os.listdir("."):
                                    os.chdir("iso")
                                x = 0
                        except:
                            print("There was an error.")
                            os.system("pause")
                    if opcg == "r":
                        cwd = os.getcwd()
                        os.chdir(ro)
                        print os.getcwd()
                        os.system("pause")
                        mm = []
                        for root, directories, filenames in os.walk('.'):
                            for filename in filenames: 
                                    h = os.path.join(root,filename)
                                    h = h[2:]
                                    mm.append(h)
                        lmfao = []
                        dect = str(mm).lower()
                        for u in range(1,9):
                            u = str(u)
                            o = "st0" + u
                            f = "vs0" + u
                            if o in dect:
                                lmfao.append(u)
                            if f in dect:
                                lmfao.append("VS" + u)
                        if 'stbn' in dect:
                            lmfao.append("Bonus")
                        if 'stmenu' in dect:
                            lmfao.append("Stage Menu")
                        if 'title.int' in dect:
                            lmfao.append("Title")
                        charx = []
                        #conditional checks
                        if 'wp2' in dect:
                            charx.append('Music Modding')
                            if 'gm0n' in dect:
                                charx.append("Bad/Awful Editing")
                        if 'int' in dect:
                            charx.append('INT Mod')
                        if 'olm' in dect:
                            charx.append('OLM Editing')
                        if 'xtr' in dect:
                            charx.append('Cutscene Editing')
                        if 'hk0' in dect:
                            charx.append('Boxy Editing')
                        if 'ext' in dect:
                            charx.append('Music Box Editing')
                        if 'scus' in dect:
                            charx.append('ELF Model Editing')
                        mdin = md.readlines()
                        mdin[4] = str(mm) + "\n"
                        mdin[6] = str(lmfao) + "\n" 
                        mdin[7] = str(charx)
                        md.truncate()
                        md.close()
                        md = open("mod.inf", "r+")
                        md.writelines(mdin)
                        md.close()
                        md = open("mod.inf", "r+")
                        os.chdir(cwd)
            if opc == "i":
                dch = raw_input("Name of INT (with .int)> ")
                print("Working..")
                os.system(ms + "ptr2int.exe e "+ og + "\\DATA\\" + dch + " " + dch[:-4] + ">nul")
            if opc == "p":
                print("Working..")
                dch = os.path.split(os.getcwd())[-1] + ".int"
                os.chdir("..")
                os.system(ms + "ptr2int.exe c "+ dch + " " + dch[:-4] + ">nul")            
                os.chdir(dch[:-4])
            elif opc == "t":
                dch = raw_input("Name of Model (with .spm)> ")
                os.chdir("PROPS")
                os.system(ms + "ptr2spm.exe gtex0 "+ dch + " temp" + ">nul")
                shutil.move("temp", "../temp")
                os.chdir("..")
                os.mkdir("tex")
                os.system(ms + "ptr2tex.exe e TEXTURES temp tex" + ">nul")
            elif opc == "r":
                os.system(ms + "ptr2tex.exe i TEXTURES temp tex" + ">nul")
        elif opc == 27:
            n = True
        break
