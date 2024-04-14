# Function to calculate the sum of values from two dictionaries
def sum_dict_values(listDict):
    sum_values = sum(dict1.values()) + sum(dict2.values())
    return sum_values

# Example dictionaries
dict1 = {"data1": 5, "data2": 10, "data3": 15}
dict2 = {"data4": 20, "data5": 25}
listDict = [dict1, dict2]

# Calculate the sum of values
total_sum = sum_dict_values(listDict)
print("Sum of the values:", total_sum)
