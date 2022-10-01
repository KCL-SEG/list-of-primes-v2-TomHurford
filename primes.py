"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

# if n is 0 or negative return a ValueError

def primes(n):
    """Return a list of n prime numbers."""
    if n <= 0:
        raise ValueError("n must be a positive integer")
    primes = []
    i = 2
    while len(primes) < n:
        if is_prime(i):
            primes.append(i)
        i += 1
    return primes

def is_prime(n):
    """Return True if n is prime."""
    for i in range(2, n):
        if n % i == 0:
            return False
    return True