
def make_list():
    user_num = []
    user_number = get_input()
    try:
        for i in range(0,3):
            user_number
            if user_number.isdigit():
                user_num.append(int(user_number))
            else:
                raise TypeError
    except TypeError:
        print('Numbers only please.')


    return user_num


def get_input():


    pass

