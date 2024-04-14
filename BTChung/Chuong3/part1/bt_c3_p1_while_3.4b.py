# cách chỉ dùng while
dong = 1
while dong <= 9:
    DauCach = 1 # để xác định số dấu cách đã in ra trên mỗi dòng
    while DauCach <= 9 - dong:
        print(" ", end = "") # in xong dấu cách thì in tiếp
        DauCach += 1
    
    DauSao = 1 # để xác định số dấu sao đã in ra trên mỗi dòng
    while DauSao <= 2 * dong - 1:
        print("*", end = "")
        DauSao += 1

    print("") # để xuống dòng tiếp theo
    dong += 1