import subprocess
import os
import shutil
import time
from pathlib import Path
from os import mkdir

def wile_comand():

    while True:
        print(f"Что вы хотите сделать,{polzak}?:\n 1 - Запусти протокол ВсёБеги \n 2 - Запусти протокол сортировки Загрузки")
        user_choose=input()
        protocol = {'1':'runalll.py','2':'sort_download.py','3':'convert_file.py'}
        try:
            subprocess.Popen(['python',os.path.join(script_path,r'ОчХорошаяПапка',protocol[user_choose])])
        except:
            print("Такой команды нет")

if __name__=='__main__':

    full_path = os.path.join(os.path.expanduser('~'))
    real_path = os.path.realpath(__file__)
    real_path = real_path.replace(r'\ULTIMATIVE.py','')
    script_path = os.path.join(real_path)
    polzak=full_path.split('\\')[-1]
    print(f"Приветствую! Я личный ассистент пользователя {polzak}")
    wile_comand()
