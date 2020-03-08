from HelperMethods import is_prime, e_sieve


def method():
    print("how many circular primes are there below one million?")

    # circular prime: all rotations of digits are prime
    # ex: 197 - 197, 971, 719 all prime

    lim = 1_000_000
    circular_primes = [prime for prime in e_sieve(2, lim) if is_circular_prime(str(prime), str(prime))]
    print(f"generate primes first: {len(circular_primes)} below {lim}")
    return


def is_circular_prime(num_str, orig_num_str, iteration=0):
    while True:
        # if the num has been rotated back to the orig number without issue, return true
        if iteration > 0 and num_str == orig_num_str:
            return True

        # get number from string and rotate number
        num = int(num_str)
        rotate = num_str[1:] + num_str[0]

        # if iteration > 0, number has been rotated
        # check if it is prime
        # if true, go to next rotation
        # or if this is the first iteration, we know that this number is already prime, so check next rotation
        if iteration == 0 or iteration > 0 and is_prime(num):
            num_str = rotate
            iteration += 1
            continue

        # here, iteration > 0 and num is not prime, so return false
        return False
