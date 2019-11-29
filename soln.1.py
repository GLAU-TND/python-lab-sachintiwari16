class MyException(Exception):
    pass


def Xyz(a, b):
    if (a + b) < 150:
        raise MyException("Custom Exception Occurred")
    else:
        print(a + b)


a = int(input())
b = int(input())
Xyz(30, 40)    