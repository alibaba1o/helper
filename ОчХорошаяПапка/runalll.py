import os
import subprocess
real_path = os.path.realpath(__file__)
real_path = real_path.replace('runalll.py', '')

folder = real_path + r'ПапкаДляПротоколаВсеБеги'
os.chdir(folder)
print('Приятного пользования, менеджер!')
subprocess.Popen(r"AmneziaVPN.lnk",shell=True)
subprocess.Popen(r"TgWsProxy_windows.exe")
os.chdir(folder+r'\zapret-discord-youtube')
subprocess.Popen(r"general (FAKE TLS AUTO33).bat",shell=True)
os.chdir('..')
subprocess.Popen(r"C:\Users\kirya\AppData\Roaming\Telegram Desktop\Telegram.exe")

