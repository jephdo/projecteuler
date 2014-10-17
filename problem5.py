"""
2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?
"""

def factorize(n):
    """Return a dictionary of factors for a given number.

    >>> n = 2 * 2 * 3 * 5
    >>> factorize(n)
    {2: 2, 3: 1, 5: 1}
    """
    factors = {}

    # Loop will end when all factors are divided out of n leaving 1.
    while n > 1:
        for i in range(2, n+1):
            # Check how many times a number divides into n.
            while (n % i == 0) and n > 1:
                factors[i] = factors.setdefault(i, 0) + 1

                n /= i

    return factors

def combine_factors(fs):
    """
    Finds the largest exponent for each prime number from a list of factors.
    Then multiplies out all the factors, returning the smallest positive
    number divisible.
    """
    A = {}

    for factors in fs:
        for k,v in factors.items():
            A[k] = max(A.get(k, 0), v)

    mult = lambda p, q: p * q

    return reduce(mult, [k**v for k,v in A.items()])

def smallest_multiple(n):
    return combine_factors(factorize(i) for i in range(1,n+1))


if __name__ == '__main__':
    print(smallest_multiple(20))
