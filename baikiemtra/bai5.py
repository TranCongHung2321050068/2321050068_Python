#viết chg trình nhập 2 số nguyên dương m,n kiểm tra xem m có chia hết tổng chữ số của n không?
class bai5:
    def __init__(self):
        self.m = int(input("Nhập số nguyên dương m: "))
        self.n = int(input("Nhập số nguyên dương n: "))
    def tinh(self):
        tong = 0
        for i in str(self.n):
            tong += int(i)
        if self.m % tong == 0:
            return "{} chia hết tổng chữ số của {} là {}".format(self.m, self.n, tong)
        else:
            return "{} không chia hết tổng chữ số của {} là {}".format(self.m, self.n, tong)
b = bai5()
print(b.tinh())

#
m = int(input("Nhập m: "))
n = int(input("Nhập n: "))
tong = 0
temp = n
while temp > 0:
    tong = tong + temp % 10
    temp //= 10
if m % tong == 0:
    print(f"{m} chia hết cho tổng của chữ số {n} là {tong}")
else:
    print(f"{m} không chia hết cho tổng của chữ số {n} là {tong}")