#cách 1
for _ in range(int(input())):
    a = int(input())
    b = str(a)
    if b[:2] == b[-2:]:
        print("YES")
    else:
        print("NO")
#cách 2
for _ in range(int(input())):
    a = input()
    b = list(a)
    if b[:2] == b[-2:]:
        print("YES")
    else:
        print("NO")