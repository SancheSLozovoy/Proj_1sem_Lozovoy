# В исходном текстовом файле(hotline1.txt) найти всеномера телефонов,
# соответствующих шаблону 8(000)000-00-00. Посчитать количество полученных
# элементов. После фразы «Горячая линия» добавить фразу «Министерства
# образования Ростовской области», выполнив манипуляции в новом файле.

import re
p = re.compile(r'[8][(][0-9]{3}[)][0-9]{3}[-][0-9]{2}[-][0-9]{2}')
with open("hotline1.txt", "rt", encoding="UTF-8") as f1:
    t = f1.read()
    r = re.findall(p, t)
print(f"Количество полученных элементов: {len(r)}")
