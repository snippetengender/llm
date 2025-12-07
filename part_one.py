def show_menu():
    print("\nChoose an operation:")
    print("1. Insert an element")
    print("2. Delete an element")
    print("3. Search an element")
    print("4. Update an element")
    print("5. Display array")
    print("6. Exit")

arr = []

while True:
    show_menu()
    print(arr)
    choice = int(input("Enter your choice (1-6): "))

    if choice == 1:
        value = int(input("Enter value to insert: "))
        arr.append(value)
        print("Inserted!")

    elif choice == 2:
        value = int(input("Enter value to delete: "))
        if value in arr:
            arr.remove(value)
            print("Deleted!")
        else:
            print("Element not found!")
    
    elif choice == 3:
        value = int(input("Enter value to search: "))
        found = False
        for i in range(len(arr)):
            if arr[i] == value:
                print(f"Element found at index {i}")
                found = True
                break
        if not found:
            print("Element not found!")
    
    elif choice == 4:
        index = int(input("Enter index to update: "))
        if 0 <= index < len(arr):
            new_value = int(input("Enter new value: "))
            arr[index] = new_value
            print("Updated!")
        else:
            print("Index out of range!")
    elif choice == 5:
        print("Current array:", arr)
    elif choice == 6:
        print("Exiting...")
        break