from math import isqrt
def nt(n):
    for i in range(2, isqrt(n)+1):
        if n % i == 0:
            return False
    return n >1
for _ in range(int(input())):
    n = input()
    n1= n[::-1]
    t = 0
    d =0
    for i in n:
        t += int(i)
        if nt(int(i)):
            d += 1
    if nt(int(n)) and nt(int(n1)) and nt(t) and d == len(n):
        print("Yes")
    else:
        print("No")



