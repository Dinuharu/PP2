import re
file = open('TSIS5/row.txt')
for line in file:
    line = line.rstrip()
    condition = re.findall('[A-Z][a-z]+', line)
    if len(condition) == 1:
        print(condition)
