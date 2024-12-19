from math import isqrt
def nt(n):
    for i in range(2,isqrt(n)+1):
        if n % i == 0:
            return False
    return n >1
for _ in range(int(input())):
    a = []
    n = int(input())
    for i in range(13,n):
            x = str(i)
            x1 = int(x[::-1])
            if nt(i) and nt(x1) and i != x1 and x1 < n and str(i) not in a :
                a.append(str(i))
                a.append(str(x1))
    print(" ".join(a))






