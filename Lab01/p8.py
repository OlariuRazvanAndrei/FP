def smallest_fibonacci_greater_than(n: int) -> int:
    # returns the smallest Fibonacci number strictly greater than n
    prev, current = 1, 1
    while current <= n:
        prev, current = current, prev + current
    return current


def read_number() -> int:
    return int(input("Write a natural number n: "))


def print_result(n: int, m: int):
    print(f"The smallest Fibonacci number greater than {n} is {m}")


def main():
    n = read_number()
    print_result(n, smallest_fibonacci_greater_than(n))


main()
