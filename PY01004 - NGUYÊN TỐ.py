from math import *
def nt(x):
    for i in range(2,isqrt(x)+1):
        if x % i == 0: return False
    return x>1
for i in range(int(input())):
    n=int(input())
    K = 0
    for z in range(1, n):
        if  gcd(z, n) == 1:
            K += 1
    if nt(K):
        print("YES")
    else: print("NO")

