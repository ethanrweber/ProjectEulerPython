from HelperMethods import is_pandigital


def method():
    print("find the largest 1-9 pandigital, 9-digit number that can be formed as the concatenated product "
          "of an integer with (1,2,...,n) where n > 1")

    # ex: 192
    # 192*1 = 192, 192*2 = 384, 192*3 = 576
    # 192_384_576 contains all digits 1-9
    # ex: 9
    # 9*1 = 9, 9*2 = 18, 9*3 = 27, 9*4 = 36, 9*5 = 45
    # 9_18_27_36_45 contains all digits 1-9

    # max iteration is 9876: concatenating anything larger than that will be larger than the 9-digit max
    # 9877*1 = 9877, 9877*2 = 19754
    # 9877_19754 > max 9-digit pandigital 987654321
    # 9876*2 = 19752, 9876_19752 < 987654321

    max = 0
    max_i = 0
    for i in range(1, 9877):
        m = 0
        if i < 10:
            m = 5
        elif i < 100:
            m = 4
        elif i < 1000:
            m = 3
        elif i < 10000:
            m = 2

        concat = str(i)
        for n in range(2, m+1):
            concat += str(i * n)

        num = int(concat)
        if num < 123456789 or num > 987654321:
            continue

        if is_pandigital(num) and num > max:
            max = num
            max_i = i

    print(f" max num with a pandigital concatenated product is {max_i}")
    print(f"it's product is {max}")
    return
