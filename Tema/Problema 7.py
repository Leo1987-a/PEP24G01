#lista taskuri = save delete send

# lista = input('Introduceti lista de taskuri:')
# lista_taskuri = lista.split(',')
# #
#
# for character in lista[::]:
#     if character not in lista_taskuri:
#         lista_taskuri.count(character)
#     else:
#         print(character)
# lista.count()
# print(lista_taskuri)
# print(lista)

lista = input("Introduceti lista de taskuri: ")
lista_taskuri = lista.split(",")
print(lista_taskuri)

no_duplicates = []

for task in lista_taskuri:
    if task not in no_duplicates:
        no_duplicates.append(task)

print(no_duplicates)