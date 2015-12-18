# Selection Sort - Python3

# Procedure selection_sort sorts a list with a complexity of O(n^2).
def selection_sort(raw_list):
    for i in range(0, len(raw_list)):
        min = raw_list[i]
        position = i
        for j in range(i, len(raw_list)-1):
            if(min > raw_list[j+1]):
                min = raw_list[j+1]
                position = j + 1
        temp = raw_list[i]
        raw_list[i] = raw_list[position]
        raw_list[position] = temp

#Test with hardcoded list.
x = [5,9,8,2,4,3,2,1]
selection_sort(x)
print(x)
