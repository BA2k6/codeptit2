n = int(input())
a = list(map(float, input().split()))
a.sort()
b=[]
for i in range(1,len(a)-1):
    if a[i] != a[0] and a[i] != a[len(a)-1]:
        b.append(a[i])
tb = sum (b)/len(b)
print('{:.2f}'.format(tb))