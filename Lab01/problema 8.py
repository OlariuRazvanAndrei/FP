def fibonacci(n: int):
    fib = [1, 1]
    i = 2
    while i < n:
        fib.append(fib[i - 1] + fib[i - 2])
        i += 1
    return fib[n - 1]

print(fibonacci(6))

