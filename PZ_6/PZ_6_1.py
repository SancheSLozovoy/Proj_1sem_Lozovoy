# Дан список A размера N. Вывести вначале его элементы с нечетными номерами в
# порядке возрастания номеров, а затем — элементы с четными номерами в порядке
# убывания номеров: A1, A3, А5, …, A6, A4, A2. Условный оператор не использовать.
import random
n = random.randint(2, 20)
i = 0
while i < n:
    a = list(range(1, n + 1))
    i += 1
for element in a:
    lstM = list(a[0::2])
    lstMch = list(a[1::2])
    lstMch.sort(reverse=True)
print(*lstM, *lstMch, sep=", ")