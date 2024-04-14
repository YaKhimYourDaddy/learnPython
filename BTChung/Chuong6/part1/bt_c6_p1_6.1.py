# Function to input items and quantities into a dictionary
def input_items(itemDict):
    while True:
        name = input("Enter the name of the item (enter empty to finish): ")
        if not name:
            break
        quantity = int(input("Enter the quantity: "))
        if name in itemDict:
            itemDict[name] += quantity  # If item already exists, increment quantity
            # itemDict.update(name, itemDict[name] + quantity)
        else:
            itemDict[name] = quantity

# Function to print the item with the maximum and minimum quantity
def print_max_min_quantity(itemDict):
    if not itemDict:
        print("No item entered yet.")
        return
    max_quantity = max(itemDict.values())
    min_quantity = min(itemDict.values())
    max_items = [name for name, quantity in itemDict.items() if quantity == max_quantity]
    min_items = [name for name, quantity in itemDict.items() if quantity == min_quantity]
    
    print(f"Item(s) with the maximum quantity {max_quantity}:")
    # print(", ".join(found_locations)) 
    # print(*found_locations, sep=", ")
    for i in range(len(max_items)):
        print(max_items[i], end=", " if i < len(max_items) - 1 else "\n")
        
    print(f"Item(s) with the minimum quantity {min_quantity}:")
    # print(", ".join(min_items)) 
    # print(*min_items, sep=", ")
    for i in range(len(min_items)):
        print(min_items[i], end=", " if i < len(min_items) - 1 else "\n")

# Function to remove items with quantity <= 10
def remove_items(itemDict):
    if not itemDict:
        print("No items entered yet.")
        return
    keys_to_remove = [name for name, quantity in itemDict.items() if quantity <= 10]
    for key in keys_to_remove:
        # del itemDict[key]
        itemDict.pop(key)
    print("itemDict after removal:")
    print_items(itemDict)


# Function to search for an item by name and print its quantity
def search_item(itemDict):
    if not itemDict:
        print("No item entered yet.")
        return
    name = input("Enter the name of the item to search for: ")
    if name in itemDict:
        print("Quantity of item {}: {}".format(name, itemDict[name]))
    else:
        print("Item {} not found".format(name))

# Function to print all items and quantities
def print_items(itemDict):
    if not itemDict:
        print("No item entered yet.")
        return
    print("All items and quantities:")
    for name, quantity in itemDict.items():
        print("- Name:", name, "| Quantity:", quantity)

# Main menu
def main_menu():
    itemDict = {}
    while True:
        print("\nMenu:")
        print("a. Input items and quantities")
        print("b. Print item with maximum and minimum quantity")
        print("c. Print all items and quantities")
        print("d. Remove items with quantity <= 10")
        print("e. Search for an item by name")
        print("0. Exit")
        choice = input("Enter your choice: ")
        if choice == 'a':
            input_items(itemDict)
        elif choice == 'b':
            print_max_min_quantity(itemDict)                
        elif choice == 'c':
            print_items(itemDict)
        elif choice == 'd':
            remove_items(itemDict)
        elif choice == 'e':
            search_item(itemDict)
        elif choice == '0':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the main menu
if __name__ == "__main__":
    main_menu()
