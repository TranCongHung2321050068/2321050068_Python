#iết chương trình nhập vào một dãy số thực x1, x2, …, xn (0 < n < 100), sau đó tìm trung bình cộng các phần tử âm trong dãy mà giá trị nằm trong khoảng (-1000, -10)
class tbc: 
    def __init__(self):
        self.n = int(input("Nhập số lượng phần tử: "))
        self.a = []
        for i in range(self.n):
            self.a.append(float(input("Nhập phần tử thứ {}: ".format(i + 1))))

    def tbc_am(self):
        tong = 0
        dem = 0
        for i in self.a:
            if i < 0 and -1000 < i < -10:
                tong += i
                dem += 1
        if dem == 0:
            return "Không có phần tử âm nào trong khoảng (-1000, -10)"
        else:
            return tong / dem
c = tbc()
print("Trung bình cộng các phần tử âm trong khoảng (-1000, -10) là: ", c.tbc_am())