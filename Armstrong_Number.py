#checking armstrong number or not
'''
here we use while loop when x is not equals to zero then the loop will execute then we will chwck thw given conditions of the armstrong number then it will execute
if the result sum is equals to the number we enter then it will be the armstrong number otherwise it will not a armstrong number
'''
x=int(input("enter the number"))
a=x
sum=0
b=len(str(x))
while x!=0:
  d=x%10
  sum=sum+d**b
  x=x//10
if sum==a:
  print(a,"is armstrong")
else:
  print(a,"is not armstrong")


#print all armstrong numbers
'''
to print some numbers we ask the range then we use the for loop to execute the loop then we assign the valuse that i to the a 
then we are having the while loop and in that we have the condition checking the armstrong  if the condition is true then the result will print other wise it will not print at finally we get the list of armstrong numbers
'''
x=int(input ("enter the range"))
for i in range(x):
    a = i
    sum = 0
    b = len(str(i))
    while i!=0:
        d=i%10
        sum=sum+d**b
        i=i//10
    if sum==a:
        print(sum)





def amstrong(x):
  x=int(input("enter the number"))
  a=x
  sum=0
  b=len(str(x))
  while x!=0:
    d=x%10
    sum=sum+d**b
    x=x//10
  if sum==a:
    print("armstrong")
  else:
    print("not armstrong")
amstrong(153)