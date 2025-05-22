# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
s = 0
for line in fh:
    if line.startswith("X-DSPAM-Confidence: "):
        line = line.rstrip()
        count += 1
        s += float(line[19:])
print('Average spam confidence:',s/count)
