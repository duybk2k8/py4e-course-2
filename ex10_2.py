fname = input("Enter file name: ")
a = open(fname)

counts = list()
cnt = list()
dic = dict()
b = list()
#count = 0
for line in a:
    if line.startswith("From"):
        line = line.rstrip()
        b = line.split()
        if(len(b) == 2):
            continue
        else:
            counts.append(b[5])
#print(counts)
for word in counts:
    word = word.split(':')
    cnt.append(word[0])
for l in cnt:
    dic[l] = dic.get(l, 0) + 1

for v, k in sorted(dic.items()):
    print(v, k)