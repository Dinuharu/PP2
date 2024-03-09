import re
file = open('TSIS5/row.txt')
for line in file:
    line = line.rstrip()
    line = re.findall('[A-Z][^A-Z]*', line)
    if len(line) > 0:
        print(line)