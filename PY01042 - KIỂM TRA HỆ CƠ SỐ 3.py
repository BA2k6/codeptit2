def check(x):
    for i in x:
        if i != "0" and i != "1" and i != "2":
            return False
    return True
for _ in range(int(input())):
    x = input()
    if check(x):
        print("YES")
    else:
        print("NO")
