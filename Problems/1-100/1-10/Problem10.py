from HelperMethods import esieve


def method():
    print("find the sum of all primes < 2,000,000")

    prime_limit = 2000000
    print(sum(esieve(prime_limit)))
    return
