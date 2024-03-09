import re
file = open('TSIS5/row.txt')
p = ""
for line in file:
    line = line.rstrip()
    if re.search('[a-z]+_[a-z]+',line):
        newline = line.split('_')
        p += newline[0]
        for i in range(1,len(newline)):
            p += newline[i][0].upper() + newline[i][1:]
        print(p)
        p = ""