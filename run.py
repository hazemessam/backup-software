from modules.ListParser import listParser
from modules.Backup import backup
from modules.GarbageCollector import garbageCollector
from modules.Access import accessAllowed
from colorama import init, Fore
from time import sleep
import os
import sys


def run(backupList):
    for src, dist in backupList:
        if not os.path.exists(dist):
            os.mkdir(dist)
        backup(src, dist)
        garbageCollector(src, dist)


if not os.path.exists('B:\\'):
    sys.exit()

init()
backupList = listParser()
# backupList = [
#     ('D:/Media/Documents', 'C:/Users/Hazem/OneDrive/Documents')
# ]
print('Start backup?')
start = input('(y or n): ')
if start.lower() == 'y':
    if True: # put accessAllowed() to put password
        print(Fore.GREEN + 'Starting...')
        run(backupList)
        print(Fore.GREEN + 'All done!')
    else:
        print(Fore.RED + 'Access Denied!')
sleep(5)
sys.exit()

