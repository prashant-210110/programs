a=0
b=1
n=int(input("enter how many numbers do you  want:"))
sum=0
print(a)
print(b)
for i in range(n):
    sum=a+b
    a,b=b,sum
    print(sum)
print("thank you")




#Fibonacci Sequence
def Fibonacci():
  a=0
  b=1
  sum=0
  n=int(input("enter the range"))
  print(a)
  print(b)
  for i in range(2,n):
    sum=a+b
    a,b=b,sum
    print(sum)
Fibonacci()