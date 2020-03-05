from HelperMethods import sum_divisors


def method():
    print("find the sum of all amicable numbers < 10,000")

    # d(n) is the sum of numbers < n which divide evenly into n
    # if d(a) = b and d(b) = a and a != b then a and b are amicable numbers

    # ex: d(220) = 1+2+4+5+10+11+20+22+44+55+110 = 284
    #     d(284) = 1+2+4+71+142 = 220

    lim = 10_000

    am_sum = 0
    for i in range(2, lim):  # sum of divisors of 1 = 0 or 1, either way it won't match anything
        sum_of_divisors = sum_divisors(i)
        for j in range(i+2, lim, 2):
            if sum_of_divisors == j and sum_divisors(j) == i:
                am_sum += i + j
    print(am_sum)
    return
