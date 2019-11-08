def method():
    print("how many unique paths are there in a 20x20 grid if you can only move right or down?")

    n = 20

    grid = [0] * (n+1)
    for i in range(len(grid)):
        grid[i] = [0] * (n+1)

    for i in range(n):
        grid[i][n] = 1
        grid[n][i] = 1

    for i in range(n-1, -1, -1):
        if i == 0:
            print("test")
        for j in range(n-1, -1, -1):
            grid[i][j] = grid[i+1][j] + grid[i][j+1]

    print("there are " + str(grid[0][0]) + " paths")

    return
