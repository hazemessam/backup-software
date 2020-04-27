# Remove files and folders that doesn't esist in the src folder
import os
import shutil
from colorama import init, Fore


def rmdir(dirPath):
    for f in os.listdir(dirPath):
        fPath = os.path.join(dirPath, f)
        if os.path.isfile(fPath):
            os.chmod(fPath, 0o777)
            os.remove(fPath)
        else:
            rmdir(fPath)
    os.rmdir(dirPath)

def garbageCollector(srcDir, distDir):
    srcList = os.listdir(srcDir)
    distList = os.listdir(distDir)
    for f in distList:
        srcPath = os.path.join(srcDir, f)   
        distPath = os.path.join(distDir, f)
        if f not in srcList:
            if os.path.isdir(distPath):
                rmdir(distPath)
            elif os.path.isfile(distPath):
                os.chmod(distPath, 0o777)
                os.remove(distPath)
            print(Fore.RED, f'{distPath} was deleted')
        elif os.path.isdir(distPath):
            garbageCollector(srcPath, distPath)
