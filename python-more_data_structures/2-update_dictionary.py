#1/usr/bin/python3


def update_dictionary(a_dictionary, key, value):
    a_dictionary[key] = value
    return a_dictionary

my_dict = {'name': 'John', 'age': 30}

updated_dict = update_dictionary(my_dict, 'age', 31)
print(updated_dict)

updated_dict = update_dictionary(my_dict, 'city', 'New York')