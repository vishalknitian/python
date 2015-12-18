# Binary Search - Python3

# Procedure binary_search uses divide and conquer approach.
# It divides the problem of size 'n' into sub problems of size 'n/2'.
# It also assumes the list is already in a sorted order(ascending).
# Worst-case complexity O(logn).
def binary_search(list, search_element):
    start = 0
    end = len(list) -1
    while start < end:
        mid = (start + end)//2
        if (list[mid] == search_element):
            print("Element found at position: ", (mid + 1))
            break
        elif (list[mid] < search_element):
            start = mid + 1
        else:
            end = mid - 1

#Test with hardcoded list.
x = [1,3,5,7,9]
binary_search(x, 7)
