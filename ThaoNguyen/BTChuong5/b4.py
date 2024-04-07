def reverse_list(A):
    B = []
    for i in range(len(A) - 1, -1, -1):
        B.append(A[i])
    return B

def sort_list(B):
    n = len(B)
    for i in range(n):
        for j in range(0, n-i-1):
            if B[j] > B[j+1]:
                B[j], B[j+1] = B[j+1], B[j]

n = int(input("n="))
A = []
for _ in range(n):
    A.append(int(input()))
B = reverse_list(A)
for item in B:
    print(item, end=" ")
print() # để xuống dòng
sort_list(B)
for item in B:
    print(item, end=" ")