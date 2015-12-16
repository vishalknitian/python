#Merge Sort - Python3

#Procedure merge_sort is called recursively to sort subarrays.
def merge_sort(raw_list, start, end):
    if start<end:
        mid=(start+end)//2
        merge_sort(raw_list, start, mid)
        merge_sort(raw_list, mid+1, end)
        merge(raw_list,start,mid,end)


#Procedure merge is used to merge sorted subarrays.
def merge(raw_list, start, mid, end):
    len_left_list = mid-start+1
    len_right_list = end-mid 
    left_list=[]
    right_list=[]
    for i in range(start,mid+1):
        left_list.append(raw_list[i])

    for j in range(mid+1,end+1):
        right_list.append(raw_list[j])
    i=0
    j=0
    for k in range(start,end+1):
        if i>=len_left_list:
            raw_list[k]=right_list[j]
            j=j+1
        elif j>=len_right_list:
            raw_list[k]=left_list[i]
            i=i+1
        elif left_list[i]<right_list[j]:
            raw_list[k]=left_list[i]
            i=i+1
        else:
            raw_list[k]=right_list[j]
            j=j+1
    

#Test with hardcoded list.
x=[5,4,3,2,1]
merge_sort(x,0,len(x)-1)
print(x)
