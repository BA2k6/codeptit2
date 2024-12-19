
def check(n):
    if len(n) % 2 ==1  or n != n[::-1] :
        return False
    for i in n:
            if int(i) % 2 != 0:
                return False
    return True
for _ in range(int(input())):
    n = int(input())
    for i in range(22, n,2):
        x = str(i)
        if check(x):
                print(i, end = " ")
    print()


