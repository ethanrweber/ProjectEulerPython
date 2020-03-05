from Constants import FILE_PREFIX


def method():
    print("find the first 10 digits of the sum of the hundred 50-digit numbers in the given file")

    filename = FILE_PREFIX + "13numbers.txt"
    sum_lines = 0
    with open(filename, 'r') as f:
        sum_lines = sum(int(line) for line in f.readlines())

    print(str(sum_lines)[0:10])
    return
