# Binary Search in Python
# Linear Search in Python
# Bubble Sort in Python
# Insertion Sort in Python
# Heap Sort in Python
# Merge Sort in Python

list = [5, 3, 8, 1, 2, 7, 4, 6, 9, 14, 24, 25, 26]

def binary_search(list, target):
    left, right = 0, len(list) - 1
    while left <= right:
        mid = (left + right) // 2
        mid_value = list[mid]
        
        if mid_value == target:
            return mid
        elif mid_value < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return -1

def linear_search(list, target):
    for index, value in enumerate(list):
        if value == target:
            return index
    return -1

def bubble_sort(list):
    n = len(list)
    for i in range(n):
        for j in range(0, n-i-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]

def insertion_sort(list):
    for i in range(1, len(list)):
        key = list[i]
        j = i - 1
        while j >= 0 and key < list[j]:
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = key

def heapify(list, n, i):
    # Helper function for heap sort to maintain heap property
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and list[left] > list[largest]:
        largest = left

    if right < n and list[right] > list[largest]:
        largest = right

    if largest != i:
        list[i], list[largest] = list[largest], list[i]
        heapify(list, n, largest)

def heap_sort(list):
    n = len(list)
    for i in range(n // 2 - 1, -1, -1):
        heapify(list, n, i)

    for i in range(n - 1, 0, -1):
        list[0], list[i] = list[i], list[0]
        heapify(list, i, 0)

def merge_sort(list):
    if len(list) > 1:
        mid = len(list) // 2
        L = list[:mid]
        R = list[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                list[k] = L[i]
                i += 1
            else:
                list[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            list[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            list[k] = R[j]
            j += 1
            k += 1

def main():
    while True:
        print("\nMenu:")
        print("1. Binary Search")
        print("2. Linear Search")
        print("3. Bubble Sort")
        print("4. Insertion Sort")
        print("5. Heap Sort")
        print("6. Merge Sort")
        print("7. Exit")

        choice = input("Choose an option (1-7): ")

        if choice == '1':
            target = int(input("Enter the number to search for: "))
            result = binary_search(list, target)
            if result != -1:
                print(f"Number {target} found at index {result}.")
            else:
                print(f"Number {target} not found in the list.")

        elif choice == '2':
            target = int(input("Enter the number to search for: "))
            result = linear_search(list, target)
            if result != -1:
                print(f"Number {target} found at index {result}.")
            else:
                print(f"Number {target} not found in the list.")

        elif choice == '3':
            bubble_sort(list)
            print("Sorted list (Bubble Sort):", list)

        elif choice == '4':
            insertion_sort(list)
            print("Sorted list (Insertion Sort):", list)

        elif choice == '5':
            heap_sort(list)
            print("Sorted list (Heap Sort):", list)

        elif choice == '6':
            merge_sort(list)
            print("Sorted list (Merge Sort):", list)

        elif choice == '7':
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
