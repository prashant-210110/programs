#checking the given strong is palindrome or not
a=input("enter the string")
b=a[::-1]
if a==b:
  print(f"{a} is palindrome")
else:
  print(f"{a} is not a palindrome")