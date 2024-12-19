# cách 1
import ntpath

if __name__ == "__main__":
    P = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
    while True:
        try:
            k,s = input().split()
            k = int(k)
            x = str()
            for i in range(len(s)):
                x += P[(P.index(s[i])+ k) % 28]
            print(x[::-1])
        except:
            break
# cách 2
P = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
while True:
    x = input() # input
    if x == "0": # nhập vào 0 thì thoát khỏi input
        break
    k, s = x.split() #tạo 1 list gồm k và s
    n =""
    for i in s:
        d = 0 # vị trí của phần tử i trong P
        for j in P:
            if i ==j: # phần tử trong s giống trong P
                break
            d += 1 # nếu phần tử trong s khác trong P thì d +1
        d = (d+ int(k)) %28 #vị trí kí tự theo yêu cầu
        n = P[d] + n # kí tự tạo sau chèn lên trước (đảo ngược thứ tự cữ cái)
    print(n)
