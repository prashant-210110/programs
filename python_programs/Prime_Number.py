#printing the prime numbers in between two numers
start=int(input("enter the starting number"))
end=int(input("enter the ending number"))
for i in range(start,end+1):              # Loop through numbers from 0 to 99
  if i>1:                                 # Skip 0 and 1 (not prime)
    for j in range(2,i):                  # Check divisibility from 2 to i-1
      if i%j==0:                          # If divisible, it's not prime
        break
    else:                                 # If loop didn't break, it's prime
      print(i)                            # Print the prime number





#checking the given number is prime or not
#program to check the given number is prime number or not
n=int(input("enter the number"))
if n<=0:
  print("enter valide number")
elif n==1:
  print("1 is not a prime number")
elif n==2:
  print("2 is only even prime number")
else:
  for i in range(2,n):
    if n%i==0:
      print(f"{n} is not prime number")
      break
  else:
    print(f"{n} is a prime number")
