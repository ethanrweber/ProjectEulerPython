def method():
    print("calculate fibonacci recursively to find the iteration of the first term with 1000 digits")

    result = fibonacci(1, 1)
    print(result)
    return


def fibonacci(p1, p2):

    temp = p1
    i = 1
    while len(str(temp)) < 1000:
        i += 1
        temp = p1
        p1 += p2
        p2 = temp
    return i