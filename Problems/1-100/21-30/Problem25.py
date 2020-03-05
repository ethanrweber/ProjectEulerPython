def method():
    print("calculate fibonacci recursively to find the iteration of the first term with 1000 digits")

    # recursive bad :(
    result = fibonacci(1, 1)
    print(result)
    return


def fibonacci(p1, p2):
    i = 1
    while len(str(p1)) < 1000:
        i += 1
        p1, p2 = p1 + p2, p1

    return i