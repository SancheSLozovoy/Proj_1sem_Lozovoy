# Книжные магазины предлагают следующие коллекции книг.
# Магистр – Лермонтов, Достоевский, Пушкин, Тютчев
# ДомКниги – Толстой, Грибоедов, Чехов, Пушкин.
# БукМаркет – Пушкин, Достоевский, Маяковский.
# Галерея – Чехов, Тютчев, Пушкин.
# Определить:
# 1.в каких магазинах одновременно можно и нельзя приобрести книги Достоевского и Пушкина.
# 2.в ассортимент магазина Галерея добавить автора Грибоедов.
# 3.какие книги из магазина ДомКниги отсутствуют в магазине Галерея
Magistr = {"Лермонтов", "Достоевский", "Пушкин", "Тютчев"}
DomKnigi = {"Толстой", "Грибоедов", "Чехов", "Пушкин"}
BukMarket = {"Пушкин", "Достоевский", "Маяковский"}
Galery = {"Чехов", "Тютчев", "Пушкин"}
# 1
for i in Magistr, DomKnigi, BukMarket, Galery:
    if "Достоевский" not in i or "Пушкин" not in i:
        print("Ассортимент, где не содержится одновременно Достоевского и Пушкина:", *i)
    else:
        print("Ассортимент где содержится одновременно Достоевский и Пушикн:", *i)

# 2
Galery.add("Грибоедов")
print("\n", "Обновленный ассортимент Галереи:", *Galery, "\n")

# 3
print("Книги из магазина ДомКниги, которые отсутствуют в магазине Галерея:", *DomKnigi - Galery)
