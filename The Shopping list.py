
def add_items_to_list(shopping_list):
    while True:
        item = input("Enter an item to add to the shopping list (or type 'done' to finish): ")
        if item.lower() == 'done':
            break
        shopping_list.append(item)
        print(f"{item} has been added to the shopping list.")

# Function to remove items from the shopping list
def remove_item_from_list(shopping_list):
    while True:
        item_to_remove = input("Enter an item to remove from the shopping list (or type 'done' to finish): ")
        if item_to_remove.lower() == 'done':
            break
        if item_to_remove in shopping_list:
            shopping_list.remove(item_to_remove)
            print(f"{item_to_remove} has been removed from the shopping list.")
        else:
            print(f"{item_to_remove} is not in the shopping list. Please enter a valid item.")

# Function to print the shopping list in a formatted way
def print_shopping_list(shopping_list):
    if shopping_list:
        print("\nYour Shopping List:")
        for index, item in enumerate(shopping_list, start=1):
            print(f"{index}. {item}")
    else:
        print("\nYour shopping list is empty.")

# Main program with a loop for continuous interaction
if __name__ == "__main__":
    shopping_list = []
    print("Welcome to the Shopping List Maker!")

    while True:
        print("\nMenu:")
        print("1. Add items to the shopping list")
        print("2. Remove items from the shopping list")
        print("3. Print the shopping list")
        print("4. Quit")

        choice = input("Choose an option (1-4): ")

        if choice == '1':
            add_items_to_list(shopping_list)
        elif choice == '2':
            remove_item_from_list(shopping_list)
        elif choice == '3':
            print_shopping_list(shopping_list)
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")