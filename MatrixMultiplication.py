# 65. Matrix multiplication

x = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

y = [
    [10, 11, 12],
    [13, 14, 15],
    [16, 17, 18]
]

result = [  
    [0, 0, 0],              #This is where we store the answer
    [0, 0, 0],
    [0, 0, 0]
]

for i in range(len(x)):            #i represents the row
    for j in range(len(y[0])):     #j represents the column, This line is simply finding how many columns Matrix y has, and then making j move through those column positions.
        for k in range(len(y)):    #k is used to perform the multiplication and addition.
            result[i][j] += x[i][k] * y[k][j] #Take one row from x, one column from y, multiply corresponding values, add them, and put the answer into result[i][j]
for r in result: #This goes through each row of result and prints it.
    print(r)


# y[0]
# means:
# Give me the first row of y

# i → row
# j → column
# k → multiply and add
