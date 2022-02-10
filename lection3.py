def mult(x):
    return x**2


# def ReadLine():
#     data = open("file.txt", "r")
#     list = []
#     for line in data:
#         list.append(int(line))
#     data.close()
#     return list

def ReadLine():
    data = open("file.txt", "r")
    res = list(map(int, data))
    data.close()
    return res


lst = ReadLine()

list = [(i, mult(i)) for i in lst if i % 2 == 0]

print(lst)
print(list)
