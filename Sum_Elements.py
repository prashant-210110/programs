#sum of elements in the list
def sum():
  a=[]
  n=int(input("enter number of elements do you want"))
  for i in range(n):
    b=int(input(f"enter the numbers {i+1}:"))
    a.append(b)
  print(f"{a} is your list")
  sum=0
  for i in range(len(a)):
    sum=sum+a[i]
  print(f"the toal sum is {sum}")
sum()