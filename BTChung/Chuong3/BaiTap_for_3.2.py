n = 0
while n < 1 or n > 50: # while not (n >= 1 and n <= 50)
    n = int(input("input n: "))
print("right input n = " + str(n)) # print("right input n =", n)

for i in range(n):
    print(i, end = " ")
    if i % 10 == 0:
        print("") # to move onto next line

