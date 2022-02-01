from random import randint
# 16. Задать список из n чисел последовательности (1+1/n)^n и вывести на экран их сумму


def SummaNumberN(n):
    tmp = []
    for n in range(1, n + 1):
        tmp.append((1 + 1 / n)**n)
    return sum(tmp)


print(SummaNumberN(10))

# 17. Задать список из N элементов, заполненных числами из [-N, N]. Найти произведение элементов на указанных позициях.
#     Позиции хранятся в файле file.txt в одной строке одно число


def ListElements(N):
    ListNumbers = []
    for i in range(-N, N + 1):
        ListNumbers.append(i)

    data = open("file.txt", "r")
    for line in data:
        print(ListNumbers[int(line)])
    data.close()
    return ListNumbers


print(ListElements(5))

# 18. Реализовать алгоритм перемешивания списка.

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def RandomNumbersInList():
    tmp = []
    q = 0
    for i in range(len(lst)):
        q = randint(0, 9)
        tmp = lst[q]
        lst[q] = lst[i]
        lst[i] = tmp

    return lst


print(RandomNumbersInList())

# 19. Реализовать алгоритм задания случайных чисел. 
# Без использования встроенного генератора псевдослучайных чисел

def RandomNumbers():
    result = 0
    
    return result

# 20. Определить, присутствует ли в заданном списке строк, некоторое число
