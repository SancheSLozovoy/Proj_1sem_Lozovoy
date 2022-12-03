# Выполнить сортировку словаря d = {'a': 1, 'b': 2, 'c': 3}
d = {'a': 1, 'b': 2, 'c': 3}
print("Результат сортировки:")
for i in sorted(d.items(), key=lambda sort: (sort[0], sort[1])):
    print(*i)