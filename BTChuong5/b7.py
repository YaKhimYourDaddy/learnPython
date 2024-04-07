def main():
    n = int(input("Nhập số nguyên n: "))
    
    L = []
    for i in range(n):
        L.append(int(input()))

    M = []
    for item in L:
        if item not in M:
            M.append(item)

    print(*M)

if __name__ == "__main__":
    main()
