class Car:  # definitia unei fabrici
    name = 'car'                                             # class variable
    fuel_support = [95, 98]
    color = 'white'
    doors = 4
    # cars_built = []
    def __init__(self, doors =4):
        self.doors = doors
        print('Starting constructor')

    # def change_car_color(self,color):
    #     print(f'Changing car {self.brand}')
    #     self.color = color

    def change_car_color_user_input(self,color):
        print(f'Changing car {self.name}')
        self.color = input('Your new color is :')
car = Car(2)
print(car.brand)
car.brand = 'BMW'
car.fuel_support.append(101)
car.change_car_color_user_input('red')

print(car.brand)
print(car.fuel_support)
print(car.color)
print(f'Car {car.brand} nr of doors is {car.doors}')

car2 = Car()
print('New car:', car2.name)
print('New car:', car2.fuel_support)
car2.change_car_color_user_input('blue')
print(car2.color)
print(f'Car {car2.name} nr of doors is {car.doors}')


# def change_car(self):
#     print('Changing car')
# change_car()


class Dacia():
    name = 'car'  # class variable
    fuel_support = [95, 98]
    color = 'white'
    doors = 4
    brand = 'Dacia'

    # cars_built = []
    def __init__(self, doors=4):
        self.doors = doors
        print('Starting constructor')

    def change_car_color(self,color):
         print(f'Changing car {self.name}')
         self.color = color

    def change_car_color_user_input(self, color):
        print(f'Changing car {self.name}')
        self.color = input('Your new color is :')

    def drive(self):
        print('Driving 2 well drive car')


class Bmw():
    name = 'car'  # class variable
    fuel_support = [95, 98]
    color = 'white'
    doors = 4
    brand = 'Dacia'

    # cars_built = []
    def __init__(self, doors=4):
        self.doors = doors
        print('Starting constructor')

    def change_car_color(self, color):
        print(f'Changing car {self.name}')
        self.color = color

    def change_car_color_user_input(self, color):
        print(f'Changing car {self.name}')
        self.color = input('Your new color is :')

    def drive(self):
        print('Driving 4 well drive car')