#without using choice to select a person to pay the  bill
'''we import random module
then we take input from the user
input is in string formate
we use split() to split the string which is given by the string
then we choose by using random.randint
at last we just print the random name which is selected by the module'''
import random
x=input("enter all names by using comma")
list=x.split(",")
b=len(list)
choice=random.randint(0,b-1)
print(f"{list[choice]} :will pay the bill")


