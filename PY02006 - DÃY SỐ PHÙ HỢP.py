def check(a, b):
    for i in range(len(a)):
        if a[i] > b[i]:
            return False
    return True
for _ in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    a.sort()
    b = [int(i) for i in input().split()]
    b.sort()
    if check(a, b):
        print("YES")
    else:
        print("NO")
