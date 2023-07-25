#!/usr/bin/python3

import sys


def main():
    arguments = sys.argv[1:]
    num_arguments = len(arguments)

    output_lines = []

    if num_arguments == 0:
        output_lines.append("0 arguments:")
    elif num_arguments == 1:
        output_lines.append("1 argument:")
    else:
        output_lines.append(f"{num_arguments} arguments:")

    for i, arg in enumerate(arguments, start=1):
        output_lines.append(f"{i}: {arg}")

    output = "\n".join(output_lines)
    print(output)
    print(f"\n({len(output)} chars long)")

    print("[stderr]: [Anything]")

if __name__ == "__main__":
    main()