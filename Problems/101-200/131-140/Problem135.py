def method():
    print("for values of a number n from 1 to 1 million, determine the number of solutions for n in which n can be "
          "expressed as z^2-y^2-x^2 in exactly 10 unique ways, where x,y,z are terms in a series of "
          "arithmetic progression")

    print()
    print(arithmetic_progression_sums(1000000, 10))
    return


def arithmetic_progression_sums(n: int, w: int) -> int:
    """
    General method for solving problem 135 with variable n and w
    :param n: limit for a number n
    :param w: number of unique ways n can be expressed as z^2 - y^2 - x^2 for x, y, z > 0
    :return: the number of solutions for n in which n can be expressed in w ways as z^2 - y^2 - x^2 for x, y, z > 0
    """
    slns = [0] * (n + 1)
    for u in range(1, n + 1):
        for v in range(n // u + 1):
            if (u + v) % 4 == 0 and (3 * v) > u and (3 * v - u) % 4 == 0:
                slns[u * v] += 1
    return slns.count(w)
