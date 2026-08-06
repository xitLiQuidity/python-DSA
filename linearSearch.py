#LINEAR SEARCH or sequential search 
# - it is also known as sequential search which helps us to search for the given element is pesent or not in the given list
# - in this iterate through each element and compare with given element, if it is true print its index and break the loop 
# - if all the iteration is completed while coming out of the for loop print value not found in the else block 

def linear_search(num,l1):
    for i in range(len(l1)):
        if l1[i] == num:
            print("value found at ", i )
            break
    else: 
            print("value not found")

l1 = [12, 45, 23, 67, 11, 47, 35]
num = 67
linear_search(num,l1)
