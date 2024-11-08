# Python Program to append element in the list and update list with insertion of elements, 
# removing an element, comparison of two lists, etc
my_list = [] 

def display_list(list):
    print("Current list:", list)
    
def append_element():
    element = input("Enter an element to append to the list: ")
    my_list.append(element)
    print(f"Element '{element}' appended.")
    
def insert_element():
    position = int(input("Enter the position (index) to insert an element (0-based): "))
    element_to_insert = input("Enter the element to insert: ")
    if 0 <= position <= len(my_list):
        my_list.insert(position, element_to_insert)
        print(f"Element '{element_to_insert}' inserted at position {position}.")
    else:
        print("Invalid position.")
        
def remove_element():
    element_to_remove = input("Enter the element to remove from the list: ")
    if element_to_remove in my_list:
        my_list.remove(element_to_remove)
        print(f"Element '{element_to_remove}' removed.")
    else:
        print(f"Element '{element_to_remove}' not found in the list.")
        
def enter_another_list():
    another_list = input("Enter another list of elements separated by space: ").split()
    print("List 1:", my_list)
    print("List 2:", another_list)
    if my_list == another_list:
        print("Both lists are equal.")
    else:
        print("The lists are not equal.")

def main():
    while True:
        print("\nMenu:")
        print("1. Append element to the list")
        print("2. Insert element at a specific position")
        print("3. Remove an element from the list")
        print("4. Compare two lists")
        print("5. Display the current list")
        print("6. Exit")
        
        choice = input("Choose an option (1-6): ")

        if choice == '1':
            append_element()
        
        elif choice == '2':
            insert_element()

        elif choice == '3':
            remove_element()
        
        elif choice == '4':
            enter_another_list()

        elif choice == '5':
            display_list(my_list)

        elif choice == '6':
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()

