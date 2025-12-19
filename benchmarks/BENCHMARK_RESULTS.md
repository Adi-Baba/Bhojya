# Bhojya vs Python Performance Benchmark

## Test Configuration
- **CPU**: 4 cores
- **OS**: Windows 10
- **Bhojya**: v1.0 (LLVM native compilation)
- **Python**: Python 3.13.9

## Benchmark: Recursive Fibonacci(35)

| Language | Time (ms) | Time (s) | Speedup |
|----------|-----------|----------|---------|
| Bhojya   | 207 ms | 0.207s | 1.0x (baseline) |
| Python   | 4486 ms | 4.486s | 21.7x slower |

## Result
**Bhojya is 21.7x faster than Python** for this computational workload.

## Why the difference?
- **Bhojya**: Compiles to optimized native machine code ahead-of-time (AOT)
- **Python**: Interpreted/JIT compiled at runtime with interpreter overhead

## Conclusion
For computationally intensive tasks, Bhojya's native compilation provides significant performance advantages over interpreted languages like Python.
