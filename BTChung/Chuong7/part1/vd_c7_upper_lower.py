def count_character(string, ch):
    string = string.lower()
    ch = ch.lower()
    
    count = 0
    for char in string:
        if char == ch:
            count += 1
    return count

# Example string and character
input_str = input("input string: ")
input_ch = input("input character: ")

# Count the number of occurrences of the character
num_occurrences = count_character(input_str, input_ch)
print("Number of character", input_ch, "is:", num_occurrences)
