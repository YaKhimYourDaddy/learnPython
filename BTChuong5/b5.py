def sumOfItemsAtEvenIndex(A):
    sum = 0
    n = len(A)
    for i in range(n):
        if i % 2 == 0:
            sum += A[i]
    return sum

n = int(input("n="))
A = []
for _ in range(n):
    num = int(input())
    A.append(num)
    
sum = sumOfItemsAtEvenIndex(A)
print("Tong=", sum)