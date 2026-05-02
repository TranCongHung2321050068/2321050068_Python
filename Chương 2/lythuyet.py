#2.1. if:
#Nhập  3 số nguyên, tìm số max,min trong 3 số đó:
a = int(input("nhập a: "))
b = int(input("nhập b: "))  
c = int(input("nhập c: "))
max = a
if b > max:
    max = b
if c > max:
    max = c
print("số lớn nhất là: ", max)
#cmtt với min.
# 2.1.2. if-else:
#Nhập 1 số nguyên, kiểm tra xem số đó là chẵn hay lẻ:
n = int(input("nhập n: "))
if n % 2 == 0:
    print("%d là số chẵn" %n)
else:
    print("%d là số lẻ" %n)
#GPT bậc nhất ax + b = 0
a = int(input("nhập a: "))
b = int(input("nhập b: "))
if a == 0:
    if b == 0:
        print("phương trình vô số nghiệm")
    else:
        print("phương trình vô nghiệm")
else:
    x = -b/a
    print("phương trình có nghiệm x = %.2f" %x)
#Nhập 2 số và ktra ><=:
a = int(input("nhập a: "))
b = int(input("nhập b: "))
if a > b:
    print("%d > %d" %(a,b))
elif a < b:
    print("%d < %d" %(a,b))
else:
    print("%d = %d" %(a,b))
#2.1.3 if elif else:
#Nhập mã dân tộc và hiển thị:
ma = input("nhập mã dân tộc: ")
if ma == 1:
    print("dân tộc Kinh")
elif ma == 2:
    print("dân tộc Tày")
elif ma == 3:
    print("dân tộc Nùng")
elif ma == 4:
    print("dân tộc Thái")
elif ma == 5:
    print("dân tộc Khmer")
else:
    print("kco mã tương ứng")
#2.2 while:
#Tính tổng các số 1,2,...,n:
n = int(input("nhập n: "))
s = 0
i = 1
while i <= n:
    s += i
    i += 1
print("tổng là: ", s)
#break, continue, pass:
var = 10
while var > 0:
    print("giá trị hiện tại: ", var)
    var -= 1
    if var == 5:
        break

var  = 5
while var > 0:
    var -= 1
    if var == 3:
        continue
    print("giá trị hiện tại: ", var)

i = 1
while i <= 10:
    if i % 2 == 0:
        pass
    else:
        print("giá trị hiện tại: ", i)
    i += 1

#BT: Nhập 3 điểm toán, lý, hóa. Tính điểm trung bình và xếp loại: với <5: yếu, 5-6.5: trung bình, 6.5-8: khá, >8: giỏi.
toan = float(input("nhập điểm toán: "))
ly = float(input("nhập điểm lý: "))
hoa = float(input("nhập điểm hóa: "))
dtb = (toan + ly + hoa)/3
if dtb < 5:
    print("xếp loại yếu")
elif dtb < 6.5:
    print("xếp loại trung bình")
elif dtb < 8:
    print("xếp loại khá")
else:
    print("xếp loại giỏi")

#2BTVN: file riêng

#2.3 For:
#Tính tổng các số 1,2,...,n:
n = int(input("nhập n: "))
s = 0
for i in range(1, n+1):
    s += i
print("tổng là: ", s)
#tính tổng dãy số bất kỳ:
n = int(input("nhập dãy: "))
s = 0
a=[]
for i in range(n):
    x = int(input("nhập số thứ " + str(i+1) + ": "))
    a.append(x)
for i in a:
    s += i
print("tổng là: ", s)
#nhập và in ma trận:
m = int(input("nhập số dòng: "))
n = int(input("nhập số cột: "))
for i in range(m):
    for j in range(n):
        x = int(input("nhập phần tử thứ [" + str(i) + "][" + str(j) + "]: "))
        print(x, end = " ")
    print()
#nhập vào 1 xâu ký tự với mỗi ký tự trên 1 dòng
s = input("nhập xâu: ")
for i in range(len(s)):
    print(s[i])
    i += 1

#cách 2:
s = "CNTT"
i=0
while i < len(s):
    print(s[i])
    i += 1
#nhập 1 số và ktra số đó có phải số hoàn hảo không
n = int(input("nhập n: "))
s = 0
for i in range(1, n/2 + 1):
    if n % i == 0:
        s += i
    if s == n:
        print("%d là số hoàn hảo" %n)
    else:
        print("%d không phải là số hoàn hảo" %n)
#ktra 1 xâu ký tự xem có bnh ktu là số và bnh ktu là chữ, nếu ktdb thì thoát:
s = input("nhập xâu: ")
dem_so = 0
dem_chu = 0
for i in s:
    if i.isdigit():
        dem_so += 1
    elif i.isalpha():
        dem_chu += 1
    else:
        print("xâu có ký tự đặc biệt, thoát chương trình")
        exit()
print("số ký tự là số: ", dem_so)
print("số ký tự là chữ: ", dem_chu)
#cho A[1,2,3], B[4,5,6]. Tạo C là hợp của A&B:
A = [1,2,3]
B = [4,5,6]
C=[]
for i in A:
    C.append(i)
for i in B:
    C.append(i)
print("hợp của A và B là: ", C)
