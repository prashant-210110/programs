#pyramid program
n=int(input("enter the size of pyramid"))     # Ask the user to input the number of rows for the pyramid
for i in range(n):                            # Outer loop to handle the number of rows (0 to 4)
    for j in range(i, n):                     # Prints spaces to align the stars to the right
        print(" ", end="")                    # Print space without newline
    for j in range(i + 1):                    # Prints stars, increasing with each row
        print("*", end=" ")                   # Print star followed by space, without newline
    print()  



#inverted pyramid program
n = int(input("enter the size of pyramid"))   # Ask the user to input the number of rows for the pyramid
for i in range(n):                            # Loop through each row from 0 to n-1
    for j in range(i):                        # Print increasing spaces to shift stars to the right
        print(" ", end="")                    # Print a space without moving to the next line
    for j in range(n, i, -1):                 # Print decreasing number of stars in each row
        print("*", end=" ")                   # Print a star followed by a space, without newline
    print()                                   # Move to the next line after finishing one row