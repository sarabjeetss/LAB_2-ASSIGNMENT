
'''
    SARABJET SINGH
    22049221
    SOLUTION OF QUE 4

    '''
# take random numbers in list
myNumbers = [1, 5, 6, 7, 10, 12, 4, 18, 52, 74, 64, 1] 

# according to que use function and loop
def list_elements(list):
    for element in list:   #using loop
        print(element)

def print_elements_greater_than_12(list):
    greater_than_12 = [element for element in list if element > 12]
    print(f"Elements greater than 12: {greater_than_12}")
 

print("All elements in the list:")
print(myNumbers)

print("\n") # for space in line
print_elements_greater_than_12(myNumbers)
