n = int(input())
x = [int(i) for i in input().split()]
d = 0
for i in range(len(x)-1):
    for j in range(i+1,len(x)):
        if x[i] > x[j]:
            d += 1
print(d)
