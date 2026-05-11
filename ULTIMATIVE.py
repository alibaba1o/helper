import subprocess
import os
import shutil
import time
from pathlib import Path
from os import mkdir
dn = 'Users'
full_path = os.path.join(os.path.expanduser('~'))
script_path = os.path.join(full_path, 'Desktop','Helper','ОчХорошаяПапка')
polzak=full_path.split('\\')[-1]
#Ещё Надо Реализовать папку для конвертации объектов. Пока идей нет
print(f"Приветствую! Я личный ассистент пользователя {polzak}")
while True:
    print(f"Что вы хотите сделать,{polzak}?:\n 1) Запустит ВсёБеги \n 2)Запустить сортировку Загрузки\n 3) Выискивание повторяющихся файлов в папке")
    g=input()
    if g=='1':
        subprocess.run(['python',os.path.join(script_path,'runalll.py')])
        с=input()
    elif g=='2':
        subprocess.run(['python',os.path.join(script_path,'hihihaha.py')])
        c=input()
    elif g=='3':
        print('Укажите пожалуйста путь папки')
        c=input()
        subprocess.run(['python',os.path.join(script_path,'CopyThatCopycat.py'),c])
