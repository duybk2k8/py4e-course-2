fname = input("Enter file name: ")
a = open(fname)
b = a.read()
c = b.split()
l = list()
for line in c:
    if line in l:
        continue
    else:
        l.append(line)
l.sort()
print(l)
    
    

