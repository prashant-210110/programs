#1.even digit sum check-wap that returns yes if the sym of even digits is greatert then sum of digits of odd .otherwise return no
def check(x):
    x=int(input("enter the number"))
    sum_even=0
    sum_odd=0
    for digit in str(x):
        d=int(digit)
        if d%2==0:
            sum_even+=d
        else:
            sum_odd+=d
    return "Yes" if sum_even > sum_odd else "No"
print(check(1524))



#2. Grade Categorizer
'''Write a function that accepts a score between 0 and 100 and returns a letter grade based on the following criteria:
 * A: 90-100
 * B: 75-89
 * C: 60-74
 * D: 40-59
 * F: Below 40'''
def grade(m):
    m=int(input("enter the marks of the student"))
    if m>=90 and m<=100:
        return "A"
    elif m>=75 and m<=89:
        return "B"
    elif m>=60 and m<=74:
        return "C"
    elif m>=40 and m<=59:
        return "d"
    elif m<40 and m>0:
        return"you are fail"
    else:
        return"invalid marks ,please enter correct markd between 0 to 100"
print(grade(125))



#3. Leap Year Checker
'''Write a function that takes a year as input and returns whether it is a leap year or not using if-else conditions.
'''
def leapyear(x):
    x = int(input("enter the year"))
    if x % 4 == 0:
        if x % 100 == 0:
            if x % 400 == 0:
                print("leap year")
            else:
                print("not a leap year")
        else:
            print("leap year")
    else:
        print("not a leap year")
print(leapyear(1523))



#4. Reverse Word Pyramid
'''Write a program that takes a string and prints it in a reverse triangle pattern, removing one character from the end in each line.
'''
def reverse(x):
    x=input("enter the string")
    length = len(x)
    for i in range(length, 0, -1):
        print(x[:i])
reverse("x")

#5. List of Squares of Even Numbers
'''Given a list of integers, return a new list containing the squares of only the even numbers.
'''
def square(num):
    return [n**2 for n in num if n % 2 == 0]
nums=[1,5,8,6,8,2,1,4]
result=square(nums)
print(result)



#6