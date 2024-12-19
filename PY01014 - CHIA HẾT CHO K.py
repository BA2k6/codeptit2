a, K, N = map(int, input().split())
d =0
for i in range(K - a%K, N - a +1, K):
        print(i, end = " ")
        d += 1
if d == 0:
    print("-1")
