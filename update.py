import urllib, subprocess
from msvcrt import getch
from decimal import Decimal as decimal

v = open("temp/version.txt").read()
v = float(v[:-1])
print("Downloading..")
urllib.urlretrieve("https://github.com/MGRich/ptr2modder/releases/download/" + str(v) + "b" "/ptr2modder.exe ptr2modder.exe")
print("Starting..")
subprocess.Popen("ptr2modder.exe")
exit()