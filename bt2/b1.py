# bai1
def find_max_abs(lines):
    max_negative = 0
    max_positive = 0

    for line in lines:
        num = int(line.strip())

        if num < 0:
            if max_negative == 0 or num < max_negative:
                max_negative = num
        elif num > 0:
            if max_positive == 0 or num > max_positive:
                max_positive = num

    return max_negative, max_positive

def bai1(input_file, output_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()
    max_negative, max_positive = find_max_abs(lines)
    with open(output_file, 'w') as f:
        f.write(f"{max_negative} {max_positive}\n")

def main():
    bai1("InpMax.txt", "OutMax.txt")

if __name__ == "__main__":
    main()
