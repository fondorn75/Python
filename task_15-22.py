# 15. Дано число. Проверить кратно ли оно 7 и 23

def MultipleNumbers(number):
    if number % 7 == 0 and number % 23 == 0:
        return f"Число {number} кратное 7 и 23"
    else:
        return f"Число {number} не кратное 7 и 23"


print(MultipleNumbers(161))

# 16. Дано число обозначающее день недели. Выяснить является номер недели выходным днём


def WeekDayHolyday(day):
    days = ["Понедельник", "Вторник", "Среда",
            "Четверг", "Пятница", "Суббота", "Воскресенье"]
    if day == 6 or day == 7:
        return f"{days[day-1]} выходной"
    else:
        return f"{days[day-1]} будний день"


print(WeekDayHolyday(6))

# 17. По двум заданным числам проверять является ли одно квадратом другого


def SquareNumber(num1, num2):
    if num2 * num2 == num1:
        return f"Число {num1} является квадратом {num2}"
    else:
        return f"Число {num1} не является квадратом {num2}"


print(SquareNumber(27, 5))

# 18. Проверить истинность утверждения ¬(X ⋁ Y) = ¬X ⋀ ¬Y


def TrueOrFalse(x, y):
    return not(x and y) == (not x or not y)


print(TrueOrFalse(False, False))
print(TrueOrFalse(False, True))
print(TrueOrFalse(True, False))
print(TrueOrFalse(True, True))

# 19. Определить номер четверти плоскости, в которой находится точка с координатами Х и У, причем X ≠ 0 и Y ≠ 0


# 20. Ввести номер четверти, показать диапазоны для возможных координат


# 21. Программа проверяет пятизначное число на палиндромом.


# 22. Найти расстояние между точками в пространстве 2D/3D
