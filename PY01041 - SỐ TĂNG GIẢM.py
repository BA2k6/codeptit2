def kt(n):
    if len(n) <3 :
        return False
    i = 1
    while i < len(n) and n[i] > n[i-1]:
        i += 1
    if i == 1 or i == len(n):
        return False
    while i < len(n)  and n[i] < n[i - 1]:
        i+=1
    return i == len(n)
for _ in range(int(input())):
    n = input().strip()
    if kt(n):
        print("YES")
    else:
        print("NO")



