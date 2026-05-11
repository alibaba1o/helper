import os
import sys
import hashlib
c=sys.argv[1]
class file:
    def __init__(self,c,path):
        self.path=os.path.join(c,path)
        self.size=os.path.getsize(self.path)
        self.direct = os.path.splitext(self.path)
        self.namefile = os.path.basename(self.path)
        self.number=0
        with open(self.path,'rb') as f:
            self.hash=hashlib.sha256(f.read()).hexdigest()
    def destroy(self):
        #print(self.path)
        os.remove(self.path)

def find_dubl(ddc,d):
    if len(d)>=1:
        wwd = [ddc]
        d.remove(ddc)
    else:
        return 0
    b=d.copy()
    for cop in b:
        #print(f"сравниваю {wwd[0].namefile} ({wwd[0].hash[:8]}) с {cop.namefile} ({cop.hash[:8]})")
        if wwd[0].size == cop.size:
            if wwd[0].hash == cop.hash:
                wwd.append(cop)
                d.remove(cop)
    if len(wwd)==1:
        return
    number=1
    for x in wwd:
        x.number=number
        print(str(x.number)+')'+x.namefile + ';')
        number+=1
    print(f'Команды:\nСохранить всё-skip,\nУдалить только некоторые копии-delnum;\nУдалить ненужные копии - del\n Введите команду:')
    command = input()
    if command == 'del':
        print('Выберите номер оригинала, остальное всё удалится')
        c=int(input())
        if c==0:
            c=1
        for ddc in wwd:
            if ddc.number != c:
                ddc.destroy()
    elif command == 'delnum':
        print('Введите числа через запятую')
        command = list(map(int,input().split(',')))
        for i in command[::-1]:
            if i!=0:
                try:
                    print(wwd[i].namefile+'- УНИЧТОЖЕН')
                    wwd[i].destroy()
                except:
                    print(f'Копии файла номера {i} не существует!')
    else:
        d=d
    return d
def collect(c,d):
    for dec in os.listdir(c):
        if os.path.isdir(os.path.join(c, dec)):
            d.extend(collect(os.path.join(c, dec),[]))
        else:
            ddc = file(c,dec)
            d.append(ddc)
    #print([f.path for f in d])
    return d
def copycat(c,d):
    d=collect(c, [])
    #print([f.namefile for f in d])
    b = d.copy()
    for ddc in d:
        b = find_dubl(ddc, d)
copycat(c,[])
print("Других файлов больше нет!\n-----------------------------------------------------------\n")
"""recurse = list(map(lambda x: x.namefile, copycat([], d)))
            if len(recurse) > 1:
                print(recurse)
                print(
                    f'Команды:\nСохранить всё-skip,\nСохранить только некоторые копии-safe,номера через запятую;\nУдалить ненужные копии - del\n')
                command = input()
                if command == 'del':
                    for ddc in recurse[1:]:
                        ddc.destroy()
                elif command == 'safe':
                    command = list(map(int, command.split(',')))
                    for i in command:
                        recurse[i - 1].destroy()
                else:
                    continue
def copycat(duble,c):
    for dec in os.listdir(c):
        if not(os.path.isdir(os.path.join(c,dec))):
            ddc = file(os.path.join(c, dec))
            if len(duble) == 0:
                duble.append(ddc)
            else:
                if ddc.size == duble[-1].size:
                    if ddc.hash == duble[-1].hash:
                        duble.append(ddc)
        else:
            copycat(duble, os.path.join(c,dec))
    return duble
"""