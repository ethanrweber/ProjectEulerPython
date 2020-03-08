from HelperMethods import is_palindrome


def method():
    print("find the sum of all numbers < 1000000 that are palindromic in base 10 and base 2")

    lim = 1_000_000
    sum_palindromes = sum(i for i in range(1, lim) if is_palindrome(str(i)) and is_palindrome(bin(i)[2:]))
    print(sum_palindromes)
    return
