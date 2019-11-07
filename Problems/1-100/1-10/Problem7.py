from HelperMethods import is_prime


def method():
    print("find the 10,001st prime number")

    prime_counter = 0
    i = 1
    while prime_counter != 10001:
        i += 1
        if is_prime(i):
            prime_counter += 1

    print(i)
    return
