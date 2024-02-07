list = ["Masa", 5, "Scaun", 4.5, [5, 6, 7], 8]
for obj in list:
    print(f'Tipul obiectului {obj} este {type(obj)} ')
    if type(obj) == list:  # verificare daca un obiect este o lista
        for inner_obj in obj:
            print(f'Tipul obiectului {inner_obj} este {type(obj)}')
