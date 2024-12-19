
for i in range(int(input())): # đếm số bộ test
    kt = 0
    n=input() #dãy địa chỉ
    t=n.split(".") #chia đi chỉ thành từng phần trong list theo dấu .
    if len(t) != 4: # nếu t có khác 4 phần tử in ra NO
        print("NO")
    else:
        for i in t: # duyệt từng phần tử trong t
            if i.isdigit(): # kiểm tra xem mỗi phần tử của t có phải toàn số không
                a=int(i) #ép kiểu của phần tử trong i về dang int
                if 0 <= a and a <= 255: # điều kiện cần 2
                    kt +=1
        if kt == 4: #nếu kt = 4 tức là cả 4 phần tử đều thỏa mãn yêu cầu
             print("YES")
        else:
             print("NO")













