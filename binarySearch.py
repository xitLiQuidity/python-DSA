#BINARY SEARCH 
# it is a searching technique which helps us to search for the given element only in sorted list 

# algoithm - 
# consider 2 variables start and end 

# --------------------
# 11|18|27|43|49|51|65|            sorted manner 
# --------------------
# start             end           pointing at index 

# - start a traversing by checking start index should be always less than n th index if it is true find the mid index with the help of start and end.
# mid = (start + end) // 2
#        (0+6) // 2 -> 3 

# - check if the mid value is equals to the search value or not , if true return mid 
# - if the above condition is false check if search value is less than the mid value or not, if it is true bring the end to mid -1 position
# elif search_val < l1[mid]
#  end = mid -1 
# - elif search_val > l1[mid]:
#   start = mid + 1

def binary_search(l1,num):
    start = 0 
    end = len(l1)-1

    while start < end:
        mid = (start+end) // 2 
        if l1[mid] == num:
            return mid
        elif num < l1[mid]:
            end = mid - 1
        elif num > l1[mid]:
            start = mid + 1

        return -1

l1 = [11,23,45,67,89,90,101]
num = 101
print("value found at: ",binary_search(l1,num))
        
