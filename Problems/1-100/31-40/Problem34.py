from math import factorial


def method():
    print("find the sum of all numbers which are equal to the sum of the factorials of their digits")

    sum = 0
    for i in range(3, 100_000):
        c_sum = 0
        for c in str(i):
            c_sum += factorial(int(c))

        if c_sum == i:
            sum += i

    print(sum)
    return
