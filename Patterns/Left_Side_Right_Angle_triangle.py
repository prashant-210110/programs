#left sided right angle triangle
 n=int(input("enter the size"))
 for i in range(0,n+1):
  for j in range(i,n+1):
    print(" ",end=" ")
  for j in range(i):
    print("*",end=" ")
  print()


#inverted left sided right angle triangle
n=int(input("enter the size"))
for i in range(0,n+1):
  for j in range(i,n):
    print("*",end=" ")
  for j in range(i):
    print("",end=" ")
  print()