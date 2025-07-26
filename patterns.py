#printing the Hallow square
n=int(input("enter the size of the square:"))
for i in range(n):
    for j in range(n):
        if j==0 or j==n-1 or i==0  or i==n-1 :
            print("*",end="")
        else:
            print(" ",end="")
    print()


#printing the left sided right angle triangle
for i in range(0,n+1):
    print("*"*i)


#printing the inverted left sided right angle triangle
for i in range(n+1,0,-1):
    print("*"*i)


