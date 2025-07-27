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



#6. Vowel Counter per Word:
'''Given a sentence, return a dictionary with each word as a key and the count of vowels in that word as its value.
'''
def vowel(x):
    x=input("enter the string")
    vowels = 'aeiouAEIOU'
    result = {}
    words = x.split()
    for word in words:
        count = sum(1 for char in word if char in vowels)
        result[word] = count
    return result
print(vowel("x"))


#7.Remove Duplicates
'''# Write a function to remove duplicates from a list without using set() and return the result while preserving the original order.'''
def duplicate(x):
    x = input("Enter items separated by spaces: ")
    list = x.split()
    seen = {}
    result = []
    for item in list:
        if item not in seen:
            seen[item] = True
            result.append(item)
    return result
print(duplicate(list))


#8.Item Frequency Counter:
'''Given a list of items, return a dictionary with the count of each item.
'''
def frequency(x):
    x = input("Enter items separated by spaces: ")
    y = x.split()
    f = {}
    for item in y:
        if item in f:
            f[item] += 1
        else:
            f[item] = 1
    return f
print(frequency(list))

#9.Maximum Value Key:
'''Given a dictionary of key-value pairs, return the key that has the maximum value.
'''
def maxvalue(d):
    if not d:
        return None
    return max(d, key=d.get)
dict = {'apple': 10, 'banana': 25, 'cherry': 20}
print("Key with max value:", maxvalue(dict))


#10.Flatten Nested List:
'''#Given a list of lists (2D list), flatten it into a single list using a for loop.
'''
def flatten_nested_list(nested_list):
    flat_list = []
    for sublist in nested_list:
        for item in sublist:
            flat_list.append(item)
    return flat_list
nested = [[1, 2], [3, 4], [5], [6, 7]]
print(flatten_nested_list(nested))
print("THANK YOU")