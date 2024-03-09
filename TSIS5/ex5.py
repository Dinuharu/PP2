import re
file = open('TSIS5/row.txt')
for line in file:
    line = line.rstrip()
    if re.search('a.+b$',line):
        print(line)