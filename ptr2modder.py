import os, sys, glob, time, linecache, urllib
from zipfile import ZipFile as zipfile
from shutil import copy2 as cpy

if not os.path.isdir("config"):
    print("Welcome to PTR2Modder.\nThis is a program specifically made for making and using PTR2 mods.\nSpecial thanks to the PTR2 Modding Discord for motivating me to do this.")
    print("")
    print("We will start by creating basic configuration files.")
    os.mkdir("mods")
    os.mkdir("config")
    os.chdir("config")
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
        os.mkdir("temp")
        urllib.urlretrieve("https://mgrich.github.io/storage/tools.zip", "temp/tools.zip")
        os.chdir("temp")
        print("Extracting..")
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
