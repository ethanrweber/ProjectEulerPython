from math import sqrt


def method():
    print("what is the value of the first triangle number with over 500 divisors?")

    n = 0
    next = 0
    while is_divisible(n) <= 500:
        next += 1
        n += next

    print(n)
    return


def is_divisible(num):
    total_divisors = 2  # num is always divisible by 1 and itself
    # iterate through sqrt(num) and increment total divisors by 2 for the divisor below and above the sqrt
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            total_divisors += 2

    return total_divisors
