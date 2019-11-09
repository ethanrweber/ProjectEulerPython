def method():
    print("find the sum of all numbers that can be written as the sum of "
          "fifth powers of their digits")

    # upper bound
    # max digit = 9, 9^5 = 59049. max digits = 5
    # 5 * 9^5 = 295245, so with 5 digits we can make a 6 digit number. (too low)
    # 6 * 9^5 = 354294, so with 6 digits we can make a 6 digit number
    # another check
    # 9 * 9^5 (aka 9^6) = 531441, so with 9 digits we can only make a 6 digit number
    # so a number with 6 digits seems like a good bound

    power = 5

    results = []

    for n in range(2, 6 * (9 ** power)):  # loose approximation of upper bound
        ns = str(n)
        l = len(ns)
        i_digits = [0] * l
        powers_sum = 0
        for i in range(l):
            i_digits[i] = int(ns[i])
            powers_sum += i_digits[i] ** power

        if n == powers_sum:
            results.append(n)

    print(f"{len(results)} numbers whose digits to the power of {power} = the original number")
    print(f"sum: {sum(results)}")
    return
