def show_menu():
    print("\nDictionary Operations:")
    print("1. Add key-value pair")
    print("2. Update value of a key")
    print("3. Delete a key")
    print("4. Search for a key")
    print("5. Display dictionary")
    print("6. Count character frequency (string → dictionary)")
    print("7. Exit")

my_dict = {}

while True:
    show_menu()
    choice = input("Enter your choice (1-7): ")

    if choice == '1':
        key = input("Enter key: ")
        value = input("Enter value: ")
        my_dict[key] = value
        print(f"Added ({key}: {value}) to the dictionary.")
    
    elif choice == '2':
        key = input("Enter key to update: ")
        if key in my_dict:
            value = input("Enter new value: ")
            my_dict[key] = value
            print(f"Updated ({key}: {value}) in the dictionary.")
        else:
            print("Key not found.")
    elif choice == '3':
        key = input("Enter key to delete: ")
        if key in my_dict:
            del my_dict[key]
            print(f"Deleted key '{key}' from the dictionary.")
        else:
            print("Key not found.")
    elif choice == '4':
        key = input("Enter key to search: ")
        if key in my_dict:
            print(f"Found: ({key}: {my_dict[key]})")
        else:
            print("Key not found.")
    elif choice == '5':
        print("Current Dictionary:", my_dict)
    elif choice == '6':
        s = input("Enter a string: ")
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1
        print("Character Frequency:", freq)
    elif choice == '7':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")