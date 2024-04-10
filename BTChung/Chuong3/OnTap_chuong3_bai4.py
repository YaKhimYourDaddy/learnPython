while True:
    # Nhập hai số thực từ bàn phím
    a = float(input("a = "))
    b = float(input("b = "))
    
    # Nhập toán tử từ bàn phím
    operator = input("Nhập toán tử (+, -, *, /): ")
    
    # Thực hiện phép tính tương ứng
    if operator == '+':
        result = a + b
    elif operator == '-':
        result = a - b
    elif operator == '*':
        result = a * b
    elif operator == '/':
        # Kiểm tra chia cho 0
        if b == 0:
            print("Lỗi: Không thể chia cho 0.")
            continue
        result = a / b
    else:
        print("Lỗi: Toán tử không hợp lệ.")
        continue
    
    # In kết quả
    print("{} {} {} là: {}".format(a, operator, b, result))
    
    command = input("Nhập 't' hoặc 'T' để kết thúc: ")
    # Kiểm tra nếu là kết thúc
    if command == 't' or command == 'T':
        print("Kết thúc chương trình.")
        break
