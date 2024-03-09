import re
file = open('TSIS5/row.txt')
for line in file:
    line = line.rstrip()
    line = re.sub('[., ]',':',line)
    print(line)