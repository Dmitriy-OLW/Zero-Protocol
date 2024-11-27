import random
from playsound import playsound










"""Unitology-1team"""
u1_diploma=1
u2_tehnica=0
u3_stroit=0
u4_moderniz=0
u5_isled=0

"""OAK-2team"""
o1_diploma=0
o2_tehnica=1
o3_stroit=0
o4_moderniz=0
o5_isled=0

"""UNSC-3team"""
k1_diploma=0
k2_tehnica=0
k3_stroit=1
k4_moderniz=0
k5_isled=0

"""Terragroup-4team"""
t1_diploma=0
t2_tehnica=0
t3_stroit=0
t4_moderniz=0
t5_isled=1

"""Bucva_Uy-5team"""
b1_diploma=0
b2_tehnica=0
b3_stroit=0
b4_moderniz=1
b5_isled=0




























print("Unitology-1team")
s=[]
for otrez in range(0,u1_diploma+1):
    s.append(otrez)
    s1=str(s)
print("Уровень Демократии: "+s1)

s=[]
for otrez in range(0,u2_tehnica+1):
    s.append(otrez)
    s1=str(s)
print("Уровень Тяж.Техники/Логистика: "+s1)

s=[]
for otrez in range(0,u3_stroit+1):
    s.append(otrez)
    s1 = str(s)
print("Уровень Строительства: " + s1)

s=[]
for otrez in range(0,u4_moderniz+1):
    s.append(otrez)
    s1 = str(s)
print("Уровень Полевой Модернизации: " + s1)

s=[]
for otrez in range(0,u5_isled+1):
    s.append(otrez)
    s1=str(s)
print("Уровень Иследований: "+s1)

print("")
print("OAK-2team")
s=[]
for otrez in range(0,o1_diploma+1):
    s.append(otrez)
    s1=str(s)
print("Уровень Демократии: "+s1)

s=[]
for otrez in range(0,o2_tehnica+1):
    s.append(otrez)
    s1=str(s)
print("Уровень Тяж.Техники/Логистика: "+s1)

s=[]
for otrez in range(0,o3_stroit+1):
    s.append(otrez)
    s1 = str(s)
print("Уровень Строительства: " + s1)

s=[]
for otrez in range(0,o4_moderniz+1):
    s.append(otrez)
    s1 = str(s)
print("Уровень Полевой Модернизации: " + s1)

s=[]
for otrez in range(0,o5_isled+1):
    s.append(otrez)
    s1=str(s)
print("Уровень Иследований: "+s1)


print("")
print("UNSC-3team")
s=[]
for otrez in range(0,k1_diploma+1):
    s.append(otrez)
    s1=str(s)
print("Уровень Демократии: "+s1)

s=[]
for otrez in range(0,k2_tehnica+1):
    s.append(otrez)
    s1=str(s)
print("Уровень Тяж.Техники/Логистика: "+s1)

s=[]
for otrez in range(0,k3_stroit+1):
    s.append(otrez)
    s1 = str(s)
print("Уровень Строительства: " + s1)

s=[]
for otrez in range(0,k4_moderniz+1):
    s.append(otrez)
    s1 = str(s)
print("Уровень Полевой Модернизации: " + s1)

s=[]
for otrez in range(0,k5_isled+1):
    s.append(otrez)
    s1=str(s)
print("Уровень Иследований: "+s1)

print("")
print("Terragroup-4team")
s=[]
for otrez in range(0,t1_diploma+1):
    s.append(otrez)
    s1=str(s)
print("Уровень Демократии: "+s1)

s=[]
for otrez in range(0,t2_tehnica+1):
    s.append(otrez)
    s1=str(s)
print("Уровень Тяж.Техники/Логистика: "+s1)

s=[]
for otrez in range(0,t3_stroit+1):
    s.append(otrez)
    s1 = str(s)
print("Уровень Строительства: " + s1)

s=[]
for otrez in range(0,t4_moderniz+1):
    s.append(otrez)
    s1 = str(s)
print("Уровень Полевой Модернизации: " + s1)

