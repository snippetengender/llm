def show_menu():
    print("\nString Operations:")
    print("1. Reverse string")
    print("2. Check palindrome")
    print("3. Count vowels")
    print("4. Character frequency")
    print("5. Find substring")
    print("6. Exit")

while True:
    s = input("Enter a string: ")
    print(s)
    show_menu()
    choice = int(input("Enter your choice (1-6): "))
    

    if choice == 1:
        print("Reversed string:", s[::-1])
    elif choice == 2:
        if s == s[::-1]:
            print("The string is a palindrome.")
        else:
            print("The string is not a palindrome.")
    elif choice == 3:
        count = 0
        for ch in s.lower():
            if ch in 'aeiou':
                count += 1
        print("Number of vowels:", count)
    elif choice == 4:
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1
        print("Character frequency:", freq)
    elif choice == 5:
        sub = input("Enter substring to find: ")
        if sub in s:
            print(f"Substring '{sub}' found in the string.")
        else:
            print(f"Substring '{sub}' not found in the string.")
    else:
        print("Exiting...")
        break
    