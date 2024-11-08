my_dict = {'a': 1, 'b': 2, 'c': 3}

def display_dictionary():
    if not my_dict:
        print("The dictionary is empty.")
    else:
        print("Current dictionary:")
        for key, value in my_dict.items():
            print(f"{key}: {value}")

def add_key_value_pair():
    key = input("Enter the key: ")
    value = input("Enter the value: ")
    my_dict[key] = value
    print(f"Key-value pair '{key}: {value}' added.")

def sort_dictionary_by_keys():
    if not my_dict:
        print("The dictionary is empty. Please add elements to the dictionary first.")
        return
    
    sorted_dict = dict(sorted(my_dict.items()))
    print("Dictionary sorted by keys:", sorted_dict)

def sort_dictionary_by_values():
    if not my_dict:
        print("The dictionary is empty. Please add elements to the dictionary first.")
        return
    
    # Convert all values to strings for sorting
    sorted_dict = dict(sorted(my_dict.items(), key=lambda item: str(item[1])))
    print("Dictionary sorted by values:", sorted_dict)


def main():
    while True:
        print("\nMenu:")
        print("1. Add a key-value pair")
        print("2. Display the current dictionary")
        print("3. Sort the dictionary by keys")
        print("4. Sort the dictionary by values")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            add_key_value_pair()
        
        elif choice == '2':
            display_dictionary()

        elif choice == '3':
            sort_dictionary_by_keys()

        elif choice == '4':
            sort_dictionary_by_values()

        elif choice == '5':
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
