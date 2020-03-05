def method():
    print("find the sum of the numbers along the diagonals of a 1001x1001 square matrix")

    sum = 1  # 1x1 square
    n = 1001

    num = 1
    dist = 2
    for side in range(3, n+1, 2):  # side length of each outer spiral
        # below: num increases by i, sum increases by the i'th triangular number
        # for i in range(4):
        #     num += dist
        #     sum += num

        num, sum = num + 4 * dist, sum + 4 * num + 10 * dist
        dist += 2

    print(sum)
    return
