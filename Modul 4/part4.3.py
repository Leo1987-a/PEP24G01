# Exceptiile
try:
    # raise NotImplemented('This is a test')
    # print(result)
    # result = 1 / 0
    # print(result)
    pass
except ZeroDivisionError:  # doar aceasta exceptie va fii tratata
    print('Cannot divided by 0')
except NameError:
    print('Variable result nu exista ')
# except TypeError:
# print('Variabila type nu exista ')
except Exception:# cuprinde toate errorile aflate in except
    print('some unexpected error occured')
else:
    print('Everything was executed successfully')
finally:
    print('This will always get printed')
    
