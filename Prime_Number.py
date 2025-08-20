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
n = int(input("enter the number"))     # Take input from the user and convert it to an integer
if n > 1 :                             # Prime numbers are greater than 1
    for i in range(2, n):              # Loop from 2 to n-1 to check for any divisors
        if n % i == 0:                 # If n is divisible by i, it's not prime
            print("not prime")         # Print result if a divisor is found
            break                      # Exit the loop early since we know it's not prime
    else:                              # This else belongs to the for-loop, not the if-statement
        print("prime")                 # If no divisors were found, n is prime
else:                                  #else block
    print("not prime")                 # If n is 1 or less, it's not prime
