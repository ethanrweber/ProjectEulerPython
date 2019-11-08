def method():
    print("what is the sum of the digits of 2^1000?")

    power = 2 ** 1000

    sum = 0
    for c in str(power):
        sum += int(c)

    print(sum)
    return
