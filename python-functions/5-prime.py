#!/usr/bin/env python3

def is_prime(number):
    if number <= 1:
        return False

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True

(is_prime(17))
(is_prime(15))
(is_prime(-5))
(is_prime(0))
