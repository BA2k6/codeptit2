n = int(input())
d =0
a = [int(i) for i in input().split()]
for j in range(1,len(a)):
    if a[j] != a[j-1]:
        d += 1
print(d)