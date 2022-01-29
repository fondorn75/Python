# 11. Для натурального N создать множество: 1, -3, 9, -27, 81 и т.д.

def NaturalN(N):
    list = set()
    for i in range (N):
        list.add(3**i)
    return sorted(list)



print(NaturalN(6))

# 12. Для натурального N создать словарь индекс-значение, состоящий из элементов последовательности 3k + 1.


def DictionaryN(n):
    result = {}
    for k in range(1, n+1):
        result[k] = 3*k+1
    return result


print(DictionaryN(6))

# 13. Пользователь задаёт две строки. Определить количество вхождений одной строки в другой.


# 14. Подсчитать сумму цифр в вещественном числе.


# 15. Написать программу получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда
# [ 1, 2, 6, 24 ]
