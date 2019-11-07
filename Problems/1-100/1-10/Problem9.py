def method():
    print("find a*b*c for the pythagorean triplet a^2 + b^2 = c^2 for a + b + c = 1000")

    a = 0
    b = 0
    c = 0
    loop_limit = 1000
    for i in range(loop_limit):
        for j in range(i + 1, loop_limit):
            if i + j < 1000:
                k = 1000 - i - j
                if i * i + j * j == k * k:
                    a = i
                    b = j
                    c = k

    print("a, b, c: ", str(a), str(b), str(c))
    print(str(a) + "^2 + " + str(b) + "^2 = " + str(c) + "^2")
    print(str(a) + " + " + str(b) + " + " + str(c) + " = 1000")
    print(str(a) + " * " + str(b) + " * " + str(c) + " = " + str(a*b*c))
    return

