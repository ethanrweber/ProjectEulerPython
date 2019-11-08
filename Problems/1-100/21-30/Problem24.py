from itertools import permutations


def method():
    print("what is the millionth lexicographic permutation of the digits 0123456789?")

    digits = "0123456789"
    n = 1000000

    perms = permute(digits)
    print(perms[n-1])
    return


def permute(s):
    perm = sorted(''.join(c) for c in permutations(s))
    return perm
