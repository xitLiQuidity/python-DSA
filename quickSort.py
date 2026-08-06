def partition(start,end,l1):
    i = start
    j = end-1
    pivot = l1[end]

    while i < j:
        while l1[i] < pivot:
            i += 1

        while l1[j] > pivot:
            j -= 1 

        if i < j:
            l1[i], l1[j] = l1[j], l1[i]

    if l1[i] > pivot:
        l1[i] , l1[end] = l1[end], l1[i]

    return i 

def quick_sort(start,end,l1):
    if start < end:
        pi = partition(start,end,l1)
        quick_sort(start,pi-1,l1)
        quick_sort(pi+1,end,l1)

l1 = [3,5,8,1,2,9,4,7,6]
print("before sorting :",l1)
quick_sort(0,len(l1)-1,l1)
print("after soting :", l1)



# QUICK SORT - 

# - START THE ALOGRITHM FROM START VALUE AND END VALUE AND START VALUE SHOULD BE ALWAYS LESS THAN END VALUE 
# - IF IT IS TRUE CALL THE PARTITION ALGORITHM AND STORE THE PATITION POSITION INTO A LOCAL VARIABLE 
# - RECURSIVELY CALL THE QUICK SORT SORT ALGORITHM FOR LEFT OF THE LIST BY PASSING START AND END AGAIN RECURSIVELY CALL QUICK SORT ALGORITHM FOR RIGHT OF THE LIST BY PASSING START AND END POSITON 