s=[]
for otrez in range(0,t5_isled+1):
    s.append(otrez)
    s1=str(s)
print("Уровень Иследований: "+s1)

print("")
print("Bucva_Uy-5team")
s=[]
for otrez in range(0,b1_diploma+1):
    s.append(otrez)
    s1=str(s)
print("Уровень Демократии: "+s1)

s=[]
for otrez in range(0,b2_tehnica+1):
    s.append(otrez)
    s1=str(s)
print("Уровень Тяж.Техники/Логистика: "+s1)

s=[]
for otrez in range(0,b3_stroit+1):
    s.append(otrez)
    s1 = str(s)
print("Уровень Строительства: " + s1)

s=[]
for otrez in range(0,b4_moderniz+1):
    s.append(otrez)
    s1 = str(s)
print("Уровень Полевой Модернизации: " + s1)

s=[]
for otrez in range(0,b5_isled+1):
    s.append(otrez)
    s1=str(s)
print("Уровень Иследований: "+s1)


print("")
print("")
print("")
who=str(input("ведите какая операция сейчас будет: all - альянс"))





if who == "all":
    name = int(input("Введите номер вашей команды, первая группа альянса"))
    if name == 1:
        al1=(( (u1_diploma) *4)+( (u5_isled) *3)+( (u4_moderniz)  *2)+( (u3_stroit) )+( (u2_tehnica) //2))
    elif name == 2:
        al1=(((o2_tehnica) *4) + ((o3_stroit) *3) + ((o4_moderniz) * 2) + ((o5_isled)) + ((o1_diploma) // 2))
    elif name == 3:
        al1=(((k3_stroit) *4) + ((k2_tehnica) *3) + ((k4_moderniz) * 2) + ((k1_diploma)) + ((k5_isled) // 2))
    elif name == 4:
        al1=((( t5_isled ) *4) + (( t4_moderniz  ) *3) + (( t1_diploma  ) * 2) + (( t3_stroit  )) + (( t2_tehnica   ) // 2))
    elif name == 5:
        al1=(((b4_moderniz) *4) + ((b5_isled) *3) + ((b3_stroit) * 2) + ((b1_diploma)) + ((b2_tehnica) // 2))
    else:
        print("Произошла ошибка определения уровня спецификации.")
        name = int(input("Введите номер вашей команды"))
        if name == 1:
            al1=(((u1_diploma) * 4) + ((u5_isled) * 3) + ((u4_moderniz) * 2) + ((u3_stroit)) + ((u2_tehnica) // 2))
        elif name == 2:
            al1=(((o2_tehnica) * 4) + ((o3_stroit) * 3) + ((o4_moderniz) * 2) + ((o5_isled)) + ((o1_diploma) // 2))
        elif name == 3:
            al1=(((k3_stroit) * 4) + ((k2_tehnica) * 3) + ((k4_moderniz) * 2) + ((k1_diploma)) + ((k5_isled) // 2))
        elif name == 4:
            al1=(((t5_isled) * 4) + ((t4_moderniz) * 3) + ((t1_diploma) * 2) + ((t3_stroit)) + ((t2_tehnica) // 2))
        elif name == 5:
            al1=(((b4_moderniz) * 4) + ((b5_isled) * 3) + ((b3_stroit) * 2) + ((b1_diploma)) + ((b2_tehnica) // 2))
    name = int(input("Введите номер вашей команды, вторая группа альянса"))
    if name == 1:
        al2=(( (u1_diploma) *4)+( (u5_isled) *3)+( (u4_moderniz)  *2)+( (u3_stroit) )+( (u2_tehnica) //2))
    elif name == 2:
        al2=(((o2_tehnica) *4) + ((o3_stroit) *3) + ((o4_moderniz) * 2) + ((o5_isled)) + ((o1_diploma) // 2))
    elif name == 3:
        al2=(((k3_stroit) *4) + ((k2_tehnica) *3) + ((k4_moderniz) * 2) + ((k1_diploma)) + ((k5_isled) // 2))
    elif name == 4:
        al2=((( t5_isled ) *4) + (( t4_moderniz  ) *3) + (( t1_diploma  ) * 2) + (( t3_stroit  )) + (( t2_tehnica   ) // 2))
    elif name == 5:
        al2=(((b4_moderniz) *4) + ((b5_isled) *3) + ((b3_stroit) * 2) + ((b1_diploma)) + ((b2_tehnica) // 2))
    else:
        print("Произошла ошибка определения уровня спецификации.")
        name = int(input("Введите номер вашей команды"))
        if name == 1:
            al2=(((u1_diploma) * 4) + ((u5_isled) * 3) + ((u4_moderniz) * 2) + ((u3_stroit)) + ((u2_tehnica) // 2))
        elif name == 2:
            al2=(((o2_tehnica) * 4) + ((o3_stroit) * 3) + ((o4_moderniz) * 2) + ((o5_isled)) + ((o1_diploma) // 2))
        elif name == 3:
            al2=(((k3_stroit) * 4) + ((k2_tehnica) * 3) + ((k4_moderniz) * 2) + ((k1_diploma)) + ((k5_isled) // 2))
        elif name == 4:
            al2=(((t5_isled) * 4) + ((t4_moderniz) * 3) + ((t1_diploma) * 2) + ((t3_stroit)) + ((t2_tehnica) // 2))
        elif name == 5:
            al2=(((b4_moderniz) * 4) + ((b5_isled) * 3) + ((b3_stroit) * 2) + ((b1_diploma)) + ((b2_tehnica) // 2))
    name = int(input("Введите номер вашей команды, третья группа альянса"))
    if name == 1:
        al3 = (((u1_diploma) * 4) + ((u5_isled) * 3) + ((u4_moderniz) * 2) + ((u3_stroit)) + ((u2_tehnica) // 2))
    elif name == 2:
        al3 = (((o2_tehnica) * 4) + ((o3_stroit) * 3) + ((o4_moderniz) * 2) + ((o5_isled)) + ((o1_diploma) // 2))
    elif name == 3:
        al3 = (((k3_stroit) * 4) + ((k2_tehnica) * 3) + ((k4_moderniz) * 2) + ((k1_diploma)) + ((k5_isled) // 2))
    elif name == 4:
        al3 = (((t5_isled) * 4) + ((t4_moderniz) * 3) + ((t1_diploma) * 2) + ((t3_stroit)) + ((t2_tehnica) // 2))
    elif name == 5:
        al3 = (((b4_moderniz) * 4) + ((b5_isled) * 3) + ((b3_stroit) * 2) + ((b1_diploma)) + ((b2_tehnica) // 2))
    elif name ==0:
        al3=0
    else:
        print("Произошла ошибка определения уровня спецификации.")
        name = int(input("Введите номер вашей команды"))
        if name == 1:
            al3 = (((u1_diploma) * 4) + ((u5_isled) * 3) + ((u4_moderniz) * 2) + ((u3_stroit)) + ((u2_tehnica) // 2))
        elif name == 2:
            al3 = (((o2_tehnica) * 4) + ((o3_stroit) * 3) + ((o4_moderniz) * 2) + ((o5_isled)) + ((o1_diploma) // 2))
        elif name == 3:
            al3 = (((k3_stroit) * 4) + ((k2_tehnica) * 3) + ((k4_moderniz) * 2) + ((k1_diploma)) + ((k5_isled) // 2))
        elif name == 4:
            al3 = (((t5_isled) * 4) + ((t4_moderniz) * 3) + ((t1_diploma) * 2) + ((t3_stroit)) + ((t2_tehnica) // 2))
        elif name == 5:
            al3 = (((b4_moderniz) * 4) + ((b5_isled) * 3) + ((b3_stroit) * 2) + ((b1_diploma)) + ((b2_tehnica) // 2))
        elif name == 0:
            al3 = 0
    al_l=al1+al2+al3
    print(al_l)

    vero = int(input("Введите уровень общей спицификации"))
    kolll= int(input("Введите количество игроков в альянсе"))
    if kolll == 2:
        y = str(random.randint(1, 210))
        high = ""
        for i in range(1, vero + 1):
            high += str(i)
        if y in high:
            print("Да")
        else:
            print("Нет")
    elif kolll == 3:
        y = str(random.randint(1, 315))
        high = ""
        for i in range(1, vero + 1):
            high += str(i)
        if y in high:
            print("Да")
        else:
            print("Нет")


    with open("all.txt", "a") as f:
        f.write(' 1 ')
        f.close()
    with open("all.txt", "r") as f:
        text = f.read()
        print("Уровень дебафа(количество 1): "+ text)
        f.close()


if who == "end":
    playsound('NextOren.mp3')

w=5
while w>0:
    name=int(input("Введите номер вашей команды"))
    if name == 1:
        print(( (u1_diploma) *4)+( (u5_isled) *3)+( (u4_moderniz)  *2)+( (u3_stroit) )+( (u2_tehnica) //2))
    elif name == 2:
        print(((o2_tehnica) *4) + ((o3_stroit) *3) + ((o4_moderniz) * 2) + ((o5_isled)) + ((o1_diploma) // 2))
    elif name == 3:
        print(((k3_stroit) *4) + ((k2_tehnica) *3) + ((k4_moderniz) * 2) + ((k1_diploma)) + ((k5_isled) // 2))
    elif name == 4:
        print((( t5_isled ) *4) + (( t4_moderniz  ) *3) + (( t1_diploma  ) * 2) + (( t3_stroit  )) + (( t2_tehnica   ) // 2))
    elif name == 5:
        print(((b4_moderniz) *4) + ((b5_isled) *3) + ((b3_stroit) * 2) + ((b1_diploma)) + ((b2_tehnica) // 2))
    else:
        print("Произошла ошибка определения уровня спецификации.")
        name = int(input("Введите номер вашей команды"))
        if name == 1:
            print(((u1_diploma) * 4) + ((u5_isled) * 3) + ((u4_moderniz) * 2) + ((u3_stroit)) + ((u2_tehnica) // 2))
        elif name == 2:
            print(((o2_tehnica) * 4) + ((o3_stroit) * 3) + ((o4_moderniz) * 2) + ((o5_isled)) + ((o1_diploma) // 2))
        elif name == 3:
            print(((k3_stroit) * 4) + ((k2_tehnica) * 3) + ((k4_moderniz) * 2) + ((k1_diploma)) + ((k5_isled) // 2))
        elif name == 4:
            print(((t5_isled) * 4) + ((t4_moderniz) * 3) + ((t1_diploma) * 2) + ((t3_stroit)) + ((t2_tehnica) // 2))
        elif name == 5:
            print(((b4_moderniz) * 4) + ((b5_isled) * 3) + ((b3_stroit) * 2) + ((b1_diploma)) + ((b2_tehnica) // 2))

    vero=int(input("Введите уровень общей спицификации"))
    y=str(random.randint(1,105))
    high=""
    for i in range(1,vero+1):
        high+=str(i)
    if y in high:
        print("Да")
    else:
        print("Нет")
    w=w-1
        




    

"""
#Нулевые значения
#Unitology-1team
u1_diploma=1
u2_tehnica=0
u3_stoit=0
u4_moderniz=0
u5_isled=0

#OAK-2team
o1_diploma=0
o2_tehnica=1
o3_stoit=0
o4_moderniz=0
o5_isled=0

#UNSC-3team
k1_diploma=0
k2_tehnica=0
k3_stoit=1
k4_moderniz=0
k5_isled=0

#Terragroup-4team
t1_diploma=0
t2_tehnica=0
t3_stoit=0
t4_moderniz=0
t5_isled=1

#Bucva_Uy-5team
b1_diploma=0
b2_tehnica=0
b3_stoit=0
b4_moderniz=1
b5_isled=0

"""
























#y=( (x1) **3)+( (x2) **2)+( (x3)  *2)+( (x4) )+( (x5) //2)