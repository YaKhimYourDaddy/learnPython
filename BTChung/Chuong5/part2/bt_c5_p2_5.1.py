def Input():
    n = int(input("n="))

    L = []
    for _ in range(n):
        L.append(int(input()))

    x = int(input("x="))

    return L, x

def FirstAndLast(L):
    new_list = [L[0], L[-1]]
    print(new_list)
    return new_list

def Search(L, x):
    if x in L:
        return True
    else:
        return False

def main():
    # Nhập dữ liệu từ hàm Input()
    L, x = Input()

    # Gọi hàm FirstAndLast() và in danh sách mới chỉ gồm phần tử đầu tiên và cuối cùng của L
    new_list = FirstAndLast(L)

    # Kiểm tra x có trong L hay không và in kết quả ra màn hình
    print(Search(L, x))

if __name__ == "__main__":
    main()
