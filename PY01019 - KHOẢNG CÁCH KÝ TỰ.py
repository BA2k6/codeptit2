def kt(s1):
    n = len(s1)
    s2 =s1[::-1]
    for i in range(1,n):
        if abs(ord(s1[i])-ord(s1[i-1])) != abs(ord(s2[i])-ord(s2[i-1])):
            return False
    return True
for _ in range(int(input())):
    s1 = input().strip()
    if kt(s1):
        print("YES")
    else:
        print("NO")
