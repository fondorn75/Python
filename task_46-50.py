import math
# 26. Дано число. Составить список чисел Фибоначчи, в том числе для отрицательных индексов
# для положительных формула: F(n) = F(n-1) + F(n-1)
# для отрицательных формула: F(n) = F(n+2) - F(n+1)


# 27. Строка содержит набор чисел. Показать большее и меньшее число

def StringNumbers():
    str = input("Введите любые числа: ")
    lst = []
    for i in str:
        lst.append(i)
    num1 = max(lst)
    num2 = min(lst)
    return f"Большее число - {num1}, Меньшее число - {num2}"


print(StringNumbers())

# 28. Найти корни квадратного уравнения Ax² + Bx + C = 0
#     * Математикой
#     * Используя дополнительные библиотеки*
# Чтобы найти корни уравнения, необходимо вычислить дискриминант.
# D = b*b – 4*a*c
# x1 = ((-b+(b*b-4*a*c)**0.5)/(2*a))
# x2 = ((-b-(b*b-4*a*c)**0.5)/(2*a))
# При D > 0, уравнение имеет два корня
# при D = 0, один корень
# при D ˂ 0, уравнение корней не имеет


def QuadraticEquation(a, b, c):
    D = b*b - 4*a*c
    if D < 0:
        return "Уравнение корней не имеет"
    elif D == 0:
        #x1 = ((-b+(b*b-4*a*c)**0.5)/(2*a))
        x1 = (-b+(math.sqrt(b*b-4*a*c))) / (2*a)
        #x2 = ((-b-(b*b-4*a*c)**0.5)/(2*a))
        x2 = (-b-(math.sqrt(b*b-4*a*c))) / (2*a)

        return f"Уравнение имеет один корень: {round(x1, 2)}, {round(x2, 2)}"
    elif D > 0:
        #x1 = ((-b+(b*b-4*a*c)**0.5)/(2*a))
        x1 = (-b+(math.sqrt(b*b-4*a*c))) / (2*a)
        #x2 = ((-b-(b*b-4*a*c)**0.5)/(2*a))
        x2 = (-b-(math.sqrt(b*b-4*a*c))) / (2*a)
        return f"Уравнение имеет два корня: {round(x1, 2)}, {round(x2, 2)}"


print(QuadraticEquation(-4, 2, 5))

# 29. Найти НОК двух чисел


# 30. Вычислить число  c заданной точностью d
# Пример: при d = 0.001,  = 3.141. 10-1d10-10