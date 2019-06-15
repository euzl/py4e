# 연습문제 4.6
def computepay(h,r):
    h = float(h)
    r = float(r)
    if h>40:
        return h*r + (h-40)*(r*0.5)
    else :
        return h*r

hrs = input("Enter Hours:")
rs = input("Enter rates:")

p = computepay(hrs,rs)
print(p)
