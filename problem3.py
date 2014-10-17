"""
The prime factors of 13195 are 5, 7, 13 and 29. What is the largest prime
factor of the number 600851475143?
"""

def largest_prime_factor(n):
    # The max prime factor of any number n is at most sqrt(n).
    k = int(round(n**0.5+1))

    while k > 0:
        if (n % k == 0) and is_prime(k):
            return k

        k -= 1

    return k

def is_prime(n):
    if n < 2:
        return False
    elif n == 2 :
        return True
    elif n % 2 == 0:
        return False

    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False

    return True

if __name__ == '__main__':
    print(largest_prime_factor(600851475143))
