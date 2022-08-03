import os
import shutil
from turtle import back
path = 'd:/null/cstest'
files = os.listdir(path)
backupdir = path+'Backup'
if os.path.exists(backupdir):
    shutil.rmtree(backupdir)
shutil.copytree(path, backupdir)
for f in files:
    folder_name = path + '/' + f.split('.')[-1]
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        shutil.move(path + '/' + f, folder_name)

    else:
        shutil.move(path + '/' + f, folder_name)
