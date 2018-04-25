import os, sys, glob, time, linecache, urllib, ctypes, ast
from shutil import copy2 as cpy
from msvcrt import getch
from decimal import Decimal as decimal

if not os.path.isdir("temp"):
    os.mkdir("temp")
title = ctypes.windll.kernel32.SetConsoleTitleA
title("PTR2Modder")

urllib.urlretrieve("https://mgrich.github.io/storage/ptr2modder/versionb.txt", "temp/version.txt")
v = open("temp/version.txt").read()
v = float(v[:-1])
if not os.path.isdir("config"):
    print("Welcome to PTR2Modder.\nThis is a program specifically made for making and using PTR2 mods.\nSpecial thanks to the PTR2 Modding Discord for motivating me to do this.")
    print("")
    print("We will start by creating basic configuration files.")
    os.mkdir("mods")
    os.mkdir("config")
    os.chdir("config")
    os.mkdir("mds")
    con1 = open("basic.conf", 'w+')
    os.mkdir("ibrn")
    while not os.path.isfile("ibrn/imgburn.exe"):
        print("Please put your IMGBurn exe (all lowercase) in ibrn (in config).")
        os.system("pause >nul")
    os.chdir("..")
    os.mkdir("ogiso")
    while not os.path.isfile("ogiso/SYSTEM.CNF"):
        print("Please place your unedited ISO in ogiso (at root of ptr2modder).")
        os.system("pause >nul")
    sys = linecache.getline("ogiso/SYSTEM.CNF", 3)
    sys = sys[-4:-1]
    if sys == "TSC":
        sys = "NTSC"
    con1.write(sys + "\n")
    os.mkdir("miso")
    print("Copying into miso..")
    os.system("xcopy /s /q ogiso miso")
    h = str(raw_input("Do you plan using this in (b)asic mode or (c)reation mode? (B OR C)> "))
    h = str(h) + "\n"
    con1.write(h)
    if h == h.lower():
        print("Downloading tools..")
        urllib.urlretrieve("https://mgrich.github.io/storage/tools.zip", "temp/tools.zip")
        os.chdir("temp")
        print("Extracting..")
        from zipfile import ZipFile as zipfile
        zipfile('tools.zip').extractall()
        os.remove('tools.zip')
        os.chdir("..")
        print("Moving..")
        os.mkdir("tools")
        os.system("xcopy /s /q temp tools")
        os.system("rmdir /Q /S temp")
        os.chdir("config")
        con2 = open("create.conf", 'w+')
        print("Done with tools.\nChanging to basic mode will not get rid of the tools.")
        print("")
        os.chdir("..")
        h = str(raw_input("What do you want your WIP folder where WIP mods are stored to be called? (cannot be called mods)> "))
        while h == "mods":
            print("Nice try.")
            h = input("Pick an actual name> ")
        try:
            os.mkdir(h)
        except WindowsError:
            print("That didn't work, going with 'wip'.")
            os.mkdir("wip") 
    print("Congratulations, you're now all set!")
    print("The program will now shut down to load the config correctly.")
    time.sleep(5)
    exit()
else:
    conf = os.getcwd() + "\\config\\basic.conf"
    ibrn = os.getcwd() + "\\config\\ibrn\\imgburn.exe"
    if os.path.isfile("config/create.conf"):
        confc = open("config/create.conf")

print("Downloading news..")
urllib.urlretrieve("https://mgrich.github.io/storage/ptr2modder/news.txt", "temp/news.txt")
while True:
    os.system("cls")
    print("")
    print("PTR2Modder")
    print("Tool by RMGRich")
    print("Icon by Charx")
    print("")
    while True:
        if v > 1.0:
            opt = ["1", "2", "3", "4", "5", "6"]
        else:
            opt = ["1", "2", "3", "4", "5"]
        print("1. Convert ISO mod to usable mod")
        print("2. Apply mod")
        print("3. Unapply mod")
        print("4. Check news")
        print("5. Exit properly")
        if v > 1.0:
            print("6. Install new version")
        ch = getch()
        if not ch in opt:
            print("Invalid answer")
            time.sleep(3)
            os.system("cls")
        else:
            break
    if ch == "1":
        os.chdir("mods")
        h = str(raw_input("What do you want your mod's folder to be called?> "))
        os.mkdir(h)
        os.chdir(h)
        print("Now to setup configuration:")
        m = open("mod.inf", "w+")
        h1 = str(raw_input("Name of mod> "))
        h2 = str(raw_input("Author> "))
        h3 = str(raw_input("Version> "))
        h4 = str(raw_input("Description> "))
        m.write(h1 + "\n" + h2 + "\n" + h3 + "\n" + h4 + "\n")
        print("Please place your modified ISO contents (only the modified files) WITH THEIR CORRECT FOLDERS in the new 'iso' folder.\nMake sure you do it correctly, as if you mess it up, the mod wont work unless you start over.")
        os.mkdir("iso")
        os.system("pause")
        mm = []
        for root, directories, filenames in os.walk('.'):
            for filename in filenames: 
                    h = os.path.join(root,filename)
                    h = h[2:]
                    mm.append(h)
        m.write(str(mm))
        m.write(str(linecache.getline(conf, 1)))
        m.close()
        os.chdir("../../config")
        mm = open("mods.conf", "w+")
        mm.write(h)
        mm.close()
        os.chdir("..")
        print("Done.")
    elif ch == "2": 
        os.chdir("config")
        m = open("mods.conf", "r")
        mds = m.readlines()
        print(mds)
        os.chdir("../mods")
        mds = map(lambda s: s.strip(), mds)
        for x in mds:
            mdl = []
            mdlo = []
            md = linecache.getline(x + "/mod.inf", 1)
            mdlo.append(x)
            mdl.append(md)
        mdl = map(lambda s: s.strip(), mdl)
        while True:
            print('\n'.join(mdl))
            print("")
            m = raw_input("Which mod?> ")
            if not m in mdl:
                print("Mod doesnt exist.")
                os.system("pause")
            else:
                break
        blo = mdl.index(m)
        ate = mdlo[int(blo)]
        os.chdir(ate)
        pips = linecache.getline("mod.inf", 6)
        if not pips == str(linecache.getline(conf, 1)):
            print("This mod is not meant for your region.")
        else:
            os.chdir("iso")
            dc = os.getcwd()
            print(dc)
            os.chdir("../../..")
            print("Applying mod..")
            os.system("xcopy /s /q /y " + dc + " miso")
            print("Done with general modding. Starting with IMGBurn..")
            os.system("move " + ibrn + ".")
            os.system("imgburn.exe /MODE BUILD /SRC miso /DEST PTR2Modded.iso /FILESYSTEM \"ISO9660 + UDF \" /UDFREVISION \"1.02\" /NOIMAGEDETAILS /ROOTFOLDER YES /VOLUMELABEL \"MISO\" /OVERWRITE YES /START /CLOSE")
            os.system("move imgburn.exe config/ibrn")
            print("Done! Exported to PTR2Modded.iso.")
        os.system("pause")
    elif ch == "4":
        print(open("temp/news.txt").read())
        os.system("pause")
    elif ch == "5":
        exit()



