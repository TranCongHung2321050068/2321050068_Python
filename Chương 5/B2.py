#Viết chương trình nhập vào một dãy số nguyên x1, x2, …, xn (0 < n < 200), tính tổng các phần tử chẵn trong dãy, và kiểm tra xem tổng này có chia hết cho 7 và nhỏ hơn 200 hay không
class tinhsochan:
    def __init__(self):
        self.n = int(input("Nhập số lượng phần tử: "))
        self.a = []
        for i in range(self.n):
            self.a.append(int(input("Nhập phần tử thứ {}: ".format(i + 1))))

    def tong_so_chan(self):
        tong = 0
        for i in self.a:
            if i % 2 == 0:
                tong += i
        return tong

    def kiem_tra(self):
        tong_chan = self.tong_so_chan()
        if tong_chan % 7 == 0 and tong_chan < 200:
            return "Tổng các phần tử chẵn là {} và nó chia hết cho 7 và nhỏ hơn 200".format(tong_chan)
        elif tong_chan % 7 == 0 and tong_chan > 200:
            return "Tổng các phần tử chẵn là {} và nó chia hết cho 7 nhưng không nhỏ hơn 200".format(tong_chan)
        elif tong_chan % 7 != 0 and tong_chan < 200:
            return "Tổng các phần tử chẵn là {} và nó không chia hết cho 7 và nhỏ hơn 200".format(tong_chan)
        else:
            return "Tổng các phần tử chẵn là {} và nó không chia hết cho 7 và không nhỏ hơn 200".format(tong_chan)
c = tinhsochan()
print(c.kiem_tra())