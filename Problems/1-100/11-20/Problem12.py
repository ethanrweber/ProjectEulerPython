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
    # iterate through sqrt(num) and increment total divisors by 2 for the divisor below and above the sqrt
    # + 2 because a positive integer > 1 is always divisible by 1 and itself
    return sum(2 for i in range(2, int(num ** .5) + 1) if num % i == 0) + 2
