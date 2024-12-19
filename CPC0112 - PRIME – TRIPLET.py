from math import isqrt
def nt(n):
    for i in range(2, isqrt(n)+1):
        if n % i == 0:
            return False
    return True
for _ in range(int(input())):
    d =0
    x = int(input())
    for p in range(2, x-6):
        if nt(p) and nt(p+2) and nt(p+6):
            d +=1
        if nt(p) and nt(p+4) and nt(p+6):
            d +=1
    print(d)


