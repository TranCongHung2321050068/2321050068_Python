#Viết chương trình nhập vào 2 số nguyên dương m và n, sau đó tính tổng (a+b) và tìm ra chữ số lớn nhất trong tổng đó.
class tinh:
    def __init__(self):
        self.a = int(input("Nhập số nguyên dương a: "))
        self.b = int(input("Nhập số nguyên dương b: "))

    def tong(self):
        return self.a + self.b

    def chu_so_lon_nhat(self):
        tong = self.tong()
        max_digit = 0
        while tong > 0:
            digit = tong % 10
            if digit > max_digit:
                max_digit = digit
            tong //= 10
        return max_digit
c = tinh()
print("Tổng của a và b là: ", c.tong())
print("Chữ số lớn nhất trong tổng là: ", c.chu_so_lon_nhat())