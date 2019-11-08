from Constants import FILE_PREFIX
import string


def method():
    print("using the given file of names, assign a name score to each and sum all of the scores")

    filename = FILE_PREFIX + "22names.txt"
    f = open(filename, "r")
    names = f.read()
    f.close()

    names = names.split(',')
    names.sort()

    name_sum = 0
    for i in range(len(names)):
        name = names[i].replace('"', '').lower()
        name_sum += get_str_val(name) * (i+1)

    print(name_sum)
    return


def get_str_val(s):
    ssum = 0
    for c in s:
        ssum += string.ascii_lowercase.index(c) + 1
    return ssum
