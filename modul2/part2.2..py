#string format

#method format

'''my_string = "text {}"
print(my_string.format(''exemple''))
my_string = "text {}"
print(my_string.format(2))
my_str = "text {1} {0}"
print(my_str.format("example1", "exemple2"))
my_str = "text {ex1} {ex2}"
print(my_str.format(ex1="masina",ex2="tigaie"))'''

#formated string
ex1 = 'Python'
ex2 = 'Learning'
ex3 = "on sesion3"
print(f"text2 {ex1}")
print(f"text2 {ex1} {ex2} \n {ex1}")
print(f"text2 {ex1} \n \t {ex2} \n \t {ex1}")
print(f"text2 {ex1} {ex2} {ex3}")


# functia len

ex1 = "exemple1"
print(len(ex1))

#index of string

hello = "hello world"
print(hello[3])
print(hello[3:7]) # last index not included
print(hello[0:10:2])
print(hello[0:12:2]) #not all version of python 3
print(hello[::2])  #start from the first to the last index
print(hello[::-1])  # star from the back (in ordine inversa)
print(hello[-5:-1:])
