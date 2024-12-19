from math import isqrt
def chan_le(n):
    for i in range(len(n)):
        if i % 2 == 0 and int(n[i]) % 2 ==0:
            return True
        elif i % 2 != 0 and int(n[i]) % 2 != 0:
            return True
        else:
            return False
def nt(t):
    for i in range (2, isqrt(t)+1):
        if t % i == 0:
            return False
    return t >1
for _ in range(int(input())):
    n = input()
    t = 0
    for i in n:
        t += int(i)
    if chan_le(n) and nt(t):
        print("YES")
    else:
        print("NO")

