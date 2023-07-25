#!/usr/bin/python3

import sys


def main():
    arguments = sys.argv[1:]
    num_arguments = len(arguments)

    print(f"Number of argument(s): {num_arguments}", end="")

    if num_arguments == 0:
        print(".")
    elif num_arguments == 1:
        print(f", argument: {arguments[0]}")
    else:
        print(", arguments:")

        # Print each argument and its position
        for i, arg in enumerate(arguments, start=1):
            print(f"{i}: {arg}")

if __name__ == "__main__":
    main()