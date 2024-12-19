def check(n):
    for i in range(1, len(n)):
        if n[i] < n[i-1]:
            return "NO"
    return "YES"
for _ in range(int(input())):
    n = input()
    print(check(n))
