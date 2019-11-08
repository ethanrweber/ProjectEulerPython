from math import factorial

def method():
    print("find the sum of the digits in 100 factorial (100!)")

    hf = factorial(100)

    sum = 0
    for c in str(hf):
        sum += int(c)

    print(sum)
    return
