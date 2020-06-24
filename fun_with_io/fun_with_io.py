import os as os
"""
file_dir = os.path.dirname(__file__)
file_name = "testscores.txt"
f = open(os.path.join(file_dir, file_name), "r")
line1 = f.read()
print(line1)
f.close()

f = open(os.path.join(file_dir, file_name), "r")
line1 = f.read(8)
print(line1)

f = open(os.path.join(file_dir, file_name),"r")
line = f.readline()
print(line)
f.close()

f = open(os.path.join(file_dir, file_name), "r")
line = f.readline(8)
print(line)
f.close()

f1 = open(os.path.join(file_dir, file_name), "r")
line = f1.readline(256)
print(line)
f.close()

f = open(os.path.join(file_dir, file_name), "r")
line = f.readlines()
print(line)
f.close()

f1 = open(os.path.join(file_dir, file_name), "r")
line = f1.readlines(8)
print(line)
f1.close()

f = open(os.path.join(file_dir, file_name), "r")
line = f.readline(256)
print(line)
f.close()
"""

f = open('testscores.txt', 'w')
f.write("First Line\n")
input_list = ['1\t', '3\t', '5\n']
f.writelines(input_list)
f.close()
