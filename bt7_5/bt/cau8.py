def giai_cau_8(x, y, z):
    tich = x * y * z
    print(f"Tích là: {tich}") 

    chuoi_tich = str(tich)
    print(f"Số lượng chữ số: {len(chuoi_tich)}")

    max_chu_so = 0
    for ky_tu in chuoi_tich:
        so = int(ky_tu)
        if so > max_chu_so:
            max_chu_so = so
            
    print(f"Chữ số lớn nhất là: {max_chu_so}")

# Gọi module câu 8
# giai_cau_8()