
# bai3
def sort_list_with_indices(original_list):
    sorted_indexed_list = sorted(enumerate(original_list), key=lambda x: x[1])
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

def main():
    bai3("inp.txt", "out.txt")

if __name__ == "__main__":
    main()

