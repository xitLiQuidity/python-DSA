n = 5

for row in range(n):                        #plus printing only works when the given input is odd
    for col in range(n):
        if row == n//2 or col == n // 2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


for row in range(n):                      ##cross printing only works when the given input lenght is odd
    for col in range(n):
        if row == col or row + col == n-1:
            print("*",end=" ")
        else: 
            print(" ",end=" ")
    print()
