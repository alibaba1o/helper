import csv
filename=input()
def read_data_from_file(filename):
    character ={}
    with open(filename, "r",encoding="utf-8") as file:
        line=csv.reader(file)
        for row in line:
            key=row[0]
            try:
                character[key] = int(row[1])
            except:
                character[key] = row[1]
    return character
expirance = {
    1:0,
    2:100,
    3:250,
    4:400,
    5:600
}
chara=read_data_from_file(filename)
d=[chara.copy()]
maxhp=int(chara["max_hp"])
maxen=int(chara["max_energy"])
print("Введите help для просмотра команд")
g=0
while True:
    hidden ={"max_hp","max_energy"}
    print("Ваше Текущее Состояние:")
    for key,value in chara.items():
        if key not in hidden:
            print(key, "|", value, "|")
    if g==0:
        print("ВАЖНО! СОВЕТУЮ СДЕЛАТЬ БЭКАП ВАШЕГО ПЕРСОНАЖА. ТАК КАК ПРОГРАММА БУДЕТ ВНОСИТЬ ВСЕ ВАШИ ИЗМЕНЕНИЯ\n. Вы были проинформированны. Спасибо\n Для продолжения напечатайте чо хотите")
        gdekakashki=input()
    print("\nИ что же делает ваш " + chara["character"] + '?')
    s = input().split()
    if s[0]=='help':
        print("\nСписок комнад, которыми вы хотели воспользоваться для изменения характеристик:")
        print(" heal x - восстановить здоровье персонажу\n healup x - увеличить максимальное количетсво здоровья у персонажа\n damage x - нанести урон персонажу\n enregy x - потратить энергию на действие у персонажа/восстановить энергию\n energyup x- повысить максимальное количество энергии у персонажа\n expup x - повысить очки уровня у персонажа\n lvlup - повысить уровень персонажу на 1 \n undo x - откатить действие(указать количество шагов, если есть таковые)\n bag- действия с рюкзачком|НЕ РАБОТАЕТ|\nПример использование команд: damage 999")
        print("И что же вы выберите?))")
        s=input().split()
    if len(s)==1:
        s.append(0)
    if s[0] == "heal":
        try:
            s[1] = int(s[1])
        except:
            s[1] = 0
        chara["hp"]+=s[1]
        if chara["hp"]>=maxhp:
            chara["hp"]=maxhp
        d.append(chara.copy())
    elif s[0] == "healup":
        try:
            s[1] = int(s[1])
        except:
            s[1] = 0
        chara["max_hp"]=s[1]
        maxhp = chara["max_hp"]
        d.append(chara.copy())
    elif s[0] == "damage":
        try:
            s[1] = int(s[1])
        except:
            s[1] = 0
        chara["hp"] -= s[1]
        if chara["hp"]>=maxhp:
            chara["hp"]=maxhp
        if chara["hp"]<=0:
            chara["hp"]=0
        if chara["hp"] == 0:
            print("Мои соболезнования, ваш персонаж откис ;p")
        d.append(chara.copy())
    elif s[0] == "enregy":
        try:
            s[1] = int(s[1])
        except:
            s[1] = 0
        print("В этом ходу вы совершали какие либо действия? Нет/Любое другое слово")
        u=input()
        if u=='Нет':
            chara["energy"]+=3+5
        else:
            chara["energy"]-=s[1]+3
        if chara["energy"]>=maxen:
            chara["energy"]=maxen
        if chara["energy"]<=0:
            chara["energy"]=0
        d.append(chara.copy())
    elif s[0] == "energyup":
        try:
            s[1] = int(s[1])
        except:
            s[1] = 0
        maxen = s[1]
        chara["max_energy"]=maxen
        d.append(chara.copy())
    elif s[0] == "expup": #
        try:
            s[1] = int(s[1])
        except:
            s[1] = 0
        chara["exp"] += s[1]
        d.append(chara.copy())
    elif s[0] == "lvlup":
        if expirance[chara["level"]+1]<=chara["exp"]:
            chara["level"]+=1
        else:
            print("У вас недостаточно опыта! Поднакопите ещё...\n",expirance[1+chara["level"]]-chara["exp"])
        d.append(chara.copy())
    elif s[0] == "undo":
        try:
            s[1] = int(s[1])
            if s[1]==0: s[1]=1
        except:
            s[1] = 1
        while s[1] != 0 and len(d) > 1:
            d.pop()
            s[1] -= 1
        chara = d[-1]
    elif s[0] == 'help':
        continue
    else:
        print("Такой команды нет")
    sev=d[-1].copy()
    with open(filename,'w',newline='',encoding='utf-8') as f:
        writer=csv.writer(f)
        for key, value in chara.items():
            writer.writerow([key,value])
    g=1
    p = input("Нажмите любую кнопку для продолжения")
    print("----------------------------------------------------------------------")

