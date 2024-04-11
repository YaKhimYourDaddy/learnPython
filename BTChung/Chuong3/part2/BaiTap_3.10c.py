# answer with while loop
n = int(input("n="))
line = 1
while line <= n:
    count = 1
    while count <= n:
        print(count, end = " ")
        count += 1
    print("") # to move onto next line
    line += 1

# # answer with for loop
# n = int(input("n="))
# for line in range(n):
#     for count in range(1, n + 1):
#         print(count, end = " ")
#     print("") # to move onto next line
    
