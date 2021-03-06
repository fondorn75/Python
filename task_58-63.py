# 38. Напишите программу, удаляющую из текста все слова содержащие "абв".

text = 'Строка абвал не существует в этом сабвуфер мире сабвиль.'


def DeleteSymbols():
    temp = text.split(' ')
    str = 'абв'
    newStroka = []
    for word in temp:
        if str not in word:
            newStroka.append(word)
    result = ' '.join(newStroka)
    return result


print(DeleteSymbols())

# 39. Помните игру с конфетами из модуля "Математика и Информатика"? Создайте такую игру для игры человек против человека
#     * Добавьте игру против бота
#     * Подумайте как наделить бота "интеллектом"


# 40. Вы когда-нибудь играли в игру "Крестики-нолики"? Попробуйте создать её.


# 41. Написать программу вычисления арифметического выражения заданного строкой.
# Используются операции +,-,/,*. приоритет операций стандартный.
# Пример: 2+2 => 4; 1+2*3 => 7; 1-2*3 => -6;
# * Добавить возможность использования скобок, меняющих приоритет операций.
# Пример: 1+2*3 => 7; (1+2)*3 => 9;

def New_calc():
    stroka = input('Введите пример: ')
    test = list(stroka.split(' '))
    x = int(test[0])
    y = int(test[2])
    if test[1] == '+':
        result = x + y
    elif test[1] == '-':
        result = x - y
    elif test[1] == '*':
        result = x * y
    elif test[1] == '/':
        result = x / y
    return (f"Результат вычислений: {stroka} = {result}")


print(New_calc())


# 42. Реализовать RLE алгоритм. реализовать модуль сжатия и восстановления данных.
# входные и выходные данные хранятся в отдельных файлах

def rle_system():
    stroka = 'aaadddeeffwwrttteegqqbbbbbfffffhjj'
    temp = stroka[0]
    count = 0
    rle = ''
    for i in stroka:
        if i == temp:
            count += 1
        else:
            rle += f'{count}{temp}'
            temp = i
            count = 1
    rle += f'{count}{temp}'
    return rle


print(rle_system())


# 43. Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
# Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

numbers = [1, 2, 3, 5, 1, 5, 3, 10, 2, 4, 10, 11]


def UniqueNumbers():
    newnumbers = []
    for i in numbers:
        if numbers.count(i) < 2:
            newnumbers.append(i)

    return newnumbers


print(UniqueNumbers())
