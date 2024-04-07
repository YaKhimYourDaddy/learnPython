import numpy as np

def main():
    M = int(input("Nhập kích thước của ma trận (MxM): "))
    K = int(input("Nhập số mũ K (K < 1000): "))

    # Nhập ma trận A
    print("Nhập ma trận A:")
    A = []
    for i in range(M):
        row = list(map(int, input().split()))
        A.append(row)
    A = np.array(A)

    # Tính ma trận B = A^k
    B = np.linalg.matrix_power(A, K)

    # Xuất ma trận B
    print("Ma trận B:")
    print(B)

if __name__ == "__main__":
    main()
