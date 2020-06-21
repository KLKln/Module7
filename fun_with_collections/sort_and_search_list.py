"""
Program:sort_and_search_list.py
Author: Kelly Klein
Last date modified: 6/21/2020
This program will take user input of numbers and store them in a list.
"""


def get_input():
    """
    Use reST style.
    :return: the number user entered
    """
    while True:
        try:
            user_input = input(print('Enter a number to add to the list: '))
            if user_input.isalpha():
                raise ValueError
        except ValueError:
            print('Positive numbers only please')
            continue

        return user_input


def make_list():
    """
    Use reST style.
    :return: the 3 number user entered
    raises TypeError: raises an exception if user uses alphabet
    """
    user_list = []

    for i in range(0, 3):
        user_number = get_input()
        user_list.append(int(user_number))

    print(user_list)
    return user_list


if __name__ == '__main__':
    make_list()
