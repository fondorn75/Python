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


# 42. Реализовать RLE алгоритм. реализовать модуль сжатия и восстановления данных.
# входные и выходные данные хранятся в отдельных файлах


# 43. Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
# Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]