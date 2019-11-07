# a bunch of helper methods

import math


def is_prime(num):
    if num < 2:
        return False

    for i in range(2, int((math.sqrt(num) + 1))):
        if num % i == 0:
            return False

    return True


def is_palindrome(string):
    leng = len(string)
    for i in range(leng):
        if string[i] != string[leng - i - 1]:
            return False
    return True


def esieve(upper_limit, lower_limit=2):
    sieve_bound = (upper_limit - 1) / 2
    upper_sqrt = int(math.sqrt(upper_limit) - 1) / 2

    prime_bits = [True] * (sieve_bound + 1)

    for i in range(upper_sqrt + 1):
        if prime_bits[i]:
            for j in range(i * 2 * (i+1), sieve_bound + 1, 2 * i + 1):
                prime_bits[j] = False

    numbers = []

    if lower_limit < 3:
        numbers.append(2)
        lower_limit = 3

    for i in range((lower_limit - 1) / 2, sieve_bound + 1):
        if prime_bits[i]:
            numbers.append(2 * i + 1)

    return numbers

