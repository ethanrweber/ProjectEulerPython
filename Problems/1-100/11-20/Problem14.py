def method():
    print("Collatz Conjecture! which starting number < 1,000,000 produces the longest collatz chain?")
    print("note: takes up to 15 seconds")
    max = 0
    max_chain = 0
    for i in range(1, 1_000_000, 2):
        # even numbers have shorter chains
        chain = collatz(i)
        if chain > max_chain:
            max = i
            max_chain = chain

    print(str(max) + "produces the longest chain: " + str(max_chain))
    return


def collatz(n):
    chain = 0
    while n > 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = 3 * n + 1
        chain += 1
    return chain
