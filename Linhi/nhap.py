def tinh_tien_dien(M1, M2, M3, S):
    sum = 0
    if S <= 100:
        sum += S * M1 # sum += ((S - 1) / 1 + 1) * M1
        return sum
    elif 100 < S <= 150:
        sum += 100 * M1 # sum += ((100 - 1) / 1 + 1) * M1
        sum += (S - 100) * M2 # sum += ((S - 101) / 1 + 1) * M2
        return sum
    else:
        sum += 100 * M1 # sum += ((100 - 1) / 1 + 1) * M1
        sum += 50 * M2 # sum += ((150 - 101) / 1 + 1) * M2
        sum += (S - 150) * M3 # sum += ((S - 151) / 1 + 1) * M3
        return sum

def main():
    # Nhập giá M1, M2, M3 và số Kw điện tiêu thụ S từ bàn phím
    M1 = int(input("Nhập giá M1 (VND/Kw): "))
    M2 = int(input("Nhập giá M2 (VND/Kw): "))
    M3 = int(input("Nhập giá M3 (VND/Kw): "))
    S = int(input("Nhập số Kw điện tiêu thụ: "))

    # Tính tổng tiền phải trả
    tong_tien = tinh_tien_dien(M1, M2, M3, S)

    # In tổng tiền ra màn hình
    print("Tổng tiền phải trả:", tong_tien, "VND")

if __name__ == "__main__":
    main()
