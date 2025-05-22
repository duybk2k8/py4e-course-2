fname = input("Enter file name: ")
a = open(fname)
count = 0
for line in a:
    if line.startswith("From"):
        line = line.rstrip()
        b = line.split()
        if(len(b) == 2):
            continue
        else:
            print(b[1])
            count += 1
                

print("There were", count, "lines in the file with From as the first word")



#len=2 => continue
#len /= 2 => split => lấy giá trị thứ 2 => in + count