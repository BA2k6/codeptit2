from math import isqrt
def nt(n):
    for i in range(2, isqrt(n)+1):
        if n % i ==0:
            return False
    return n > 1
for _ in range(int(input())):
    n = input()
    t = 0
    for i in n:
        t += int(i)
    d =0
    for i in range(len(n)):
        if i %2 ==0 and int(n[i]) %2 != 0:
            d += 1
        if i %2 != 0 and int(n[i]) % 2 == 0:
            d += 1
    if nt(t) and d == 0:
        print("YES")
    else:
        print("NO")