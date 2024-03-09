import re
p = ""
file = open('TSIS5/row.txt')
for line in file:
    line = line.rstrip()
    line = re.findall('[A-Z][^A-Z]*',line)
    if len(line) > 1:
        for i in line:
            p = p + i + " "
        print(p)
    p = ""