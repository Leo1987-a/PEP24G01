# for

'''my_str= "Hello World"
my_int= 100
for letter in my_str:
    print(letter)x

#for number in my_int:  # int is not iterable
    #print(number)

for number in range(my_int):
    print(number)


user_input= input("give me a string: ")

for letter in user_input:
    print(letter)
    if letter == "x":
        print("I fount an X")
        break
else:
    print("Could not find X")'''

user_input = input("give me a string: ")  # do not print x

for letter in user_input:
    if letter == 'x':
        continue
    print(letter)
else:
    print("Could not find X to print")
