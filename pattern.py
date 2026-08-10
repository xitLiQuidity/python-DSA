#printing only the borders in square
n = 5

for row in range(n):
    for col in range(n):
        if row == 0 or col == 0 or row == n-1 or col == n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()



##getting @ at the centre of the box mid position
for row in range(n):
    for col in range(n):
        if row == 0 or col == 0 or row == n-1 or col == n-1:
            print("*",end=" ")
        elif (row==n//2 and col == n//2):
            print("@",end=" ")
        else:
            print(" ",end=" ")
    print()
        
