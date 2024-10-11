# Python Program to Convert Decimal to Binary, Octal and Hexadecimal

decimal_num = int(input("Enter a decimal number: "))

binary_num = bin(decimal_num)  
octal_num = oct(decimal_num)   
hexadecimal_num = hex(decimal_num)  

print(f"Binary of {decimal_num} is {binary_num[2:]}")
print(f"Octal of {decimal_num} is {octal_num[2:]}")
print(f"Hexadecimal of {decimal_num} is {hexadecimal_num[2:]}")
