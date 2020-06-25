"""
Program: tuple_io.py
Author: Kelly Klein
Last date modified: 6/24/2020
This program will take an *arg and **kwarg and return a string with the given information.
"""
def average_scores_args_only(*args):
    # Use *args for average calculation
    result = 0
    for x in args:
        result += x
        average = sum(args) / len(args)
        return round(average, 2)


def average_scores(*avg, **kwargs):
    result = 0
    for x in avg:
        result += x
        average = round(sum(avg) / len(avg), 2)

    for key, value in kwargs.items():
        if key == 'gpa':
            average_scores_args_only()
        if key == 'first_name':
            first_name='Michelle'
            print("%s == %s" % (key, value))
        if key == 'last_name':
            last_name='Ruse'
            print("%s == %s" % (key, value))
        if key == 'course':
            course='World_domination'
            print("%s == %s" % (key, value))






# 'Result: name = M gpa = 3.2 course = Python with current average 30.0


if __name__ == '__main__':
    average_scores(average_scores_args_only(4, 4, 3, 2, 3, 4, 4), first_name='Kelly', last_name='Klein', course='python')
    #average_scores(gpa=(4, 3, 4, 2, 4, 2), first_name='kelly', last_name='klein', course='python')
# ky value pair
# key is first name
# value is userinput?

# first_name = 'joe'
