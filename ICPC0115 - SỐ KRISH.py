from math import factorial
def giaithua(n):
    t = 0
    while n != 0:
        t += factorial(n%10)
        n//=10
    return t
for _ in range (int(input())):
    n = int(input())
    if n == giaithua(n):
        print("Yes")
    else:
        print("No")


