n, k = map(int, input().split())
a = list(map(int, input().split()))
b = []
for i in a:
    if i not in b:
        b.append(i)
b.sort()
for i in