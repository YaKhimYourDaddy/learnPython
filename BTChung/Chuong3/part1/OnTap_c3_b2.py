n = 0
while not (n >= 1 and n <= 100):
    n = int(input("input n: "))
print("right input n = " + str(n)) # print("right input n =", n)

SoCacUoc = 0

# for i in range(1, n + 1):
#     if n % i == 0:
#         SoCacUoc += 1

i = 1
while (i <= n):
    if n % i == 0:
        SoCacUoc += 1
    i += 1

if SoCacUoc == 2:
    print(n, "is a prime number")
else:
    print(n, "is not a prime number")
