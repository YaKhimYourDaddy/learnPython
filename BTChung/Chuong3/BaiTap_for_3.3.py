for row in range(9):
    for column in range(9):
        result = row * column

        # add a space to format the table for better look
        if result < 10:
            print(" ", end = "") 

        print(result, end = " ")

    print("") # to move onto next line
    row += 1