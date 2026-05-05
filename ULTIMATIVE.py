import subprocess
import os
import shutil
import time
from pathlib import Path
from os import mkdir
dn = 'Users'
full_path = os.path.join(os.path.expanduser('~'))
script_path = os.path.join(full_path, 'Desktop','ОчХорошаяПапка')
polzak=full_path.split('\\')[-1]
#Ещё Надо Реализовать папку для конвертации объектов. Пока идей не
print(f"Приветствую! Я личный ассистент пользователя {polzak}")
while True:
    print(f"Что вы хотите сделать,{polzak}?:\n 1) Запустит ВсёБеги \n 2)Запустить сортировку Загрузки")
    g=input()
    if g=='1':
        subprocess.Popen(['python',os.path.join(script_path,'runalll.py')])
    elif g=='2':
        subprocess.Popen(['python',os.path.join(script_path,'hihihaha.py')])

