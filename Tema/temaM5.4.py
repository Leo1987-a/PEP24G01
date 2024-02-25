from random import random

from random import randint



lista = []
for x in range(6):
  lista.append(int(input("Introduceti numerele castigatoare{}:".format(x+1))))

print(f'Numelele alese sunt: {lista}')
print()

win_num = []
for x in range(6):
  print(f'Numerele castigatoare sunt: {randint(1,49)}')



num_matches = 0
for number in lista:
    if number in win_num:
        num_matches += 1
print("Ai castigat {} numere".format(num_matches))
print("Numere asemanatoare {} numbers.".format(win_num))