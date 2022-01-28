# 23. Показать таблицу квадратов чисел от 1 до N

def SquareTable(n):
    list = {}
    j = 0
    for i in range(1, n + 1):
        list[j] = i**2
        j += 1
    return list.values()


print(SquareTable(8))

# 24. Найти кубы чисел от 1 до N


def ThirdPower(n):
    list = {}
    j = 0
    for i in range(1, n + 1):
        list[j] = i**3
        j += 1
    return list.values()


print(ThirdPower(8))

# 25. Найти сумму чисел от 1 до А


def SummaNumbers(a):
    temp = 0
    for i in range(1, a + 1):
        temp += i
    return temp


print(SummaNumbers(10))

# 26. Возведите число А в натуральную степень B используя цикл


def NaturalDegree(a, b):
    temp = {}
    j = 0
    for a in range(1, b + 1):
        temp[j] = a**b
        j += 1
    return temp.values()


print(NaturalDegree(2, 3))

# 27. Определить количество цифр в числе


# 28. Подсчитать сумму цифр в числе


# 29. Написать программу вычисления произведения чисел от 1 до N


# 30. Показать кубы чисел, заканчивающихся на четную цифру
