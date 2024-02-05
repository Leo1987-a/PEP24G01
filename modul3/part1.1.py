'''# if + condition

var1 = int(input("Add number:"))

if var1 == 1:
    print(var1)
else:
    print("Number is not 1")

#trueish
print(bool(''),'Empty string')
print(bool('0'),'0 string')
print(bool(0),'0 int')
print(bool(-1100),'-1100 int')
print(bool(None),'None object')'''

'''var1 = int(input('Add number:'))

if 1 + var1:
    print(var1)
else:
    print("number is not x")  '''

# elif

'''var1 = int(input('Add number:'))

if 1 + var1:
    print('First result', var1)
elif 2 + var1:
    print(f'Second result: {2 + var1}')
else:  # not reached because it run the first 2
    print("Number is not x")'''

#
var1 = int(input('Add number:'))

if var1 > 0:
    print('Positive result', var1)
elif var1 < -10:
    print(f'Negative result: {var1}')
elif var1 <= 10 and var1 >0:
    print('Result is in interval(0-10]')
elif var1 >= -10 and var1 < 0:
    print('Result is in interval[-10-0)')

else:  # not reached because it run the first 2
    print("Number is not x")


#for loop
