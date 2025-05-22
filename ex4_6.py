def computepay(h, r):
    if(h<=40):
        return h*r
    else:
        x = (h-40)*1.50*r + 40*r
        return x

hrs = input("Enter Hours:")
rate = input("Enter Rate:")
h = float(hrs)
r = float(rate)
p = computepay(h, r)
print("Pay", p)