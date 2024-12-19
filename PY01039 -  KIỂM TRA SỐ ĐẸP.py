def check(n):
    for i in range(len(n)-2):
        if n[i] != n[i+2]:
            return False
    return True
for _ in range(int(input())):
    n = input()
    if check(n):
        print("YES")
    else:
        print("NO")






