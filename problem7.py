"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
that the 6th prime is 13.

What is the 10 001st prime number?
"""

from itertools import islice, count

def erastosthenes_sieve():
    """
    Sieve of Erastosthenes algorithm for generating a list of primes
    up till n. Yields the primes as a generator rather than using a fixed
    size array
    """
    sieve = {}

    yield 2
    for q in islice(count(3), 0, None, 2): # iterates over [3,5,7,9,...]
        p = sieve.pop(q, None)

        if p is None:
            # q is not in the sieve yet, so q is prime
            sieve[q*q] = q
            yield q
        else:
            x = p + q
            while x in sieve or (x % 2 == 0):
                x += p
            sieve[x] = p

def nth_prime(n):
    primes = erastosthenes_sieve()

    return next(islice(primes, n-1, None))

if __name__ == '__main__':
    print(nth_prime(10001))
