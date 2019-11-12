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


def is_pandigital(num):
    digits, count = 0, 0

    while num > 0:
        temp = digits
        shift = int(num % 10 - 1)
        if shift < 0:
            break
        digits = digits | 1 << shift
        if temp == digits:
            return False

        count += 1
        num /= 10

    return digits == (1 << count) - 1


def e_sieve(lower_limit, upper_limit):
    return esieve(upper_limit, lower_limit)


def esieve(upper_limit, lower_limit=2):
    sieve_bound = int((upper_limit - 1) / 2)
    upper_sqrt = int((math.sqrt(upper_limit) - 1) / 2)

    prime_bits = [1] * (sieve_bound + 1)

    for i in range(1, upper_sqrt + 1):
        if prime_bits[i] == 1:
            for j in range(i * 2 * (i+1), sieve_bound + 1, 2 * i + 1):
                prime_bits[j] = 0

    numbers = [] * int(upper_limit / (math.log(upper_limit, math.e) - 1.08366))

    if lower_limit < 3:
        numbers.append(2)
        lower_limit = 3

    for i in range(int((lower_limit - 1) / 2), sieve_bound + 1):
        if prime_bits[i] == 1:
            numbers.append(int(2 * i + 1))

    return numbers


def factorial(num):
    sum = 1
    for i in range(1, num+1):
        sum *= i
    return sum


def get_divisors(n):
    if n < 1:
        return None
    divisors = [1]
    for i in range(2, math.ceil(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.append(i)
            divisors.append(n / i)
    return divisors


def sum_divisors(n):
    sum = 0
    for d in get_divisors(n):
        sum += d
    return sum