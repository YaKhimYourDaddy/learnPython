def main():
    m = int(input("m="))
    n = int(input("n="))

    A = []
    print("A:")
    for i in range(m):
        row = []
        for j in range(n):
            row.append(int(input()))
        A.append(row)

    B = []
    print("B:")
    for i in range(m):
        row = []
        for j in range(n):
            row.append(int(input()))
        B.append(row)

    C = []
    for i in range(m):
        row = []
        for j in range(n):
            row.append(A[i][j] + B[i][j])
        C.append(row)

    print("C:")
    # for row in C:
    #     print(" ".join(map(str, row)))
    for row in C:
        row_str = ""
        for num in row:
            row_str += str(num) + " "
        print(row_str.rstrip()) #rstrip để bỏ dấu cách dư ra cuối cùng

if __name__ == "__main__":
    main()
