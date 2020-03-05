from Constants import FILE_PREFIX


def method():
    print("convert words to numbers based on the alphabetical position of each letter of the word. "
          "if the number is a triangle number, add it to the list")

    alpha = {}
    alph = "abcdefghijklmnopqrstuvwxyz"
    for i in range(len(alph)):
        c = alph[i]
        alpha[c] = i+1

    triangle_nums = set()
    for i in range(100):
        triangle_nums.add(int(.5 * i * (i+1)))

    filename = FILE_PREFIX + "42words.txt"
    f = open(filename, 'r')
    data = f.read()
    f.close()
    s = []
    for c in data:
        if c != '"':
            s.append(c)

    ss = ''.join(s)
    words = ss.split(',')

    tn_count = 0
    for word in words:
        lower = str.lower(word)
        word_sum = 0
        for c in lower:
            word_sum += alpha[c]

        if word_sum in triangle_nums:
            tn_count += 1

    print(f"{tn_count} triangle number words in file")
    return
