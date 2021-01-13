# Program of Addition of two number
First_Number = int(input())
Second_Number = int(input())


def add(a, b):
    while b != 0:
        res = a & b
        a = a ^ b
        b = res << 1
    return a


print(add(First_Number, Second_Number))
