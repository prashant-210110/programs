#finding the maximum number from the list of numbers input() no max() use range() use split()
x=input("enter the list by using space button")
list=x.split()
count=0
for list in x:
    count=count+1
print(count)
for j in range(len(list)):
    list[j] = int(list[j])
print(list) 
print(list)