for _ in range(int(input())):
    n = input()
    l = len(n)-1
    if n[0] == n[l]:
        print("YES")
    else:
        print("NO")