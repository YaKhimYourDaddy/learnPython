# for dong in range(1, 9 + 1): # cac dong tu 1 toi 9
#     for DauCach in range(1, 9 - dong + 1):
#         print(" ", end = "")
#     for DauSao in range(1, dong * 2 - 1 + 1):
#         print("*", end = "")
#     print("")

for dong in range(9): # cac dong tu 0 toi 8
    for DauCach in range(8 - dong):
        print(" ", end = "")
    for DauSao in range(dong * 2 + 1):
        print("*", end = "")
    print("")