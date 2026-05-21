#viết chương trình nhập vào 1 số nguyên dương n, kiểm tra xem tổng các chữ số của n có phải là số chia hết cho 3 không?
class bai2: 
    def __init__(self):
        self.n = int(input("Nhập số n: "))
    def tinh(self):
        tong = 0
        for i in str(self.n):
            tong += int(i)
        if tong % 3 == 0:
            print("Tổng các chữ số của {} là {}, chia hết cho 3".format(self.n, tong))
        else:
            print("Tổng các chữ số của {} là {}, không chia hết cho 3".format(self.n, tong))
b = bai2()
print(b.tinh())

#đơn giản: 
n = int(input("Nhập n: "))
tong = 0
while n>0:
    tong += n%10
    n //= 10
if tong % 3 ==0:
    print("Tổng các chữ số chia hết cho 3")
else:
    print("Tổng các chữ số không chia hết cho 3")