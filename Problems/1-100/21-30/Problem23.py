
abundant_numbers = set()


def method():
    print("find the sum of all positive integers which cannot be written as the sum of 2 abundant numbers")

    # given that all numbers above 28123 can be written as sum of 2 abundant nums

    lim = 28124

    for i in range(1, lim):
        if is_abundant(i):
            abundant_numbers.add(i)

    not_sum_sum = 0
    for n in range(1, lim):
        if not is_abundant_sum(n):
            not_sum_sum += n
    print(not_sum_sum)
    return


def is_abundant(n):
    sum = 0
    for i in range(1, int(n/2) + 1):
        if n % i == 0:
            sum += i

    return sum > n


def is_abundant_sum(n):
    for an in abundant_numbers:
        if an > n:
            return False

        if (n - an) in abundant_numbers:
            return True

    return False
