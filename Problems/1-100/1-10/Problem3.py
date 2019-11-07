from math import sqrt
from HelperMethods import is_prime


def method():
    print("find the largest prime factor of 600,851,475,143")

    inp = 600851475143

    for i in range(int(sqrt(inp)), 0, -1):
        if inp % i == 0 and is_prime(i):
            print(i)
            break

    return

