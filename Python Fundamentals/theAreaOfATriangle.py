# Python program to find the area of a triangle

# Area of a Right-Angled Triangle in Python
# area = 0.5 * base * height
def right_angled_triangle():
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))

    area = 0.5 * base * height

    print(f"The area of the triangle with base {base} and height {height} is: {area}")
    
right_angled_triangle()   

# Area of a Triangle in Python Using Heron’s Formula 
def herons_formula():
    side1 = float(input("Enter the first side of the triangle: "))
    side2 = float(input("Enter the second side of the triangle: "))
    side3 = float(input("Enter the third side of the triangle: "))
    
    s = (side1 + side2 + side3) / 2
    area = (s*(s-side1)*(s-side2)*(s-side3))**0.5
    
    print(f"The area of the triangle with Heron’s Formula is: {area}")
    
    # format in two decimal digits
    print('The area of the triangle with Heron’s Formula is: {:.2f}'.format(area))

herons_formula()