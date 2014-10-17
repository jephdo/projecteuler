"""
A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def is_palindrome(n):
    n = str(n)

    return list(n) == list(reversed(n))

def largest_palindrome_product():
    A = {(p,q): p*q for p in range(1000) for q in range(1000)}

    for k, v in A.iteritems():
        if not is_palindrome(v):
            A[k] = 0

    return max(A.values())

if __name__ == '__main__':
    print(largest_palindrome_product())
