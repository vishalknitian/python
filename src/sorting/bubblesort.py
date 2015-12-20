# Bubble sort - Python3

# Procedure bubble_sort sorts the list by pushing the biggest element towards end.
# Worst case complexity is O(n^2).
def bubble_sort(raw_list):
    length = len(raw_list)
    for i in range(length - 1, -1, -1):
        for j in range(0, i):
            if(raw_list[j] > raw_list[j+1]):
                element = raw_list[j]
                raw_list[j] = raw_list[j+1]
                raw_list[j+1] = element

# Test with hardcoded list.
x = [3,7,8,5,4,3,2,1]
bubble_sort(x)
print(x)
