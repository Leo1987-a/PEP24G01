#string format

#method format

my_string = "text {}"
print(my_string.format('''exemple'''))
my_string = "text {}"
print(my_string.format(2))
my_str = "text {1} {0}"
print(my_str.format("example1", "exemple2"))
my_str = "text {ex1} {ex2}"
print(my_str.format(ex1="masina",ex2="tigaie"))

#formated string
ex1 = 'Python'
ex2 = 'Learning'
ex3 = "on sesion3"
print(f"text2 {ex1}")
print(f"text2 {ex1} {ex2} \n {ex1}")
print(f"text2 {ex1} \n \t {ex2} \n \t {ex1}")
print(f"text2 {ex1} {ex2} {ex3}")