from HelperMethods import is_pandigital


def method():
    print("find the sum of all products whose multiplicand/multiplier/product "
          "identity can be written as a 1-9 pandigital")

    # ex: 39 x 186 = 7254. 9 total digits covering 1-9

    products = set()

    # lower bound for 2dig * 3dig = 10*100 = 1000 --- total 9 digits
    # upper bound for 2d * 3d = 99*999 = 98901 --- total 10 digits (too many)

    for i in range(1, 10000):
        for j in range(i+1, 10000):
            prod = i*j
            if prod > 99999:
                break

            concat = str(i) + str(j) + str(prod)
            if len(concat) != 9:
                continue
            if is_pandigital(int(concat)):
                products.add(prod)

    print(f"{len(products)} unique products")
    print(f"sum: {sum(products)}")
    return
