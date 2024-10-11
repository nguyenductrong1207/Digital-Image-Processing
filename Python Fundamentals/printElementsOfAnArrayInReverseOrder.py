# Python program to print the elements of an array in reverse order

n = int(input("Enter the number of elements in the array: "))

array = []

for i in range(n):
    element = input(f"Enter element {i + 1}: ")
    array.append(element)

print("The elements of the array in reverse order are:")
for element in reversed(array):
    print(element)
