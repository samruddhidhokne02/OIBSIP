import random
import string

while True:
    try:
        # Password length input
        length = int(input("Enter password length (minimum 8): "))

        if length < 8:
            print("Password length must be at least 8.")
            continue

        # Character type selection
        upper = input("Include Uppercase letters? (yes/no): ").lower()
        lower = input("Include Lowercase letters? (yes/no): ").lower()
        numbers = input("Include Numbers? (yes/no): ").lower()
        symbols = input("Include Symbols? (yes/no): ").lower()

        # Check at least 2 types selected
        selected_count = 0

        if upper == "yes":
            selected_count += 1
        if lower == "yes":
            selected_count += 1
        if numbers == "yes":
            selected_count += 1
        if symbols == "yes":
            selected_count += 1

        if selected_count < 2:
            print("Please select at least 2 character types.")
            continue

        # Store selected characters
        characters = ""

        if upper == "yes":
            characters += string.ascii_uppercase

        if lower == "yes":
            characters += string.ascii_lowercase

        if numbers == "yes":
            characters += string.digits

        if symbols == "yes":
            characters += string.punctuation

        # Generate password
        password = ""

        for i in range(length):
            password += random.choice(characters)

        print("\nGenerated Password:", password)

        # Generate again option
        again = input("\nDo you want another password? (yes/no): ").lower()

        if again != "yes":
            print("Thank you for using Password Generator!")
            break

    except ValueError:
        print("Invalid input! Please enter numbers only.")