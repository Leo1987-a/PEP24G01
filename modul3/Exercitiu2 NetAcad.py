y = input('year')
if y < 1582:
    print('Not within the Gregorian calendar period')
elif not (y % 400):
    print('Leap year')
elif not (y % 100):
    print('Leap year')
elif not (y % 4):
    print('Leap year')
else:
    print('Common year')
