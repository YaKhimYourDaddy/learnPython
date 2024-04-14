n = int(input()) 
# n = int(input("input an integer 2 <= n <= 50: "))

# # ask user input n until input right value 
# n = -9999
# while not (2 <= n and n <= 50):
#     n = int(input("input an integer 2 <= n <= 50: "))

for evenNumber in range(2, n + 1, 2):
    print(evenNumber, end = " ")