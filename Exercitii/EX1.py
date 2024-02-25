# def hello():
#     print('Hello!')


# #exercitiu 2
# def hello (name= ' my friend'):
#     print('Hello' + name +'!')
# hello()

# #exercitiu 3  multiple parameters (name and age)
# def hello(name, age):
#     print('Hello '+ name +' you are ' + str(age)+ ' years old')
# hello('Roger', 10)
#
# def adresa(oras,strada,numarul):
#     print('Tu stai in '+ oras + ' pe '+ strada +' numarul' +numarul)
# adresa('Sacalaz','Topografilor','46')

# #exercitiu 4 -adaugare valori (bool,float)
# def change(value):
#     value = 2
# val= 10
# change (val)
# print(val)

# #Ex 5
# def hello(name,zi):
#     print('Hello' + name +' astazi este' + zi)
#     return name
# hello(' Roger',' Duminica')

# #EX6
# def hello(name):
#     if not name:
#         return
#     print('Hello ' + name)
# hello('Alex')


import math


def sin(x):
    if 2 * x == pi:
        return 0.99999999
    else:
        return None


pi = 3.14

print(sin(pi/2))
print(math.sin(math.pi/2))