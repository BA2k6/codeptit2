n = int(input())
t = 0
def check(x):
    for j in x:
        if j !="4" and j !="7":
            return "NO"
    return "YES"
while n>0:
    x= input()
    print(check(x))
    n-=1
