# def add_(x,y):
#     print(locals())
#     return x +y #sub return nu se va mai executa nici o functie
#
# #result = add_(5,7)
# #print(result)
# print(add_(5,7))
#
# #print(x) # not in the function

#APP 3 FACTORIAL
#LOCAL VARIABLE
# def factorial(x):
#     result = 1
#     for i in range(1, x+1):
#         result *= i
#     return result
#
# result = factorial(4)
# print(result)



#GLOBAL VARIABLE
# result = 1
#
# def factorial(x):
#     global result
#     for i in range(1, x + 1):
#         result *= i
#
#
# factorial(4)
# print(result)


# #SUMA LUI GAUSS
# result = 0
# def gauss(x):
#     global result # result= 0
#     for i in range(1, x+1):
#         result += i
#
# gauss(100)
# print(result)
# print((100*(100+1))/2)

#SUMA NUMERELOR 1/1 PANA LA 1/N
# result = 0
# def gauss(x):
#     global result # result= 0
#     for i in range(1, x+1):
#         result += i
#
# gauss(100)
# print(result)
# print((100*(100+1))/2)

def sumafractii(x):
    suma = 0
    for i in range(1, x+1):
        suma += 1/i
    return suma

x = int(input())
print(sumafractii(x))