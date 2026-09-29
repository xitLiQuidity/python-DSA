def diagonalDifference(arr):
    
    arr_len = len(arr)
    
    leftdiagonalsum = 0 
    rightdiagonalsum = 0 
    
    i = 0 
    j = 0 
    
    while i < arr_len:
        leftdiagonalsum += arr[i][j]
        i += 1 
        j += 1 
        
    i = 0 
    j = arr_len - 1 
    while i < arr_len:
        rightdiagonalsum += arr[i][j]
        i += 1
        j -= 1 
        
    return abs(leftdiagonalsum - rightdiagonalsum)
