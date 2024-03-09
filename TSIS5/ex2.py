import re
file = open('TSIS5/row.txt')
for line in file:
    line = line.rstrip()
    if re.search('abb',line) or re.search('abbb',line):
        print(line)