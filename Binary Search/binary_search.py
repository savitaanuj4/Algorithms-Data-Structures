"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

def binary_search(input_array, value):
    """Your code goes here."""
    test_array = input_array
    current_index = int(len(input_array)/2)
    input_index = current_index

    found_value = test_array[current_index]
    while(len(test_array)>1 and found_value!=value):
        if(found_value<value):
            test_array = test_array[current_index:]
            current_index = int(len(test_array)/2)
            input_index += current_index
            found_value = test_array[current_index]
        else:
            test_array = test_array[0:current_index]
            current_index = int(len(test_array)/2)
            # had issues with using a '2' instead of a '2.0' on the below
            # line - need to use decimals to get the precision right and
            # round correctly!
            input_index = input_index - int(round(len(test_array)/2.0))

            found_value = test_array[current_index]

    if(found_value==value):
        return input_index

    return -1

test_list = [1,3,9,11,15,19,29, 35, 36, 37]
test_val1 = 25
test_val2 = 15
print binary_search(test_list, test_val1)
print binary_search(test_list, test_val2)
print binary_search(test_list, 11)
