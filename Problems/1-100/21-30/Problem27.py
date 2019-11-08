from HelperMethods import e_sieve, is_prime


def method():
    print("find the product of the coefficients a, b, for the "
          "quadratic expression that produces the maximum number "
          "of primes for consecutive values of n, starting with "
          "n = 0, where abs(a) < 1000 and abs(b) <= 1000")

    abs_lim = 1000
    b_pos = e_sieve(-abs_lim, abs_lim)

    max_prime = 0
    final_a = 0
    final_b = 0

    for a in range(-abs_lim, abs_lim):
        for b in b_pos:
            primes = find_number_of_primes(a, b)
            if primes > max_prime:
                max_prime = primes
                final_a = a
                final_b = b

    print(f"n^2 + {final_a}*n + {final_b} produces most primes: {max_prime}")
    print(f"product of coefficients a ({final_a}) and b ({final_b}) is {final_a * final_b}")

    return


def find_number_of_primes(a, b):
    number_of_primes = 0
    inp = 0

    while True:
        if not is_prime(inp * inp + a * inp + b):
            break
        inp += 1
        number_of_primes += 1

    return number_of_primes