from datetime import datetime


def method():
    print("how many ways can 2 pounds (English money) be generated with their currency?")

    # england uses pound and pence
    # 8 coin values: 1,2,5,10,20,50,100,200

    # thank you mathblog.dk for answer

    target = 200
    ways = 0

    # method 1: brute force
    s = datetime.now()
    bf_sln = brute_force(target)
    e = datetime.now()
    print("brute force solution: " + str(bf_sln))
    print("BF time: " + str(e-s) + " seconds")

    # method 2: dynamic programming
    s = datetime.now()
    dp_sln = dp(target)
    e = datetime.now()
    print("dynamic progamming solution: " + str(dp_sln))
    print("DP time: " + str(e-s) + " seconds")
    return


def brute_force(target):
    ways = 0
    for a in range(target, -1, -200):
        for b in range(a, -1, -100):
            for c in range(b, -1, -50):
                for d in range(c, -1, -20):
                    for e in range(d, -1, -10):
                        for f in range(e, -1, -5):
                            for g in range(f, -1, -2):
                                ways += 1
    return ways


def dp(target):
    target += 1
    coin_sizes = [1, 2, 5, 10, 20, 50, 100, 200]
    ways = [0] * target
    ways[0] = 1

    for i in range(len(coin_sizes)):
        for j in range(coin_sizes[i], target):
            ways[j] += ways[j - coin_sizes[i]]
    return ways[-1]
