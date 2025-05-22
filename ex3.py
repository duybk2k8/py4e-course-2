hrs = input("Enter Hours:")
rate = input("Enter Rate:")
try:
    h = float(hrs)
    r = float(rate)
except:
    print("error")
    quit()
if h<=40:
    print(h*r)
else:
    print((h-40)*r*1.5 + 40*r)