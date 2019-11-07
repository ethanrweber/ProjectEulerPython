def method():
    print("find the sum of every fibonacci number less than 4 million")

    limit = 4_000_000

    fib1 = 1
    fib2 = 1
    result = 0
    sum = 0

    while result < limit:
        if result % 2 == 0:
            sum += result
        result = fib1 + fib2
        fib2 = fib1
        fib1 = result

    print(sum)
    return
