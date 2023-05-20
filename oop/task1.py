# 1. Есть класс Person, конструктор которого принимает
# три параметра (не учитывая self) -
# имя, фамилию и квалификацию специалиста.
# Квалификация имеет значение заданное по умолчанию, равное единице.
# 2. У класса Person есть метод, который возвращает строку, включающую в себя всю информацию о сотруднике.
# 3. Класс Person содержит деструктор, который выводит на экран
#  фразу "До свидания, мистер (вместо троеточия должны выводиться имя и фамилия объекта).
# 4. В основной ветке программы создайте три объекта класса Person.
# Посмотрите информацию о сотрудниках и увольте самое слабое звено.


class Person:
    def __init__(self, name, surname, qualification=1):
        self.name = name
        self.surname = surname
        self.qualification = qualification

    def __str__(self):
        return f"{self.name} {self.surname}, квалификация: {self.qualification}"

    def __del__(self):
        print(f"До свидания, мистер {self.name} {self.surname}.")


person1 = Person("Иван", "Иванов", 3)
person2 = Person("Петр", "Петров", 2)
person3 = Person("Сидор", "Сидоров")

print(person1)
print(person2)
print(person3)

min_q = min([person1.qualification, person2.qualification, person3.qualification])

if person1.qualification == min_q:
    del person1
elif person2.qualification == min_q:
    del person2
else:
    del person3




