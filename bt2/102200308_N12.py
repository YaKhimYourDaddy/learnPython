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

# bai2
def read2(input_file):
    with open(input_file, 'r') as f:
        M, N = map(int, f.readline().strip().split())
        
        matrix = []
        for _ in range(M):
            row = list(map(int, f.readline().strip().split()))
            matrix.append(row)
        
    return M, N, matrix

def write2(output_file, matrix):
    with open(output_file, 'w') as f:
        for row in matrix:
            f.write(' '.join(map(str, row)) + '\n')

def sort_rows_descending(matrix):
    sorted_matrix = [sorted(row, reverse=True) for row in matrix]
    return sorted_matrix

def bai2(input_file, output_file):
    M, N, matrix = read2(input_file)
    sorted_matrix = sort_rows_descending(matrix)
    write2(output_file, sorted_matrix)

# bai3
def sort_list_with_indices(original_list):
    # Sort the list while preserving original indices
    sorted_indexed_list = sorted(enumerate(original_list), key=lambda x: x[1])
    # Extract the sorted items and the corresponding original indices
    sorted_items = [item for index, item in sorted_indexed_list]
    original_indices = [index for index, item in sorted_indexed_list]
    return sorted_items, original_indices

def find_min_numbers(arrA, arrK):
    sortedArrA = sorted(arrA)
    sortedArrK, originalIndicesK = sort_list_with_indices(arrK)
    current_index_on_A = 0
    lenA = len(sortedArrA)
    sortedResult = sortedArrK.copy()
    for indexK in range(len(sortedArrK)):
        while (sortedArrA[current_index_on_A] < sortedArrK[indexK]):
            current_index_on_A += 1
            if current_index_on_A >= lenA:
                break
        if current_index_on_A < lenA:
            sortedResult[indexK] = sortedArrA[current_index_on_A]
            continue
        for i in range(indexK, len(sortedArrK)):
            sortedResult[i] = -1
        break

    correctResult = sortedResult.copy()
    for indice, minNum in zip(originalIndicesK, sortedResult):
        correctResult[indice] = minNum
    
    return correctResult

def read3(input_file):
    with open(input_file, 'r') as f:
        N = int(f.readline().strip())
        arrA = list(map(int, f.readline().strip().split()))
        M = int(f.readline().strip())
        arrK = [int(f.readline().strip()) for _ in range(M)]
    return arrA, arrK

def write3(output_file, result):
    with open(output_file, 'w') as f:
        for item in result:
            f.write(str(item) + '\n')


def bai3(input_file, output_file):
    arrA, arrK = read3(input_file)
    result = find_min_numbers(arrA, arrK)
    write3(output_file, result)

# bai4
def bai4(input_file, output_file):
    with open(input_file, 'r') as f:
        N = int(f.readline().strip())
        A = list(map(int, f.readline().strip().split()))
        M = int(f.readline().strip())
        result = []
        for _ in range(M):
            Q = int(f.readline().strip())
            if Q == -1:
                min_value = min(A)
                A.remove(min_value)
                result.append(min_value)
            else:
                A.append(Q)
    with open(output_file, 'w') as f:
        for item in result:
            f.write(str(item) + '\n')

def main():
    bai1("InpMax.txt", "OutMax.txt")
    bai2("InpSortRow.txt", "OutSortRow.txt")
    bai3("inpNN.txt", "outNN.txt")
    bai4("inpTB.txt", "outTB.txt")

if __name__ == "__main__":
    main()

