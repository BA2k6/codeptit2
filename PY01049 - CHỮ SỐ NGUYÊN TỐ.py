from math import isqrt
def nt(n):
    for i in range(2, isqrt(n)+1):
        if n % i ==0:
            return False
    return n >1
for _ in range(int(input())):
    n = input()
    d =0
    for i in n:
        if nt(int(i)):
            d += 1
    if nt(len(n)) and d > len(n) - d:
        print("YES")
    else: print("NO")

