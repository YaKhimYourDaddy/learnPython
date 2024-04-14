def main():
    n = int(input("n="))
    m = int(input("m="))

    L1 = []

    print("L1:")
    for _ in range(n):
        L1.append(int(input()))

    L2 = []
    print("L2:")
    for _ in range(m):
        L2.append(int(input()))

    L3 = []
    for num in L1:
        if num in L2 and num not in L3:
            L3.append(num)

    print("L3:")
    print(*L3)

if __name__ == "__main__":
    main()
