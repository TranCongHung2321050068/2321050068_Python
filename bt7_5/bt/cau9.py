def giai_cau_9(a, b, c):
    tong = a + b + c
    print(f"Tổng là: {tong}")

    dem_chan = 0
    for ky_tu in str(tong):
        if int(ky_tu) % 2 == 0:
            dem_chan += 1
            
    print(f"Số lượng chữ số chẵn trong tổng là: {dem_chan}")

# Gọi module câu 9
# giai_cau_9()