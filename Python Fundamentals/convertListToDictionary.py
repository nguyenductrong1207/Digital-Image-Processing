# Python Program to convert list to dictionary

# Convert a List to a Dictionary using a Loop
def convert(list):
    res_dict = {}
    for i in range(0, len(list), 2):
        res_dict[list[i]] = list[i + 1]
    return res_dict

list = ['a', 1, 'b', 2, 'c', 3]
print(convert(list))

# List to Dictionary Conversation using dict Comprehension
def convert_with_comprehension(lst):
    res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
    return res_dct
        
# Driver code
lst = ['a', 1, 'b', 2, 'c', 3]
print(convert_with_comprehension(lst))
