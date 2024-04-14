def number_of_alphas_and_digits(string):
    alpha = digit = 0
    for ch in string:
        if ch.isalpha():
            alpha += 1
        if ch.isdigit():
            digit += 1
    return alpha, digit

string = input("input string: ")
alpha, digit = number_of_alphas_and_digits(string)
print("Number of alpha: {}".format(alpha))
print("Number of digit: {}".format(digit))