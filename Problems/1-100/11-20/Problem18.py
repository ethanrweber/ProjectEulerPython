from Constants import FILE_PREFIX

def method():
    print("find the maximum total from top to bottom of a triangle of numbers "
          "using only the 2 adjacent numbers below each number")

    filename = FILE_PREFIX + "18triangle.txt"
    with open(filename, 'r') as f:
        data = f.readlines()

        n = len(data)
        triangle = [None] * n
        for i in range(n):
            triangle[i] = [int(i) for i in str.split(data[i])]

        largest_values = [0] * n

        for i in range(n):
            largest_values[i] = triangle[n-1][i]

        for i in range(n - 2, -1, -1):
            for j in range(i+1):
                largest_values[j] = triangle[i][j] + max(largest_values[j], largest_values[j+1])

        print(largest_values[0])
    return
