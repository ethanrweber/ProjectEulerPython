def method():
    print("find the denominator of the resulting product of 4 fractions such that:"
          "\n - each fraction's numerator and denominator contain 2 digits,"
          "\n - removing the common digit of the numerator and denominator and dividing them yields "
          "\n\t the same result as dividing the numerator and denominator,"
          "\n - the trivial examples where numerator and denominator % 10 == 0 (such as 30/50) are ignored\n")

    product = 1
    count = 0
    for num in range(10, 100):
        for den in range(num+1, 100):
            if num % 10 == 0 and den % 10 == 0:
                continue

            ns, ds = str(num), str(den)
            pos, dpos = 0, 0
            # if ns[0] == ds[0]: pos,dpos = 0, 0 already covered by initialization
            if ns[0] == ds[1]:
                pos, dpos = 0, 1
            elif ns[1] == ds[0]:
                pos, dpos = 1, 0
            elif ns[1] == ds[1]:
                pos, dpos = 1, 1
            else:
                continue

            new_num = int(ns[1]) if pos == 0 else int(ns[0])
            new_den = int(ds[1]) if dpos == 0 else int(ds[0])

            if new_den == 0 or num / den != new_num / new_den:
                continue

            count += 1
            product *= new_num / new_den
            print(f"{num}/{den}, --> {new_num}/{new_den}")

    product = round(product, 3)
    print(f"{count} found, product: {product}")
    print(f"denom of product: {1 / product}")
    return
