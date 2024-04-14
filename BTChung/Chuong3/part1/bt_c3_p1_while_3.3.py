row = 1
while row <= 9:
    column = 1
    while column <= 9:
        result = row * column

        # add a space to format the table for better look
        if result < 10:
            print(" ", end = "") 

        print(result, end = " ")
        column += 1
    print("") # to move onto next line
    row += 1
