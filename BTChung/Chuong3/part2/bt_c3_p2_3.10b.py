# answer with while loop
n = int(input("n="))
i = 1
while i <= n:
    print(i, end = " ")
    if i % 5 == 0:
        print("") # to move onto next line
    i += 1

# # answer with for loop
# n = int(input("n="))
# for i in range(1, n + 1):
#     print(i, end = " ")
#     if i % 5 == 0:
#         print("") # to move onto next line
