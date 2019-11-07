from HelperMethods import esieve

def method():
    print("find the sum of all primes < 2,000,000")

    prime_limit = 2000000

    sum = 0
    primes = esieve(prime_limit)
    for i in primes:
        sum += i

    print(sum)
    return
