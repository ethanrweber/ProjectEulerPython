from HelperMethods import is_palindrome

def method():
    print("find the largest palindrome made from the product of two 3-digit numbers")
    one = 0
    two = 0
    biggest_palindrome = 0
    for i in range(999, 100, -1):
        for j in range(999, 100, -1):
            m = i * j
            if m > biggest_palindrome and is_palindrome(str(m)):
                biggest_palindrome = m
                one = i
                two = j
    print("biggest palindrome: " + str(biggest_palindrome) + " = " + str(one) + " * " + str(two))
    return
