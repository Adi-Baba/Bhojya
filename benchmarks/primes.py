"""
Python Benchmark: Prime Counting
Count primes up to N
"""

def is_prime(n):
    if n < 2:
        return False
    
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    
    return True

def count_primes(limit):
    count = 0
    for n in range(2, limit):
        if is_prime(n):
            count += 1
    return count

if __name__ == "__main__":
    import time
    start = time.time()
    result = count_primes(100000)
    end = time.time()
    print(f"Primes found: {result}")
    print(f"Time: {end - start:.3f} seconds")
