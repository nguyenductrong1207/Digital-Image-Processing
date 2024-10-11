# Python Program to create a dictionary

dictionary = {'a': 1, 'b': 2, 'c': 3}

def display_dictionary():
    print("Current dictionary:")
    for key, value in dictionary.items():
        print(f"{key}: {value}")

def add_key_value_pair():
    key = input("Enter the key: ")
    value = input("Enter the value: ")
    dictionary[key] = value
    print(f"Key-value pair '{key}: {value}' added.")

def update_value():
    key = input("Enter the key to update: ")
    if key in dictionary:
        new_value = input("Enter the new value: ")
        dictionary[key] = new_value
        print(f"Value for key '{key}' updated to '{new_value}'.")
    else:
        print(f"Key '{key}' not found in the dictionary.")

def remove_key():
    key = input("Enter the key to remove: ")
    if key in dictionary:
        del dictionary[key]
        print(f"Key '{key}' removed from the dictionary.")
    else:
        print(f"Key '{key}' not found in the dictionary.")

def main():
    while True:
        print("\nMenu:")
        print("1. Add key-value pair")
        print("2. Update value of a key")
        print("3. Remove a key")
        print("4. Display the dictionary")
        print("5. Convert list to ditionary")
        print("6. Exit")
        
        choice = input("Choose an option (1-6): ")

        if choice == '1':
            add_key_value_pair()
        
        elif choice == '2':
            update_value()

        elif choice == '3':
            remove_key()
        
        elif choice == '4':
            display_dictionary()

        elif choice == '5':
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
