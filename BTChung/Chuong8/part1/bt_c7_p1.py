import os

os.chdir('C:\\Chapter1')
test1_path = '..\\Chapter2\\Practice\\test1.txt'
test2_path = '..\\Chapter2\\Practice\\test2.txt'
test3_path = '..\\Chapter2\\Practice\\test3.txt'

# Bai 1
with open(test1_path, 'r') as f:
    print(f.readlines())

# Bai 2
with open(test2_path, 'r+') as f:
    if len(f.readlines()) > 5:
        # Move the file pointer to the beginning of the file
        f.seek(0)
        # Write 5 lines to the file
        for i in range(5):
            f.write(f'File 2 - Row {i + 1}\n')
        # Truncate the file to remove any remaining lines
        f.truncate()

# Bai 3
# Open test1.txt and test2.txt for reading
with open(test1_path, 'r') as file1, open(test2_path, 'r') as file2:
    # Read the contents of test1.txt and test2.txt
    content1 = file1.read()
    content2 = file2.read()

    # Open test3.txt for writing
    with open(test3_path, 'w') as file3:
        # Write the contents of test1.txt and test2.txt to test3.txt
        file3.write(content1)
        file3.write(content2)

# Bai 4
num_digits = 0
num_letters = 0

with open(test2_path, 'r') as file:
    # Read the contents of the file
    content = file.read()
    
    # Iterate through each character in the content
    for char in content:
        # Check if the character is a digit
        if char.isdigit():
            num_digits += 1
        # Check if the character is a letter
        elif char.isalpha():
            num_letters += 1

# Print the results
print("Number of digits:", num_digits)
print("Number of letters:", num_letters)