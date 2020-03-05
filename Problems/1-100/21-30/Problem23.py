

def method():
    print("find the sum of all positive integers which cannot be written as the sum of 2 abundant numbers")

    # given that all numbers above 28123 can be written as sum of 2 abundant nums
    lim = 28124

    abundant_numbers = set(i for i in range(1, lim) if is_abundant(i))

    not_sum_sum = sum(n for n in range(1, lim) if not is_abundant_sum(n, abundant_numbers))

    print(not_sum_sum)
    return


def is_abundant(n):
    sum_values = sum(i for i in range(1, n // 2 + 1) if n % i == 0)
    return sum_values > n


def is_abundant_sum(n, abundant_numbers):
    for an in abundant_numbers:
        if an > n:
            return False
        if (n - an) in abundant_numbers:
            return True
    return False
