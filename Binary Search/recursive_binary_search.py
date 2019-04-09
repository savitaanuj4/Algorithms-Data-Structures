# given array a and need to find value x
def binary_search_recursive(a, x, position=0):
    left, right = 0, len(a)

    index = (left+right)//2
    if a[index]==x:
        return position+index
    if len(a)==1: # case where x is not in the list!
        return -1
    elif a[index]<x:
        left = index
        a = a[left:right]
        position+=index # keeps track of the overall index
        return binary_search(a, x, position)
    elif a[index]>x:
        right = index
        a = a[left:right]
        return binary_search(a, x, position)
