from math import isqrt
def nt(n):
    for i in range(2, isqrt(int(n))+1):
        if int(n) % i == 0:
            return False
    return int(n) > 1
for _ in range(int(input())):
    n = input()
    d = 0
    for i in range(len(n)):
        if nt(str(i)) and nt(n[i]):
            d+=1
        elif (not nt(str(i))) and (not nt(n[i])):
            d += 1
    if d == len(n):
        print("YES")
    else:
        print("NO")




