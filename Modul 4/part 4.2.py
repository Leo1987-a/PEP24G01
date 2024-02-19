# dictionare

# dictionar in python este = cheie

my_dict = {'one': 1, 'two': 2, 'True': True}

print(my_dict)
print(type(my_dict))

my_dict = dict(one=1, two=2)
print(my_dict)

# dictionarul cu unu si doi iterat
for element in my_dict:
    print('dict key', element)

for element in my_dict.values():
    print('dict key', element)

for element in my_dict.keys():
    print('dict key', element)

for element in my_dict.items():  # obiectul va fii afisat in paranteze rotunde -Tupple nu va putea fii modificata
    print('dict key', element)

for key,value in my_dict.items():
    print('dict values', key, value)


a,b = (1,2)  # se poate scrie si fara paranteze dar returneaza identic/daca este doar un element vom scrie doar numarul si o virgula

print(a)
print(b)
print(b)
print(a)

#inversarea a 2 variabile intre ele
a,b = 4,5
a,b = b,a
print(a)
print(b)

#extragere cheie
value = my_dict['one']
print(f'returned value is : {value}')
value = my_dict['one'] = '''one'''
print(f'returned value is : {value}')



# test = {[1]: 'test'}
# print(test)
