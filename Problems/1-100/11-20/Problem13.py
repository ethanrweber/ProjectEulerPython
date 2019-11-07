from Constants import FILE_PREFIX


def method():
    print("find the first 10 digits of the sum of the hundred 50-digit numbers in the given file")

    filename = FILE_PREFIX + "13numbers.txt"
    f = open(filename, "r")
    data = f.readlines()
    f.close()

    sum = 0
    for line in data:
        sum += int(line)

    print(str(sum)[0:10])
    return
