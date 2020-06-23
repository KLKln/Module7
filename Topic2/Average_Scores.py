def average_scores_args_only(*args):
    # Use *args for average calculation
    result = 0
    for x in args:
        result += x
        average = sum(args) / len(args)
        return average

    def average_scores(*args, **kwargs):
        for key, value in kwargs.items():
            print("%s == %s" % (key, value))
        #return


def place_holder(first_name, last_name, course_name):
    print('first name: ' + first_name)
    print('last_name: ' + last_name)
    print('course name: ' + course_name)
    print('test average: ' + average_scores_args_only())


    # 'Result: name = M gpa = 3.2 course = Python with current average 30.0


if __name__ == '__main__':
    average_scores_args_only(4, 2, 4, 5, 1, 3, 2, 5)
    average_scores_args_only(5, 5, 5, 5, 5)
    average_scores_args_only(1, 3, 1, 3, 1, 3)
    average_scores_args_only(4, 4, 4, )
    place_holder('george', 'ferguson', 'python')


#ky value pair
#key is first name
#value is userinput?

#first_name = 'joe'
