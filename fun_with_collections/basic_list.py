def get_input():
    user_input = input(print('Enter a positive number to add to the list: '))
    return user_input


def make_list():
    user_list = []

    for i in range(0, 3):
        try:
            user_number = get_input()
            if user_number.isalpha():
                raise TypeError
            else:
                user_list.append(int(user_number))
        except TypeError:
            print('Numbers only please.')
    return user_list


if __name__ == '__main__':
    make_list()
