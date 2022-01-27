import math
from xmlrpc.client import MAXINT, MININT

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


print(TrueOrFalse(0, 0))
print(TrueOrFalse(0, 1))
print(TrueOrFalse(1, 0))
print(TrueOrFalse(1, 1))

# 19. Определить номер четверти плоскости, в которой находится точка с координатами Х и У, причем X ≠ 0 и Y ≠ 0


def PlaneNumber(num1, num2):
    if num1 > 0 and num2 > 0:
        return 1
    elif num1 < 0 and num2 > 0:
        return 2
    elif num1 < 0 and num2 < 0:
        return 3
    else:
        return 4


print(f"Номер четверти - {PlaneNumber(-10, -10)}")

# 20. Ввести номер четверти, показать диапазоны для возможных координат


def QuarterNumber(number):
    if number == 1:
        return f"По Х от 0 до {MAXINT}, по Y от 0 до {MAXINT}"
    elif number == 2:
        return f"По Х от 0 до {MININT}, по Y от 0 до {MAXINT}"
    elif number == 3:
        return f"По Х от 0 до {MININT}, по Y от 0 до {MININT}"
    elif number == 4:
        return f"По Х от 0 до {MAXINT}, по Y от 0 до {MININT}"


print(QuarterNumber(3))

# 21. Программа проверяет пятизначное число на палиндромом.


def Polindrom(number):
    num = str(number)
    result = num[::-1]
    return result == num


print(Polindrom(54321235))

# 22. Найти расстояние между точками в пространстве 2D/3D


def Ploskost2D(xa, ya, xb, yb):
    kv = 2
    result = math.sqrt((math.pow((xb - xa), kv) + (math.pow((yb - ya), kv))))
    return result


def Ploskost3D(xa, ya, za, xb, yb, zb):
    kv = 2
    result = math.sqrt((math.pow((xb - xa), kv) +
                       (math.pow((yb - ya), kv) + (math.pow((zb - za), kv)))))
    return result


print(round(Ploskost2D(-10, 10, 15, -5), 2))
print(round(Ploskost3D(-10, 10, 15, -5, -15, 12), 2))
