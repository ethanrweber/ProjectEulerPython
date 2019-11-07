def method():
    print("find the difference between the sum of the squares of "
          "the first one hundred natural numbers and the square of the sum")

    # sum of squares of the first n natural numbers: 1*1 + 2*2 + 3*3 + ... + n*n
    # square of the sum of the first n natural numbers: (1 + 2 + 3 + ... + n)^2
    # result: square of the sum - sum of squares

    sumOfSquares = 0
    squareOfSum = 0
    for i in range(1, 101):
        sumOfSquares += i * i
        squareOfSum += i
    squareOfSum *= squareOfSum

    print(squareOfSum - sumOfSquares)
    return
