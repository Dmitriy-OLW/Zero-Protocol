import random
vero=int(input("Введите уровень общей спицификации?"))
y=str(random.randint(1,50))
high=""
for i in range(1,vero+1):
    high+=str(i)
if y in high:
    print("Да")
else:
    print("Нет")
