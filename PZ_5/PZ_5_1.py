# С помощью функций получить вертикальную и горизонтальную линии. Линия проводится многократной печатью символа.
# Заключить слово в рамку изполученных линий.
def lean():
    a = str(input("Введите ваше слово: "))
    g_l = "_"  # задаю горизонтальную линию
    v_l = "|"  # задаю вертикальную линию
    sp_a = list(a)
    col_s = len(sp_a)
    print(g_l * col_s, v_l + a + v_l, g_l * col_s, sep="\n")  # вывод результата


lean()
