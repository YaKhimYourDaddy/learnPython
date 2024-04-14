VPP = ['but bi', 'but chi', 'vo', 'sach GK', 'but chi', 'vo']

# Function to print the menu
def print_menu():
    print("Menu of tasks:")
    print("Enter the number of the task you want to do:")
    print("1. Add a product")
    print("2. Search for a product")
    print("3. Delete products")
    print("4. Count the number of products")
    print("5. Update a product")
    print("6. Show all products")
    print("7. Show a product at specified position")
    print("0. Exit")

# Function to add products to the list
def add_product(products_list):
    product = input("Enter product: ")
    location = int(input("Enter insert location: "))
    products_list.insert(location, product)

# Function to search for a product in the list
def search_product(products_list):
    product = input("Enter the product to search: ")
    found_locations = []
    start_location = 0
    while product in products_list[start_location:]:
        location = products_list.index(product, start_location)
        found_locations.append(location)
        if location >= len(products_list) - 1:
            break
        else:
            start_location = location + 1
    if len(found_locations) > 0:
        print("Product {} is found at locations: ".format(product), end = "")
        # print(", ".join(found_locations)) 
        # print(*found_locations, sep=", ")
        for i in range(len(found_locations)):
            print(found_locations[i], end=", " if i < len(found_locations) - 1 else "\n")
    else:
        print("There is no product {} in the list.".format(product))

# Function to delete all occurrences of a product from the list
def delete_products(products_list):
    product = input("Enter the product to delete: ")
    while product in products_list:
        products_list.remove(product)

# Function to count the number of products in the list
def count_products(products_list):
    print("The number of products in the list is:", len(products_list))

# Function to update a product in the list
def update_product(products_list):
    old_product = input("Enter the old product: ")
    if old_product in products_list:
        new_product = input("Enter the new product: ")
        while old_product in products_list:
            index = products_list.index(old_product)
            products_list[index] = new_product
    else:
        print("Product {} does not exist in the list".format(old_product))

# Function to print all products in the list
def show_all_products(products_list):
    print("List of products:")
    for i in range(len(products_list)):
        print("{}. {}".format(i, products_list[i]))

# Function to show product at specified position
def show_product_at_position(products_list):
    position = int(input("Enter the position of the product: "))
    if 0 <= position < len(products_list):
        print("Product at position {} is: {}".format(position, products_list[position]))
    else:
        print("Invalid position")

# Main loop for the program
while True:
    print_menu()
    choice = input("Enter your choice: ")
    if choice == '1':
        add_product(VPP)
    elif choice == '2':
        search_product(VPP)
    elif choice == '3':
        delete_products(VPP)
    elif choice == '4':
        count_products(VPP)
    elif choice == '5':
        update_product(VPP)
    elif choice == '6':
        show_all_products(VPP)
    elif choice == '7':
        show_product_at_position(VPP)
    elif choice == '0':
        print("Thank you for using the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please choose again.")
