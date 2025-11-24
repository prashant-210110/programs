#right angle triangle
n=int(input("enter the size"))
for i in range(0,n+1):
  for j in range(i):
    print("*",end=" ")
  for j in range(i):
    print("",end=" ")
  print()


#inverted right sided right angle triangle
n=int(input("enter the size"))
for i in range(0,n+1):
  for j in range(i):
    print(" ",end=" ")
  for j in range(i,n):
    print("*",end=" ")
  print()