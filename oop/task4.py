# Создайте класс «Список», который имеет методы
# для добавления и удаления элементов,
# поиска элемента и сортировки списка.
# Создать экземпляр класса и выполнить в нем следующие действия:
# 1. Заполнить список 15 случайными числами
# 2. Проверить наличие в списке элемента со значением 2
# и удалить его из списка
# 3. Выполнить сортировку оставшихся элементов
# Результаты работы показывать в консоль.


import random


class List:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def remove(self, item):
        self.items.remove(item)

    def find(self, item):
        return item in self.items

    def sort(self):
        self.items.sort()


my_list = List()

for i in range(15):
    my_list.add(random.randint(1, 10))
print(f'Первоначальный список: {my_list.items}')

for i in my_list.items:
    if my_list.find(2):
        my_list.remove(2)

my_list.sort()

# Выводим результаты работы
print(f"Фильтрванный список список: {my_list.items}")