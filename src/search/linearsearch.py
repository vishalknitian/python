# Linear Search - Python3

# Procedure linear_search is used to search an element sequentially.
# Worst-case complexity O(n)

def linear_search(list, search_element):
    for i in range(0, len(list)):
        if (search_element == list[i]):
            print("Element found at position: ", (i+1))

#Test with hardcoded data.
x = [2,4,6,8,2]
linear_search(x, 2)
