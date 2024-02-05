number = int(input("Give number:"))

print(range(number))
print(range(0, number, 2))
print(type(range(number)))

for count in range(0, number + 1, 2):
    print(count)

print(f'Last value: {count}') # can be undefined