# Python Program to Merge two Dictionaries

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'a': 11, 'b': 22, 'c': 33}

def display_dictionaries():
    print("\nCurrent Dictionaries:")
    print("Dictionary 1:", dict1)
    print("Dictionary 2:", dict2)

def add_key_value_pairs(dict_number):
    if dict_number == 1:
        target_dict = dict1
    else:
        target_dict = dict2
        
    while True:
        key = input(f"Enter a key to add to Dictionary {dict_number} (or type 'done' to finish): ")
        if key.lower() == 'done':
            break
        value = input("Enter the value for the key: ")
        target_dict[key] = value
        print(f"Key-value pair '{key}: {value}' added to Dictionary {dict_number}.")

def merge_dictionaries():
    global dict1, dict2
    merged_dict = {**dict1, **dict2}  
    print("Merged Dictionary:", merged_dict)

def main():
    while True:
        print("\nMenu:")
        print("1. Add key-value pairs to Dictionary 1")
        print("2. Add key-value pairs to Dictionary 2")
        print("3. Display the current dictionaries")
        print("4. Merge the two dictionaries")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            add_key_value_pairs(1)
        
        elif choice == '2':
            add_key_value_pairs(2)

        elif choice == '3':
            display_dictionaries()

        elif choice == '4':
            merge_dictionaries()

        elif choice == '5':
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
