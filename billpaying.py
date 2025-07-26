#without using choice to select a person to pay the  bill
import random
x=input("enter all names by using comma")
list=x.split(",")
b=len(list)
choice=random.randint(0,b-1)
print(f"{list[choice]} :will pay the bill")