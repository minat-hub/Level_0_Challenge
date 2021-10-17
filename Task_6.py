def maximum(*numbers):
    """This function returns the maximum number out of all the numbers
     passed into the function."""
    max_number = 0
    for number in numbers:
        if number > max_number:
            max_number = number
    return max_number
       
print(maximum(9,4,6,7))
print(maximum(1,2,3))
