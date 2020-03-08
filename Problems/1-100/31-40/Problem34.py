from math import factorial


def method():
    print("find the sum of all numbers which are equal to the sum of the factorials of their digits")

    sum_nums = sum(i for i in range(3, 100_000) if sum(factorial(int(c)) for c in str(i)) == i)
    print(sum_nums)
    return
