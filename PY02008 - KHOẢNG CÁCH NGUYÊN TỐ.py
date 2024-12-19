from math import isqrt
def nt(n):
    for i in range(2, isqrt(n)+1):
        if n % i == 0:
            return False
    return n >1

n, x = map(int, input().split())
a = []
b = [x]
i = 2
while len(a) < n:
    if nt(i):
        a.append(i)
    i += 1
for j in range(n):
    k = int(a[j])+int(b[j])
    b.append(k)
print(" ".join(map(str, b)))




