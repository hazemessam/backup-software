import os
import shutil


def backup(srcDir, distDir):
    srcList = os.listdir(srcDir)
    for f in srcList:
        if f.lower().endswith('.ini'):
            continue
        srcPath = os.path.join(srcDir, f)
        distPath = os.path.join(distDir, f)
        if os.path.isfile(srcPath):
            if os.path.exists(distPath):
                os.remove(distPath)
            shutil.copy(srcPath, distPath)
        elif os.path.isdir(srcPath):
            if not os.path.exists(distPath):
                os.mkdir(distPath)
            backup(srcPath, distPath)
