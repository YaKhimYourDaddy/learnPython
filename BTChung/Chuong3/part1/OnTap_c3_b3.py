n = -999999
while not n >= 0:
    n = int(input("input n: "))
print("right input n = " + str(n))

SoChuSo = 1
cloneN = n
while cloneN / 10 > 0: # cloneN still have more than 1 digit
    cloneN /= 10
    SoChuSo += 1

print(f"{n} has f{SoChuSo} digits")

