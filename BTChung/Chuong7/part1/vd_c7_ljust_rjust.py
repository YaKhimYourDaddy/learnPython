def show(menu):
    for name, quantity in menu.items():
        print(name.ljust(20, '.') + str(quantity).rjust(6))

menu = {}
for i in range(4):
    name = input("input name: ")
    quantity = int(input("input quantity: "))
    menu[name] = quantity
show(menu)
    

