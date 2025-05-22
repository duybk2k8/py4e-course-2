import re
fname = input("Enter file name: ")
hand = open(fname)
count = 0
numlist = list()
for line in hand:
    line = line.rstrip()
    stuff = re.findall('([0-9]+)', line)
    for i in stuff:
        count += float(i)

print(count)