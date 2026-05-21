#viết chương trình nhập vào 1 số nguyên dương n, kiểm tra xem tích các chữ số của n có phải là số chẵn và lớn hơn 20 không?
class bai3:
    def __init__(self):
        self.n = int(input("Nhập số n: "))
    def tinh(self):
        tich = 1
        for i in str(self.n):
            tich *= int(i)
        if tich % 2 == 0 and tich > 20:
            return "Tích các chữ số của {} là {}, là số chẵn và lớn hơn 20".format(self.n, tich)
        else:
            return "Tích các chữ số của {} là {}, không thỏa mãn điều kiện".format(self.n, tich)
b = bai3()
print(b.tinh())

#
n = int(input("Nhập n: "))
tich = 1
while n > 0:
    tich *= n % 10
    n //= 10

if tich % 2 == 0 and tich > 20:
    print("Tích các chữ số là",tich, "số chẵn và lớn hơn 20")
else:
    print("Tích các chữ số là",tich, "không thỏa mãn điều kiện")