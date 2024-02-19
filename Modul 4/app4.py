number_of_participants = int(input("Type the number of the participants:"))
ages = []
for i in range(1, number_of_participants +1):
    try:
        age = int(input('Type the age of the participants'))
    except ValueError:
        age = int(input(f'Invalid format of the participants {i}. Type again'))
    ages.append(age)

def avg(list_of_numbers):
    total =sum(list_of_numbers)
    average_age = total/len(list_of_numbers)
    return average_age
    # total =0
    # for age in list_of_numbers:
    #
    # #     total+=age
    # # average_age= total/len(list_of_numbers)

print(avg(ages))