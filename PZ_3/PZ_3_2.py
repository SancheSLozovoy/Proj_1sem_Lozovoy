try:
    A = int(input("Введите целое число: "))
    B = int(input("Введите второе целое число: "))
    if A != B:
        if A > B:
            B = A
        else:
            A = B
    else:
        A = B = 0
    print(A, B)
except:
    print("Ошибка, введены некоректные данные!")