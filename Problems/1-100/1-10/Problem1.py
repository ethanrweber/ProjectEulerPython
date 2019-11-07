def method():
    print("find the sum of every number from 0-100 that is divisible by 3 or 5")
    sum = 0
    for i in range(0, 101):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    print(sum)
    return
