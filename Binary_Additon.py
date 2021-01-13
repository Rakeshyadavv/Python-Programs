# Program of a Binary Addition
def add(a, b):
    length = max(len(a), len(b))

    a = a.zfill(length)
    b = b.zfill(length)

    output = ''

    carry = 0

    for i in range(length - 1, -1, -1):
        r = carry
        r += 1 if a[i] == '1' else 0
        r += 1 if b[i] == '1' else 0
        output = ('1' if r % 2 == 1 else '0') + output
        carry = 0 if r < 2 else 1

    if carry != 0: output = '1' + output

    return output.zfill(length)


# Main Driving Code
First_Number = (input())
Second_Number = (input())
print(add(First_Number, Second_Number))
