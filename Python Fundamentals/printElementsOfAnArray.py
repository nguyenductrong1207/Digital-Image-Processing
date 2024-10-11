# Python program to print the elements of an array

n = int(input("Enter the number of elements in the array: "))

array = []

for i in range(n):
    element = input(f"Enter element {i + 1}: ")
    array.append(element)

print("The elements of the array are:")
for element in array:
    print(element)
