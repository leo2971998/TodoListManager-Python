todo_list = []

def add_item(item):
    todo_list.append(item)

def view_items():
    for item in todo_list:
        print(item)

def mark_item_as_completed(index):
    todo_list[index] = "DONE: " + todo_list[index]

def delete_item(index):
    del todo_list[index]

def main():
    while True:
        print("What would you like to do?")
        print("(1) Add an item")
        print("(2) View items")
        print("(3) Mark an item as completed")
        print("(4) Delete an item")
        print("(5) Exit")
        choice = int(input())
        if choice == 1:
            item = input("Enter the item: ")
            add_item(item)
        elif choice == 2:
            view_items()
        elif choice == 3:
            index = int(input("Enter the index of the item: "))
            mark_item_as_completed(index)
        elif choice == 4:
            index = int(input("Enter the index of the item: "))
            delete_item(index)
        elif choice == 5:
            break

main()