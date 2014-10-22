"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

from itertools import takewhile

from problem7 import erastosthenes_sieve


def sum_of_primes(n):
    primes = erastosthenes_sieve()

    return sum(takewhile(lambda p: p < n, primes))

if __name__ == '__main__':
    print(sum_of_primes(2000000))

