# Remove files and folders that doesn't esist in the src folder
import os
import shutil


def garbageCollector(srcDir, distDir):
    srcList = os.listdir(srcDir)
    distList = os.listdir(distDir)
    for f in distList:
        srcPath = os.path.join(srcDir, f)   
        distPath = os.path.join(distDir, f)
        if f not in srcList:
            if os.path.isdir(distPath):
                shutil.rmtree(distPath)
            elif os.path.isfile(distPath):
                os.remove(distPath)
        elif os.path.isdir(distPath):
            garbageCollector(srcPath, distPath)
