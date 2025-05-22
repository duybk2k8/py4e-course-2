num = 0
total = 0
while True:
    a = input('Enter a number: ')
    try:
        b = float(a)
        num += 1
        total += b
    except:
        if a == 'done':
            break
        else:
            print('Invalid input')
            continue
print(total, num, total/num)
    
    