class Person():
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name


per = Person("alex")
per.set_name('mike')
print(per.get_name())
