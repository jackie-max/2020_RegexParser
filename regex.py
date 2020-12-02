import re

file_in = open('input.txt', 'r')
file_out = open('output.txt', 'w')
line = file_in.readline()
name_type = {}
name_var = {}
while line:
    result = re.match(r'(int |short |long )?([a-zA-Z][a-zA-Z0-9]{0,15}):=(([a-zA-Z][a-zA-Z0-9]{0,15})|[0-9]+) ([+|-|*|/]) (([a-zA-Z][a-zA-Z0-9]{0,15})|[0-9]+)', line)
    if result:
        file_out.write('valid\n')
        name_type = re.match(r'(int |short |long)?', line)
        name_var = re.match(r'([a-zA-Z][a-zA-Z0-9]{0,15})', line)
    else:
        file_out.write('invalid')
    line = file_in.readline()
print(name_var)
print(name_type)
file_in.close()
file_out.close()
