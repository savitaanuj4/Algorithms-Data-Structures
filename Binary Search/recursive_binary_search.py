# given array a and need to find value x
def binary_search_recursive(a, x, position=0):
    left, right = 0, len(a)

    index = (left+right)//2
    if a[index]==x:
        return position+index
    elif x>(a[-1]) or x<a[0]: # first case where x is not in the list!
        return -1
    elif len(a)==1: # second case where x is not in the list!
        return -1
    elif a[index]<x:
        left = index
        a = a[left:right]
        position+=index # keeps track of the overall index
        return binary_search_recursive(a, x, position)
    elif a[index]>x:
        right = index
        a = a[left:right]
        return binary_search_recursive(a, x, position)
