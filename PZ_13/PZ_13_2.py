# В матрице найти минимальный элемент в предпоследнем столбце.

import random


n = random.randint(2, 10)  # кол-во строк в матрице
m = random.randint(2, 10)  # кол-во столбцов матрицы

matr = [[random.randint(-20,20) for i in range(n)] for j in range(m)]  # создание матрицы с рандомными значениями

print("Матрица: ")  # вывод матрицы на экран для наглядности
for i in matr:
    print(*i)

min_i = min(matr[i][-2] for i in range(m))  # нахождение минимального элемента в матрице
print(f"Минимальный элемент предпоследнего столбца: {min_i}")
