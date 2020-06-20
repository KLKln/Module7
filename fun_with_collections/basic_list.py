
def make_list():
    user_num = []
    user_number = get_input()
    print('a is set to:', 5)
    while True:
        try:
            for x in range(2):
                user_number
                if user_number.isdigit():
                    user_num.append(user_number)
                    break
                else:
                    raise TypeError
        except TypeError:
            print('Numbers only please.')
            continue

    return user_num


def get_input():


    pass

