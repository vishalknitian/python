#Insertion Sort - Python3

#Procedure insertion_sort sorts the list of numbers with nested loops, with O(n^2) complexity.
def insertion_sort(raw_list):
    length = len(raw_list)
    for i in range(0, length):
        for j in range(i, 0, -1):
            if(raw_list[j] <= raw_list[j-1]):
                element = raw_list[j]
                raw_list[j] = raw_list[j-1] 
                raw_list[j-1] = element


#Test with hardcoded list.
x = [5,4,3,2,1]
insertion_sort(x)
print(x)
