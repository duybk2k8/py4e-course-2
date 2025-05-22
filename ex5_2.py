largest = None
smallest = None
while True:
    a = input('Enter a number: ')
    try:
        b = int(a)
        if largest is None:
            largest = b
        elif largest < b:
            largest = b
        if smallest is None:
            smallest = b
        elif smallest > b:
            smallest = b
            
    except:
        if a == 'done':
            break
        else:
            print('Invalid input')
            continue
print('Maximum is', largest)
print('Minimum is', smallest)
    
    