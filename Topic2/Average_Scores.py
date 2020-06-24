
def average_scores_args_only(*args):
    # Use *args for average calculation
    result = 0
    for x in args:
        result += x
        average = sum(args) / len(args)
        return average


def average_scores(*avg, **kwargs):
    result = 0
    for x in avg:
        result += x
        average = sum(avg) / len(avg)
        return average
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))


# 'Result: name = M gpa = 3.2 course = Python with current average 30.0


if __name__ == '__main__':
    kelly = {'Name': 'kelly', 'course': 'Python', 'gpa': average_scores_args_only(4, 3, 4, 4)}
    leslie = {'Name': 'leslie', 'course': 'Database Design', 'gpa': average_scores_args_only(3, 2, 3, 4, 3.5, 2, 4, 3)}
    shep = {'Name': 'shep', 'course': 'Java 2', 'gpa': average_scores_args_only(3, 4, 2.5, 4.2, 3.2, 1)}
    average_scores(**kelly)
    average_scores(**leslie)
    average_scores(**shep)
    #print(average_scores((4,3,3,4, name = )))

#ky value pair
#key is first name
#value is userinput?

#first_name = 'joe'
