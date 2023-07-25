#!/usr/bin/python3

import os
import inspect

def load_variable_from_file(file_path, variable_name):
    with open(file_path, 'r') as file:
        exec(file.read(), globals())
        return globals()[variable_name]

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "variable_load_2.py")
    variable_name = "a"

    a_value = load_variable_from_file(file_path, variable_name)
    print(a_value)