class Car:
    def __init__(self, fuel):
        self.__fuel = fuel

    def get_fuel(self):
        return self.__fuel

    def set_fuel(self, new_fuel):
        if new_fuel < 0:
            print("Ошибка, не может быть меньше нуля")
        else:
            self.__fuel = new_fuel


car = Car(20)
print(car.get_fuel())

car.set_fuel(-10)
print(car.get_fuel())