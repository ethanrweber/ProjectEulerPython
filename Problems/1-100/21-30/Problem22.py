from Constants import FILE_PREFIX


def method():
    print("using the given file of names, assign a name score to each and sum all of the scores")

    filename = FILE_PREFIX + "22names.txt"
    with open(filename, "r") as f:
        names = f.read()

        names = names.split(',')
        names.sort()

        name_sum = 0
        for i in range(len(names)):
            name = names[i].replace('"', '').lower()
            name_sum += sum(ord(c) - 96 for c in name) * (i+1)

        print(name_sum)
    return
