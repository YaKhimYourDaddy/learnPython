n = -999999
while not (n >= 0 and n <= 100):
    n = int(input("input n: "))
print("right input n = " + str(n))

# if n == 0:
#     result = 0
# else:
#     result = 1
#     for i in range(1, n + 1):
#         result *= i

if n == 0:
    result = 0
else:
    result = 1
    i = n
    while i > 1:
        result *= i
        i -= 1

    
print(f"{n}! = {result}")



