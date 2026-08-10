n= 6                             ##PYRAMID PATTERN PRINTING
spc = n-1
star = 1

for row in range(n):
    #space
    for i in range(spc):
        print(" ",end=" ")

    #star
    for j in range(star):
        print("*",end=" ")

    spc -= 1
    star +=2
    print()



    # OPTIMIZED CODE with better complexities

for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")

    for k in range(1,i*2):
        print("*",end=" ")
    print()


