                                           ##primary diagonal 
n = 5
for row in range(n):
    for col in range(n):
        if row==col:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

print()


for row in range(n):
    for col in range(n):                   ##secondary diagonal 
        if row + col == n-1:
            print(row+1,end=" ")
        else:
            print(" ",end=" ")
    print()
