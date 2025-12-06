def greet_user():
    name = input("Enter your name: ")

    gender = input("Enter your gender : ").lower()

    if gender == "boy":
        prefix = "Mr."
    elif gender == "girl":
        prefix = "Ms."
    else:
        prefix = ""

    full_name = prefix + name
    print(f"Hello, {full_name}!")

    return full_name

def show_numbers():
    print("Numbers from 1 to 10:")
    for i in range(1, 11):
        print(i, end=' ')

    print("Now let us showw them in a list")

    numbers = []
    for i in range(1,6):
        numbers.append(i)

    print("List of numbers:", numbers)

def sum_of_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

user_full_name = greet_user()
show_numbers()

numbers = [1,2,3,4,5]
total = sum_of_list(numbers)

# Pulled and made some changes

print(f"{user_full_name} the sum of {numbers} is {total}")