def method():
    print("what is the smallest positive number evenly divisible by all numbers 1-20?")
    result = 20
    while True:
        if divisible_by_all(result):
            break
        result += 20
    print(result)
    return


def divisible_by_all(num):
    return num % 11 == 0 and num % 12 == 0 and num % 13 == 0 and num % 14 == 0 and num % 15 == 0 \
        and num % 16 == 0 and num % 17 == 0 and num % 18 == 0 and num % 19 == 0 and num % 20 == 0
