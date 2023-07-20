#!/usr/bin/env python3

def fibonacci_sequence(n):
    if n <= 0:
        return []

    fib_sequence = [0]

    if n == 1:
        return fib_sequence

    fib_sequence.append(1)

    while len(fib_sequence) < n:
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_fib)

    return fib_sequence