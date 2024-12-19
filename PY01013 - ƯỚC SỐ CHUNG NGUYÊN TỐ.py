from math import gcd, isqrt
def nt(n):
    for i in range(2, isqrt(n) +1):
        if n % i ==0:
            return False
    return n >1
for _ in range(int(input())):
    a, b = map(int, input().split())
    n = str(gcd(a,b))
    t = 0
    for i in n:
        t += int(i)
    if nt(t):
        print("YES")
    else:
        print("NO")

