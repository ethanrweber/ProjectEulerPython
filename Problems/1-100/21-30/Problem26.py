def method():
    print("which fraction from 1/1 to 1/1000 contains the longest recurring cycle "
          "when represented as a decimal, and what is that cycle?")

    # answer from mathblog.dk

    sequence_length = 0
    num = 0

    for i in range(1000, 1, -1):
        if sequence_length >= i:
            break

        found_remainders = [0] * i
        value = 1
        position = 0

        while found_remainders[value] == 0 and value != 0:
            found_remainders[value] = position
            value *= 10
            value %= i
            position += 1

        if (position - found_remainders[value]) <= sequence_length:
            continue

        num = i
        sequence_length = position - found_remainders[value]

    print("longest cycle: " + str(num) + ", len: " + str(sequence_length))
    return
