def average_scores_args_only(*args):
    # Use *args for average calculation
    result = 0
    for x in args:
        result += x
        average = sum(args) / len(args)
        return round(average, 2)


def average_scores(*avg, **kwargs):
    fir_nam = ''
    la_name = ''
    fu_name = ''
    crse = ''
    result = 0
    for x in avg:
        result += x
        average = round(sum(avg) / len(avg), 2)
    for key, value in kwargs.items():
        if key == 'first_name':
            first_name = fir_nam
        if key == 'last_name':
            last_name = la_name
            full_name = la_name, fir_nam
        if key == 'course':
            course = crse
        if key == 'gpa':
            average = average_scores_args_only()
        return print("%s == %s" % (key, value))



#average_scores(gpa = {4, 4, 3, 2, 3, 4, 4}, first_name = 'Kelly', last_name = 'Klein', course = 'python')

# def student_average(average_scores())
# 'Result: name = M gpa = 3.2 course = Python with current average 30.0


if __name__ == '__main__':
    average_scores(first_name='Kelly', last_name='Klein', course='python',
                   gpa=(4, 4, 3, 2, 3, 4, 4))

# ky value pair
# key is first name
# value is userinput?

# first_name = 'joe'
