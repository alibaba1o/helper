import os
import shutil
import time
from pathlib import Path
from os import mkdir

dn = 'Downloads'
full_path = os.path.join(os.path.expanduser('~'), dn)
os.chdir(full_path)
be=os.listdir()
dat ={
    'Jan':'01',
    'Feb':'02',
    'Mar':'03',
    'Apr':'04',
    'May':'05',
    'Jun':'06',
    'Jul':'07',
    'Aug':'08',
    'Sep':'09',
    'Oct':'10',
    'Nov':'11',
    'Dec':'12'
}

doks=['CSV','DOCX','PDF','XLS','XLSX','PPT','ODT']
pt =['PSP','PNG','WEBM','MP4','JPG','GIF','JPEG']
k=0
for i in be:
    if os.path.isfile(i):
        d=i.split('.')[-1]
        if not os.path.exists(d.upper()):
            os.mkdir(d.upper())
        shutil.move(i, d.upper())
        print(f"Файл {i} перемещён в {d.upper()}")
        k+=1
if k==0:
    print("Нечего перемещать!")
print("Нажмите любую кнопку для продолжения + Enter")
ble=input()
he=0
"""
def dig(path,downloads):
    for j in os.listdir(path):
        full = os.path.join(path, j)
        if os.path.isfile(full):
            shutil.move(full, os.path.join(downloads, j))
        else:
            dig(full,downloads)
for i in be:
    path = full_path + '/' + i
    dig(path,full_path)
"""


'''
^
|        
ОБЕЗБОЛ НА ОДНУ ГЛУБИНУ
    
УЖАСНО ВОНЯЕТ
|
v
    for j in os.listdir():
        mtime = os.path.getmtime(j)
        mtime = str(time.ctime(mtime)).split(' ')
        ntime = str(mtime[2])+'.'+str(dat[mtime[1]])+'.'+str(mtime[-1])
        if ntime not in os.listdir():
            os.mkdir(ntime)
        shutil.move(j, ntime)
'''