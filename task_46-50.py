import math
# 26. Дано число. Составить список чисел Фибоначчи, в том числе для отрицательных индексов
# для положительных формула: F(n) = F(n-1) + F(n-2)
# для отрицательных формула: F(n) = F(n+2) - F(n+1)


def Fibonachi(n):
    sum = 0
    ch1 = 0
    ch2 = 1
    lstResult = []

    for i in range(n):
        if i < n:
            sum = ch1 + ch2
            ch1 = ch2
            ch2 = sum
            i += 1
        lstResult.append(sum)

    return lstResult


print(Fibonachi(7))


def Fibonacci(n):
    if (n == 1 or n == 2):
        return 1
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)


def PrintFibonacci(n):
    listFib = []
    for i in range(n):
        listFib.append(Fibonacci(i))
    return listFib


print(PrintFibonacci(10))

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


def NOK(a, b):
    NOK.multiple = NOK.multiple + b
    if ((NOK.multiple % a == 0) and (NOK.multiple % b == 0)):
        return NOK.multiple
    else:
        NOK(a, b)
    return NOK.multiple


NOK.multiple = 0


def PrintNok():
    a = 10
    b = 8
    if a > b:
        temp = NOK(b, a)
    else:
        temp = NOK(a, b)
    return temp


print(PrintNok())

# 30. Вычислить число  c заданной точностью d
# Пример: при d = 0.001,  = 3.141. 10-1d10-10

number = "0.00001"


def NumberAccuracy(number2):
    count = len(number) - 2
    result = float(number2)

    return round(result, count)


print(NumberAccuracy(3.123569887415))
