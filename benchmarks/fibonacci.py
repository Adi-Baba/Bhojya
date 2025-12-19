"""
Python Performance Benchmark
Computing Fibonacci Numbers (Recursive)
"""

def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def main():
    # Calculate fib(35) - computationally intensive
    result = fibonacci(35)
    
    # Result should be 9227465
    return result

if __name__ == "__main__":
    import time
    start = time.time()
    result = main()
    end = time.time()
    print(f"Result: {result}")
    print(f"Time: {end - start:.3f} seconds")
