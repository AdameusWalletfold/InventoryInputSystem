import pickle


def main():
    inventory_counts, inventory_costs, inventory_descriptions = read_inventory_file()

    print("Welcome to Inventory Input System")
    print("Current Inventory:")
    display_all_inventory(inventory_counts, inventory_costs, inventory_descriptions)

    response = ''
    while response != '0':
        # Display the user menu
        print("What would you like to do?")
        print("(1) Add an item\n"
              "(2) Display an item\n"
              "(3) Delete an item\n"
              "(4) Display all inventory\n"
              "(0) Exit")

        response = input('Enter your choice: ')
        if response == "1":  # Add an item
            item_name, item_count, unit_cost, description = get_item_input()
            inventory_counts[item_name] = item_count
            inventory_costs[item_name] = unit_cost
            inventory_descriptions[item_name] = description
        elif response == "2":  # Display an item
            item_name = input('Enter item name: ')
            inventory_list = [inventory_counts, inventory_costs, inventory_descriptions]
            for dictionary in inventory_list:
                if item_name in dictionary:
                    print(f'Item name: {item_name}')
                    print(f'Count: {dictionary[item_name]}')
                    print(f'Unit Cost: {inventory_costs[item_name]}')
                    print(f'Description: {inventory_descriptions[item_name]}')
                else:
                    print('Not found')
        elif response == "3":  # Delete an item
            item_name = input('Enter item name: ')
            if item_name in inventory_counts:
                inventory_counts.pop(item_name)
                inventory_costs.pop(item_name)
                inventory_descriptions.pop(item_name)
                print(f"{item_name} removed from inventory.")
            else:
                print(f"{item_name} not found in inventory.")
        elif response == "4":  # Display all inventory
            display_all_inventory(inventory_counts, inventory_costs, inventory_descriptions)
        elif response != "0":
            print("Invalid choice. Try again.\n")

    # Ready to exit the program, display and save inventory as last steps
    print("Final Inventory:")
    display_all_inventory(inventory_counts, inventory_costs, inventory_descriptions)

    save_inventory_file(inventory_counts, inventory_costs, inventory_descriptions)


def display_all_inventory(inventory_counts, inventory_costs, inventory_descriptions):
    if not inventory_counts:
        print('== Empty ==')
    else:
        print("{:<20}{:<20}{:<20}{:<20}".format("Item Name", "Count", "Unit Cost", "Description"))
        print('-' * 80)
        for item_name in inventory_counts.keys():
            count = inventory_counts[item_name]
            cost = inventory_costs[item_name]
            description = inventory_descriptions[item_name]
            print("{Name:<20}{Count:<20}{Cost:<20}{Description:<20}".format(Name=item_name, Count=count, Cost=cost, Description=description))



def save_inventory_file(inventory_counts, inventory_costs, inventory_descriptions):
    file = open('inventory.dat', 'wb')
    pickle.dump(inventory_counts, file)
    pickle.dump(inventory_costs, file)
    pickle.dump(inventory_descriptions, file)

    file.close()


def read_inventory_file():
    inventory_counts = {}
    inventory_costs = {}
    inventory_descriptions = {}
    file = open('inventory.dat', 'rb')

    inventory_counts = pickle.load(file)
    inventory_costs = pickle.load(file)
    inventory_descriptions = pickle.load(file)

    file.close()


    return inventory_counts, inventory_costs, inventory_descriptions


# This function is complete, no changes needed, but feel free to review
def get_item_input():
    # Get item name
    while True:
        item_name = input('Enter the item name: ')
        if ',' in item_name:
            print('Item names cannot contain commas.')
        else:
            break
    # Get item count
    while True:
        try:
            item_count = int(input('Enter the item count: '))
            if item_count < 0:
                print('Item count must be 0 or greater.')
            else:
                break
        except:
            print('Item count must be an integer.')
    # Get unit cost
    while True:
        try:
            unit_cost = float(input('Enter the unit cost: '))
            if unit_cost < 0:
                print('Unit cost must be 0 or greater.')
            else:
                break
        except:
            print('Unit cost must be an integer.')
    # Get description
    while True:
        description = input('Enter the description: ')
        if ',' in description:
            print('Descriptions cannot contain commas.')
        else:
            break
    return item_name, item_count, unit_cost, description


main()