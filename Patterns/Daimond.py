#printing diamond pattern
n=4
for i in range(0,n):
  for j in range(i,n):
    print(" ",end=" ")
  for j in range(i+1):
    print("*",end=" ")
  for j in range(i):
    print("*",end=" ")
  for j in range(i):
    print(" ",end=" ")
  print()
for i in range(0,n+1):
  for j in range(i):
    print(" ",end=" ")
  for j in range(i,n):
    print("*",end=" ")
  for j in range(i,n+1):
    print("*",end=" ")
  for j in range(i):
    print(" ",end=" ")
  print()




#simple program
n = 5
for i in range(1, n+1):
  print(" "*(n-i) ,"* "*i)
for i in range(n-1,0,-1):
  print(" "*(n-i),"* "*i)




#daimond program
n = int(input("enter the size of pyramid"))    # Ask user for the size (height) of the pyramid

# 🔼 Upper Half of the Diamond (Growing Pyramid)
for i in range(n):                            
    for j in range(i, n):                      # Print decreasing spaces to center the stars
        print(" ", end="")                    
    for j in range(i):                         # Print increasing stars in each row
        print("*", end=" ")                   
    print()                                    # Move to the next line

# 🔽 Lower Half of the Diamond (Shrinking Pyramid)
for i in range(n):                            
    for j in range(i):                         # Print increasing spaces to shift stars right
        print(" ", end="")                    
    for j in range(n, i, -1):                  # Print decreasing stars in each row
        print("*", end=" ")                   
    print()                                    # Move to the next line
                                 