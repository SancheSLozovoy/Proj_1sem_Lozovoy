# Дан список размера N. Осуществить циклический сдвиг элементов списка вправо на
# одну позицию (при этом A1 перейдет в A2, A2 — в A3,..., AN — в A1).
import random
n = random.randint(1, 20)
a = []
n1 = 0
while n1 != n:
    a.append(random.randint(-20, 20))
    n1 += 1
print("Первоначальный список:", *a)
a.insert(0, a[-1])
del a[-1]
print("Результат", *a, sep=", ")