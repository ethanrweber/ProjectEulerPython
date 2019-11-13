from HelperMethods import e_sieve, is_pandigital


def method():
    print("what is the largest 1-n pandigital prime that only uses each digit up to n once?")

    lim = 10000000

    primes = e_sieve(2, lim)

    nums = []
    for p in primes:
        if is_pandigital(p):
            nums.append(p)
    print(f"count: {len(nums)}")
    print(f"largest: {max(nums)}")
    return
