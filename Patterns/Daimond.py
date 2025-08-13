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