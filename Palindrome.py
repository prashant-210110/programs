#checking the given strong is palindrome or not
a=input("enter the string")
b=a[::-1]                           #reversing the string by using slicing
if a==b:                            #checking if the both strings are equal or not
  print(f"{a} is palindrome")       #if equal this will print
else:
  print(f"{a} is not a palindrome") #else this will print