# Parse backupList.txt to list of tuples (src, dist)  
def listParser():
    backupList = list()
    file = open('backupList.txt', 'r')
    for line in file:
        line = line.strip()
        item = tuple(line.split(' -> '))
        backupList.append(item)
    return backupList