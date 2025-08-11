#normal box or square
n=int(input("enter the size"))
for i in range(n):
    for j in range(n):
        print("*",end="")
    print()


#hollow box,hollow square
n=int(input("enter the size"))
for i in range(n):
  for j in range(0,n):
    if i==0 or j==0 or i==n-1 or j==n-1:
      print("*",end=" ")
    else:
      print(" ",end=" ")
  print()