# answer with for loop:
char = input() 
# char = input("input a character: ")

n = int(input()) 
# n = int(input("input an integer 1 <= n <= 20: "))

# # ask user input n until input right value 
# n = -9999
# while not (1 <= n and n <= 20):
#     n = int(input("input an integer 1 <= n <= 20: "))

for countLine in range(n):
    for countChar in range(countLine + 1):
        print(char, end = "")
    print("") # to move onto next line


# #answer with while loop:
# char = input() # char = input("input a character: ")
# n = int(input()) # n = int(input("input an integer 1 <= n <= 20: "))
# countLine = 1
# while countLine <= n:
#     countChar = 1
#     while countChar <= countLine:
#         print(char, end = "")
#         countChar += 1
#     countLine += 1
#     print("") # to move onto next line

