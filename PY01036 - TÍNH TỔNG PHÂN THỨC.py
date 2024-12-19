for _ in range (int(input())):
    n = int(input())
    t = 0
    if n % 2 != 0:
        for i in range(1,n+1,2):
            t += 1/i
    else:
        for i in range(2,n+1,2):
            t+=1/i
    print(f"{t:.6f}")

