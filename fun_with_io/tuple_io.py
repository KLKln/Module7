import os as os
"""
Program: tuple_io.py
Author: Kelly Klein
Last date modified: 6/24/2020
This program will take input from user for student name and test scores and 
    write them to a file, and print them back.
"""

"""
f = open('testscores.txt', 'w')
f.write("First line")
input_list = ['5',\t '3'\t, '5'\n]
f.writelines(input_list)
f.close()
"""



def write_to_file(student_name_and_scores):
    #Open the file for appending (name your file 'student_info.txt')
    f = open('student_info.txt', 'w')
    #Write the tuple on one line (include any newline characters necessary)
    f.write(student_name_and_scores)
    #input_list = [student_scores]
    #f.writelines(input_list)
    #Close the file
    f.close()


def get_student_info(*args, **student_name):
    student_scores = []
    #Accepts a keyword argument for a student name
    **student_name = input('Please enter students name: ')
    #Prompts the user to input as many test scores as they wish
    for arg in args:
        student_scores = input('Please enter test scores, as many as you like: ')
    #Stores the information (name and scores) in a tuple
    student_name_and_scores = student_name, student_scores
    #Calls the function write_to_file() sending the tuple to be written to the end of the file
    write_to_file(student_name_and_scores)
    pass

def read_from_file():
    #Reads a file line by line
    #Prints each line to the console

    pass


if __name__ == '__main__':
    write_to_file()
