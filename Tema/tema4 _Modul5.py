#
from random import randint

numereLotto = []
for i in range(0,6):
    number =randint(1,50)
    while number in numereLotto:
        number = randint(1,50)
    numereLotto.append(number)
numereLotto.sort()

numereUser = []
for i in range (0,6):
    number = int(input('Introduceti 6 numere norocoase: '))
    while (number in numereUser or number < 1 or number > 50):
        print("Acest numar nu este valid")
    numereUser.append(number)


print("Numerele din extragerea de astazi sunt: ")
print(numereLotto)
print("Numerele dumneavoastra sunt: ")
print(numereUser)

counter = 0
for number in numereUser:
    if number in numereLotto:
        counter +=1
        print("Ati castigat 50Lei")
    if number in numereLotto==2:
        print("Ati castigat 50Lei")
    if number in numereLotto ==3:
        print("Ati castigat 50Lei")
    if number in numereLotto == 4:
        print("Ati castigat 500Lei")
    if number in numereLotto == 5:
        print("Ati castigat 500Lei")
    if number in numereLotto == 6:
        print("Ati castigat 1500Lei")
print('Numerele identice sunt '+ str(counter))

