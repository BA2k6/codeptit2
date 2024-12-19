from math import gcd
n = int(input())
a = [int(i) for i in input().split()]
a.sort()
for i in range(n):
    for j in range(i+1, n):
        if gcd(int(a[i]), int(a[j])) ==1:
            print(a[i], a[j])