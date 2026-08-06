# #MERGE SORT
# it is a advance sorting algorithm which helps us to sort the given list with the help of divide and conquer algorithm
# - check if the lenght of given list is more than 1 then divide the given list into 2 parts with the help of mid value and with the help of mid divide the list into two parts left list and right list 
# - recusively call the merge sort to divide the remaining list into 2 parts until it cannot be further divided 
# - division is completed start merging the elements by comparing left list element is greater than the right list element or not, if it is true swap the elements

def merge_sort(l1):
    if len(l1) > 1:
        mid = len(l1) // 2
        left_list = l1[:mid]
        right_list = l1[mid:]
        merge_sort(left_list)
        merge_sort(right_list)

        i = 0
        j = 0
        k = 0

        while i < len(left_list) and j < len(right_list):
             if left_list[i] < right_list[j]:
                 l1[k] = left_list[i]
                 i += 1
             else:
                 l1[k] = right_list[j]
                 j += 1
             k += 1

        #check if any element is remaining in both the 
        while i < len(left_list):
            l1[k] = left_list[i]
            i += 1
            k += 1

        while j < len(right_list):
            l1[k] = right_list[j]
            j += 1
            k += 1
    

l1 =[8,7,11,1,5,9,2,4]
print("l1 before merge sort:", l1)
merge_sort(l1)
print("l1 after merge sort:", l1)
