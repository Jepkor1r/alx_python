#!/usr/bin/python3

import sys


if __name__ == "__main__":
    args = sys.argv[1:]
    num_args = len(args)

    print(f"Number of argument(s): {num_args}", end="")
    print("s" if num_args != 1 else "", end="")
    print(":", end="" if num_args > 0 else ".\n")

    for i, arg in enumerate(args, 1):
        print(f"{i}: {arg}")