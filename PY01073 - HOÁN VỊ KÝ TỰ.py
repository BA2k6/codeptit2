def hv(s,a):
        if len(s) ==0: #khi đã tạo xong 1 hoán vị
                print(a) #in ra 1 hoán vị
                return #trở lại hàm đệ quy trước đó
        for i in range(len(s)):
                x = s[i]     #gán biến x để tạo 1 hoán vị mới
                c = s[:i] + s[i+1:] #xoay chuỗi ký tự
                hv(c, a+x) # đệ quy để tìm hoán vị tiếp theo
s = input()
a=""
hv(s,a) #hàm đệ quy hoán vị

