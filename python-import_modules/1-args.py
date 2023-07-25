#!/usr/bin/python3

import sys


def main():
    arguments = sys.argv[1:]
    num_arguments = len(arguments)

    output_lines = []
    output_lines.append(f"Number of argument(s): {num_arguments}")

    if num_arguments == 0:
        output_lines.append(".")
    elif num_arguments == 1:
        output_lines.append(", argument:")
        output_lines.append(f"1: {arguments[0]}")
    else:
        output_lines.append(", arguments:")
        for i, arg in enumerate(arguments, start=1):
            output_lines.append(f"{i}: {arg}")

    output = "\n".join(output_lines)
    print(output)
    print(f"\n({len(output)} chars long)")

if __name__ == "__main__":
    main()
    