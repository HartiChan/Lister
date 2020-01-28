import subprocess
import sys

def install(package):
    subprocess.call([sys.executable, "-m", "pip", "install", package])

reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
installed_packages = [r.decode().split('==')[0] for r in reqs.split()]

#print(installed_packages)
if 'progress' in installed_packages:
    print('Requirement satisfied...')
    pass
else:
    install('progress')
    pass

if 'colorama' in installed_packages:
    print('Requirement satisfied...')
else:
    install('colorama')
    pass

import getpass
from os import walk
import progressbar
import time
import logging
from colorama import init
import os
#import lolcat
init(autoreset=True)   #set to True
from colorama import Fore, Back, Style


password = getpass.getpass('Insert your password: ')

while password != 'waifu':
   print('... Sorry.. Wrong pass')
   password = getpass.getpass('Insert your password again: ')


from progress.bar import ShadyBar
bar = ShadyBar('Loading...', max=2)
for i in range(1):
    time.sleep(1)
    bar.next()
    print(Fore.RED + "Fetching data from database...")
    time.sleep(1)
    bar.next()
    print(Fore.BLUE + "Start Lister 1.0")
bar.finish()

print()

from progress.bar import ShadyBar
bar = ShadyBar('Processing ', max=1)
for i in range(1):
    print()
    print( " ___________________________.")
    time.sleep(0.1)
    print("|;;|                     |;;||")
    time.sleep(0.1)
    print("|[]|---------------------|[]||")
    time.sleep(0.1)
    print("|;;|                     |;;||")
    time.sleep(0.1)
    print("|;;|                     |;;||")
    time.sleep(0.1)
    print("|;;|                     |;;||")
    time.sleep(0.1)
    print("|;;|                     |;;||")
    time.sleep(0.1)
    print("|;;|                     |;;||")
    time.sleep(0.1)
    print("|;;|_____________________|;;||")
    time.sleep(0.1)
    print("|;;;;;;;;;;;;;;;;;;;;;;;;;;;||")
    time.sleep(0.1)
    print("|;;;;;;_______________ ;;;;;||")
    time.sleep(0.1)
    print("|;;;;;|  ___          |;;;;;||")
    time.sleep(0.1)
    print("|;;;;;| |;;;|         |;;;;;||")
    time.sleep(0.1)
    print("|;;;;;| |;;;|         |;;;;;||")
    time.sleep(0.1)
    print("|;;;;;| |;;;|         |;;;;;||")
    time.sleep(0.1)
    print("|;;;;;| |___|         |;;;;;||")
    time.sleep(0.1)
    print("\_____|_______________|_____||")
    time.sleep(0.1)
    print(" ~~~~~^^^^^^^^^^^^^^^^^~~~~~~")
    bar.next()
bar.finish()


run=1
while run != 0:
    print(Fore.RED + "WARNING: remove last \ in path")
    
    path = input("Path: ")

    

    print(Fore.BLUE + "run Lister 1.0")
    
    time.sleep(0.2)
    bar = ShadyBar(Fore.BLUE + 'Load Path...  ', max=100)
    s=0
    while s != 100:
        time.sleep(0.01)
        bar.next()
        s=s+1
    bar.finish()
    
    time.sleep(0.2)
    
    print(Fore.RED + "Current Path [" + path +"]")
    
    time.sleep(0.2)

    from progress.spinner import Spinner

    spinner = Spinner(Fore.RED + 'Loading list all Files... ')
    s=0
    while s != 20:
        time.sleep(0.1)
        spinner.next()
        s=s+1
    spinner.finish()

    

    for i in range(1):
        dirp = []
        dirn = []

        f = []
        for (dirpath, dirnames, filenames) in walk(path):

            dirp.extend(dirpath)
            dirn.extend(dirnames)
            f.extend(filenames)

            #print(dirp)

            
            print(Fore.RED + "List of all Directorys")
            
            time.sleep(1)
            print(dirn)
            print()
            

            time.sleep(1)
            print(Fore.RED + "List of all Files")
            
            time.sleep(1)
            print(f)
            print()
            break
    


    folders = []

    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for folder in d:
            folders.append(os.path.join(r, folder))

    for f in folders:
        print(f)
    
    print()


    files = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            files.append(os.path.join(r, file))

    for f in files:
        print(f)


    



    restart=""
    restart=input("restart? y/n...  ")
    while restart != "y" and restart != "n":
       print('Wrong letter')
       restart=""
       restart=input("restart? y/n...  ")
    
    if restart != "y":
        run=0
        pass

    pass
print(Fore.BLUE + "shut down Lister 1.0")
input('Press any Button to close... ')
