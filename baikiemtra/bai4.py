#Viết chg trình nhập 2 số nguyên dương a ,b.Tính tổng a+b và in ra chữ số lớn nhất trong tổng đó
class bai4:
    def __init__(self):
        self.a = int(input("Nhập số nguyên dương a: "))
        self.b = int(input("Nhập số nguyên dương b: "))
    def tinh(self):
        tong = self.a + self.b
        max_digit = max(str(tong))
        return "Tổng của {} và {} là {}, chữ số lớn nhất trong tổng là {}".format(self.a, self.b, tong, max_digit)
b = bai4()
print(b.tinh())

#
a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
s = a + b
max = 0
while s > 0:
    temp = s % 10
    if temp > max:
        max = temp
    s //= 10
print("Chữ số lớn nhất là ", max)