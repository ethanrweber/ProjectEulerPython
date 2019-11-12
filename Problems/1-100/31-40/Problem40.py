def method():
    print("if dn represents the nth digit of the irrational fraction 0.1234567891011121314...")
    print("find d1 * d10 * d100 * d1000 * d10000 * d100000 * d1000000")
    #  d1 - d1million

    lim = 1_000_000

    string = ""
    for i in range(1, lim + 1):
        string += str(i)

    result = 1
    i = 1
    while len(str(i)) < len(str(lim)):
        result *= int(string[i-1])
        i *= 10
    print(result)
    return
