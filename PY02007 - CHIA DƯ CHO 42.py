a = []
b =[]
while len(a) < 10:
    a += list(map(int, input().strip().split()))
for i in a:
    t = i % 42
    if t not in b:
        b.append(t)
print(len(b))

