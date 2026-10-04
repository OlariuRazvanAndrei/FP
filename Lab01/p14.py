from math import sqrt


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for d in range(3, int(sqrt(n)) + 1, 2):
        if n % d == 0:
            return False
    return True


def block_length(k: int) -> int:
    # number of terms the natural number k contributes to the sequence
    if k == 1 or is_prime(k):
        return 1
    length = 0
    rest = k
    d = 2
    while rest > 1:
        if rest % d == 0:
            length += d
            while rest % d == 0:
                rest //= d
        d += 1
    return length


def term_in_block(k: int, position: int) -> int:
    # the term found at the given 1-based position inside the block of k
    if k == 1 or is_prime(k):
        return k
    rest = k
    d = 2
    while True:
        if rest % d == 0:
            if position <= d:
                return d
            position -= d
            while rest % d == 0:
                rest //= d
        d += 1


def nth_term(n: int) -> int:
    # the n-th element of the sequence, without storing its elements
    position = n
    k = 1
    while position > block_length(k):
        position -= block_length(k)
        k += 1
    return term_in_block(k, position)


def read_index() -> int:
    return int(input("Write the index n (n >= 1): "))


def print_result(n: int, term: int):
    print(f"The element at position {n} in the sequence is {term}")


def main():
    n = read_index()
    print_result(n, nth_term(n))


main()