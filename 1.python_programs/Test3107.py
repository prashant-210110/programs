#1.write a function to check if a number is an amstring number
def amstrong(x):
  x=int(input("enter the number"))
  a=x
  b=len(str(x))
  sum=0
  while x!=0:
    d=x%10
    sum=sum+d**b
    x=x//10
  if sum==a:
    print("amstrong number")
  else:
    print("not amstrong ")
amstrong(153)


#2.write a recursive function to reverse a string
def reverse(x):
  x=input("enter string")
  y=x[::-1]
  return y
print(reverse("sai"))



#7.use the random module to simulate rolling two dice 1000 times ,and count how many times their sum is 7
import random
a=0
for i in range(10):
  d1=random.randint(1,6)
  d2=random.randint(1,6)
  print(d1,d2)
  if sum==7:
    a+=1
  else:
    pass
print(a)

#6.use math module to write a function that takes a radius and return the area and circumference of a circle
import math
def area(r):
  r=int(input("enter the radius of the circle"))
  area=math.pi*r*r
  return area
def circumference(r):
  r=int(input("enter the radius of circle"))
  c=2*math.pi*r
  return c
print(area(5))
print(circumference(5))