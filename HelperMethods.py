# a bunch of helper methods

import math


def is_prime(num):
    if num == 1 or num == 0:
        return False

    for i in range(2, int(math.sqrt(num)), 1):
        if num % i == 0:
            return False

    return True


def is_palindrome(string):
    leng = len(string)
    for i in range(leng):
        if string[i] != string[leng - i - 1]:
            return False
    return True
