# Function to concatenate three dictionaries into one
def concatenate_dicts(listDict):
    result_dict = {}
    for d in listDict:
        for key, value in d.items():
            result_dict[key] = value
    return result_dict

# Example dictionaries
dict1 = {1: 10, 2: 20, 3: 30}
dict2 = {4: 40, 5: 50}
dict3 = {6: 60, 7: 70, 8: 80}
listDict = [dict1, dict2, dict3]

# Concatenate dictionaries
dict_result = concatenate_dicts(listDict)
print("Concatenated dictionary:", dict_result)
