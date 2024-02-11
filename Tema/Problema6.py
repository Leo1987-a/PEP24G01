# Introduceti un cuvant (fara majuscule): rabdare
# r apare de 2 ori.


# def find_duplicates(string):
#     duplicates=[]
#     for letter in string:
#         if string.coun(letter)>1 and letter not in duplicates:
#             duplicates.append(letter)
#     return duplicates
# string = input('Introduceti cuvantul: ')
# duplicates = find_duplicates(string)
# print(duplicates)


#Problema 6
# cuvant = input("Introduceti textul ")
# duplicate_char=[]
# for character in cuvant:
#     if cuvant.count(character)>1:
#         if character not in duplicate_char:
#             duplicate_char.append(character)
# print(*duplicate_char)



#problema 7

lista = input('Introduceti lista de taskuri:')
lista_taskuri = lista.split(',')
print(lista_taskuri)
lista_taskuri=[]
for character in lista_taskuri:
    if character not in lista_taskuri:
        lista_taskuri.append(character)
    else:
        lista_taskuri.remove(character)
        print(character, 'este duplicat')
lista_taskuri.sort()
print(lista)
print(lista_taskuri)

#         if character not in duplicate_char:
#         duplicate_char.append(character)
# print(*duplicate_char)
# new_list = []
# for number in duplicated[::]:
#     if number not in new_list:
#         new_list.append(number)
#     else:
#         duplicated.remove(number)
#         print(number, ' is duplicate')
# duplicated.sort()
# print(new_list)
# print(duplicated)