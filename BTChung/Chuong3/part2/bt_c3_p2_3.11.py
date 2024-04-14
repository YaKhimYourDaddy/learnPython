numberOfPositiveIntegers = 0
numberOfNegativeIntegers = 0
while True:
    n = int(input())
    if n == 0:
        break
    elif n > 0:
        numberOfPositiveIntegers += 1
    else: # n < 0
        numberOfNegativeIntegers += 1
print(f"{numberOfPositiveIntegers} so duong")
print(f"{numberOfNegativeIntegers} so am")