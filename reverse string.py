#we are giving input once in this project so if you want to execute every program separately soo please take input and verify once


#reversing a string by using the slicing
a=input("enter the string :")
b=a[::-1]
print("the output by using slicing :",b)


#using reversed()and join()
b=''.join(reversed(a))
print("the output by using join revresed :",b)



#using the for loop
b=" "
for i in a:
    b=i+b
print("the output by using for loop :",b)




#using while loop
b=len(a)-1
c=" "
while b>=0:
    c+=a[b]
    b-=1
print("the output by using while loop :",c)




#using recurssion
def reverse(b):
    if len(b)==0:
        return b
    return reverse(b[1:])+b[0]
b=reverse(a)
print("the output by using recurssion :",b)



#using stack
b=list(a)
c=" "
while b:
  c+=b.pop()
print("the output by using stack",c)
