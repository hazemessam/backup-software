import os
from ListParser import listParser
from Backup import backup
from GarbageCollector import garbageCollector


backupList = listParser()

# backupList = [
#     ('D:/Media/Documents', 'C:/Users/Hazem/OneDrive/Documents')
# ]

for src, dist in backupList:
    if not os.path.exists(dist):
        os.mkdir(dist)
    backup(src, dist)
    garbageCollector(src, dist)
