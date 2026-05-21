#iết chương trình nhập vào một dãy số thực x1, x2, …, xn (0 < n < 100), sau đó tìm trung bình cộng các phần tử dương trong dãy mà giá trị nằm trong khoảng (0, 1000)
class tbc: 
    def __init__(self):
        self.n = int(input("Nhập số lượng phần tử: "))
        self.a = []
        for i in range(self.n):
            self.a.append(float(input("Nhập phần tử thứ {}: ".format(i + 1))))

    def tbcd(self):
        tong = 0
        dem = 0
        for i in self.a:
            if 0 < i < 1000:
                tong += i
                dem += 1
        if dem == 0:
            return "Không có phần tử dương nào trong khoảng (0,1000)"
        else:
            return tong / dem
c = tbc()
print("Trung bình cộng các phần tử dương trong khoảng (0,1000) là: ", c.tbcd())

#thuật toán:
n = int(input("Nhập số lượng dãy: "))

tong = 0
dem = 0

for i in range(n):
    x = int(input("Nhập số: "))

    if 0 < x < 1000:
        tong += x
        dem += 1

if dem > 0:
    print("Trung bình cộng của dãy: ", tong/dem)
else:
    print("TBC là:",tong/dem, "Không TM điều kiện")