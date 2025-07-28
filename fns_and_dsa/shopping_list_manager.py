shopping_list = []

def display_menu():
    print("1. Add item")
    print("2. Remove item")
    print("3. View the items")
    print("4. Exit")

def main():
    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            add_item = input("Add an item: ")
            shopping_list.append(add_item)
            print(shopping_list)

        elif choice == 2:
            remove_item = input("Enter the item to remove: ")
            if remove_item in shopping_list:
                shopping_list.remove(remove_item)
                print("Item remov
