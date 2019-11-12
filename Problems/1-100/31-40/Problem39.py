def method():
    print("assuming a number p is the perimeter of a triangle, what number maximizes the number of triangles "
          "possible from perimeter p?")

    # ex: p = 120
    # possibilities: 20,48,52, 24,45,51, 30,40,50

    # thank you mathblog.dk

    result = 0
    result_solutions = 0

    for p in range(2, 1001, 2):
        num_solutions = 0
        for a in range(2, int(p/3)):
            if p * (p - 2 * a) % (2 * (p - a)) == 0:
                num_solutions += 1
        if num_solutions > result_solutions:
            result = p
            result_solutions = num_solutions

    print(f"result: {result}")
    print(f"number of solutions: {result_solutions}")
    return
