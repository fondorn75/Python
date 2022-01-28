from asyncore import write


def FirstFunc(a):
    return a**2


def WriteFile(str):
    data = open("test.txt", "a")
    data.writelines(str)
    data.close()


def WriteLine(str):
    with open("test.txt", "a") as data:
        data.write(str)


def ReadLine():
    data = open("test.txt", "r")
    for line in data:
        print(line)
    data.close()
