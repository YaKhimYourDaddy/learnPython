# n = int(input("input an integer 0 <= n <= 9999: "))

# # ask user input n until input right value 
# n = -9999
# while not (2 <= n and n <= 50):
#     n = int(input("input an integer 0 <= n <= 9999: "))

n = int(input())
nString = str(n)

# answer with for loop and if
for char in nString:
    if char == '0':
        print('A', end = "")
    elif char == '1':
        print('B', end = "")
    elif char == '2':
        print('C', end = "")
    elif char == '3':
        print('D', end = "")
    elif char == '4':
        print('E', end = "")
    elif char == '5':
        print('F', end = "")
    elif char == '6':
        print('G', end = "")
    elif char == '7':
        print('H', end = "")
    elif char == '8':
        print('K', end = "")
    elif char == '9': # else: cũng được vì ép từ int sang str nên chỉ có thể là chữ số
        print('L', end = "")

# # answer with while loop access each character in string 
# # and use ASCII to avoid many if conditions 
# # (have not been shown in slides yet)
# i = 0
# while i < len(nString):
#     char = chr(ord('A') + ord(nString[i]) - ord('0'))
#     print(char, end = "")
#     i += 1