while True:
    n = int(input()) # n = int(input("n = "))
    if n < 0:
        break
    elif n == 0:
        result = 1
    elif n > 0:
        result = 1
        for i in range(1, n + 1):
            result *= i
    print(result) # print(f"{n}! = {result}")


# # shorter way to write if condition in this problem:
# while True:
#     n = int(input())
#     if n < 0:
#         break
#     result = 1
#     if n > 0:
#         result = 1
#         for i in range(1, n + 1):
#             result *= i
#     else: # result = 1 by default for case n == 0 so no need this else block
#         result = 1
#     print(result)



