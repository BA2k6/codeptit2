from math import isqrt
def nt(n):
    for i in range(2, isqrt(n)+1):
        if n % i == 0:
            return False
    return n >1
for _ in range(int(input())):
    n = input()
    x = n[-4:]
    if nt(int(x)):
        print("YES")
    else:
        print("NO")
