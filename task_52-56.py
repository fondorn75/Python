# 32. Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.

from random import randint


lst = [1, 4, 3, 2, 1, 2, 5, 6, 8, 5, 3, 9, 7, 8, 9, 7]


def UniqueNumbers():
    result = list(map(int, set(lst)))
    return result


print(UniqueNumbers())


# 33. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x²

def Polynomial(k):
    str = []
    for i in range(0, k + 1):
        coeff = randint(0, 100)
        if i >= 2:
            str.append(f"{coeff}*x^{i} + ")
        elif i == 1:
            str.append(f"{coeff}*x + ")
        elif i == 0:
            str.append(f"{coeff} = 0")
    stroka = str[::-1]
    result = ''.join(stroka)
    with open("test2.txt", "a") as data:
        data.write(result + '\n')


Polynomial(5)

# 34. Даны два файла в каждом из которых находится запись многочлена. Сформировать файл содержащий сумму многочленов.
# x = 1
# test = (x**2 + 5*x + 2) + (x**2 - 5*x + 3) = 2*x**2 + 5


# 35. В файле находится N натуральных чисел, записанных через пробел. Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найти его.

def Numbers():
    data = open("numbers.txt", "r")
    res = list(map(int, data.read().split(' ')))
    for i in range(1, len(res)):
        if res[i] - 1 != res[i - 1]:
            return res[i] - 1
    data.close()


print(Numbers())

# 36. Дан список чисел. Выделить среди них числа, удовлетворяющие условию: следующее больше предыдущего.
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.


def Increase():
    tmp = 0
    result = []
    for i in lst:
        if i > tmp:
            tmp = i
            result.append(tmp)
    return result


print(Increase())
