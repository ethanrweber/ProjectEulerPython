from Constants import FILE_PREFIX


def method():
    print("using the given 20x20 grid, find the largest product of 4 adjacent numbers in the same direction"
          " (up, down, left, right, or diagonally)")

    filename = FILE_PREFIX + "11grid.txt"
    n = 20

    f = open(filename, "r")
    data = f.readlines()
    f.close()

    # initialize matrix
    m = [None] * n
    for i in range(n):
        m[i] = [None] * n

    i = 0
    for x in data:
        m[i] = str.split(x)
        for j in range(n):
            m[i][j] = int(m[i][j])
        i += 1

    # iterate m
    max = 0
    for i in range(n):
        for j in range(n):

            #dr/dl diag
            if i+3 < n:
                if j+3 < n:
                    diag = m[i][j] * m[i + 1][j + 1] * m[i + 2][j + 2] * m[i + 3][j + 3]
                    if diag > max:
                        max = diag
                if j - 3 >= 0:
                    diag = m[i][j] * m[i+1][j-1] * m[i+2][j-2] * m[i+3][j-3]
                    if diag > max:
                        max = diag

            # ur/ul diag
            if i-3 >= 0:
                if j+3 < n:
                    diag = m[i][j] * m[i-1][j+1] * m[i-2][j+2] * m[i-3][j+3]
                    if diag > max:
                        max = diag
                if j-3 >= 0:
                    diag = m[i][j] * m[i-1][j-1] * m[i-2][j-2] * m[i-3][j-3]

            # left/right
            if j+3 < n:
                right = m[i][j] * m[i][j+1] * m[i][j+2] * m[i][j+3]
                if right > max:
                    max = right

            # up/down
            if i+3 < n:
                down = m[i][j] * m[i+1][j] * m[i+2][j] * m[i+3][j]
                if down > max:
                    max = down

    print(max)
    return
