import os
import shutil
from colorama import init, Fore
from filecmp import cmp

def inExceptions(f):
    exceptions = ['.mp4', '.mp3', '.png', '.jpg', '.ico']
    for excp in exceptions:
        if f.endswith(excp):
            return True
    return False

init()
def backup(srcDir, distDir):
    srcList = os.listdir(srcDir)
    for f in srcList:
        if f.lower().endswith('.ini'): continue
        srcPath = os.path.join(srcDir, f)
        distPath = os.path.join(distDir, f)
        if os.path.isfile(srcPath):
            if os.path.exists(distPath):
                if inExceptions(srcPath) or cmp(srcPath, distPath):
                    continue
                os.chmod(distPath, 0o777)
                os.remove(distPath)
            shutil.copy(srcPath, distPath)
            print(Fore.GREEN, f'{srcPath} was copied')
        elif os.path.isdir(srcPath):
            if not os.path.exists(distPath):
                os.mkdir(distPath)
            backup(srcPath, distPath)
