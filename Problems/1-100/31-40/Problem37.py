from HelperMethods import e_sieve, is_prime


def method():
    print("find the sum of the only 11 primes that are truncatable from left to right and right to left")

    # ex: 3797 is prime
    # its truncations from ltr are all prime: 797, 97, 7
    # as well as rtl: 379, 37, 3

    lim = 1_000_000

    # ignore single-digit primes (2, 3, 5, 7)
    primes = e_sieve(11, lim)
    trunc_prime_sum = 0

    for p in primes:
        if is_truncatable_prime(p):
            trunc_prime_sum += p

    print(f"sum: {trunc_prime_sum}")
    return


def is_truncatable_prime(num):
    num_str = str(num)

    trunc_left = num_str[1:]
    trunc_right = num_str[:-1]

    # truncate number from ltr and rtl
    # if any truncation is not prime, return false
    while len(trunc_left) > 0:
        if not is_prime(int(trunc_left)):
            return False
        trunc_left = trunc_left[1:]

    while len(trunc_right) > 0:
        if not is_prime(int(trunc_right)):
            return False
        trunc_right = trunc_right[:-1]

    return True

