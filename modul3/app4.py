duplicated = [1,3,5,7,7,7,7,7,9,3]    # remove duplicated numbers from the list

new_list= []
for number in duplicated:
    if number not in new_list:
        new_list.append(number)
    else:
        duplicated.remove(number)
        print(number, ' is duplicate')

print(new_list)
print(duplicated)
