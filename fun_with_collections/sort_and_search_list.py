"""
Program:sort_and_search_list.py
Author: Kelly Klein
Last date modified: 6/21/2020
This program will take user input to search a list for a number
and also sort the list.
"""

user_list = [21, 31, 56, 78, 22, 4, 13, 42, 9]

def search_list(user_list):
    """
    Use reST style.
    :param user_list: list passed in
    :return: the index of the number user chooses, or -1 if not found
    """
    #return the index of the object in the list
    number_search = int(input('What number would you like to search for: '))
    for i in range(len(user_list)):
        if user_list[i] == number_search:
            index = user_list.index(number_search)
            return print('your number is at index', index)

        else:
            return print(-1)


    # or -1 if not found
def sort_list(user_list):
    """
    Use reST style.
    :param user_list: list passed in
    :return: the list sorted
    """
    #sorts the list
    user_list.sort() #no return because it calls a built in python function
    print(user_list)

if __name__ == '__main__':
    search_list(user_list)
    sort_list(user_list)
