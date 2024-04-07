def main():
    A = []
    for i in range(10):
        A.append(int(input()))

    for i in range(0, 10 - 1, 2):
        A[i], A[i + 1] = A[i + 1], A[i]

    print(*A)

if __name__ == "__main__":
    main()
