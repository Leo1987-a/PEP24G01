# #prima varianta automat cafea
#
# print('1.Cappuciono ...4lei')
# print('2.Espresso...3.5')
#products ={'1':4,'2':3.5}  # extragere cheie din dictionar
# option = int(input('Ce optiune alegeti? [1,2]:'))
# coin = int(input('Introduceti o bancnota [5,10]):'))
# if option == 1:
#     if coin == 5:
#         rest = 5 - 4
#     elif coin == 10:
#         rest = 10 - 4
# elif option == 2:
#     if coin == 5:
#         rest = 5 - 3.5
#     elif coin == 10:
#         rest = 10 - 3.5
#
# print(f'Veti primii restul de {rest} lei.')

#varianta 2 automat cafea
print('1.Cappuciono ...4lei')
print('2.Espresso...3.5')
products ={'1':4,'2':3.5}  # extragere cheie din dictionar

option = int(input('Ce optiune alegeti? [1,2]:'))
coin = int(input('Introduceti o bancnota [5,10]):'))
if option == 1 and coin==5:
        rest = 5 - 4
elif option == 1 and coin == 10:
        rest = 10 - 4
elif option == 2 and coin == 5:
        rest = 5 - 3.5
elif option == 2 and  coin == 10:
        rest = 10 - 3.5
else:
        print('Invalid products')


print(f'Veti primii restul de {rest} lei.')