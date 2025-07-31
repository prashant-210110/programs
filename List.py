#append(2),extend(b),insert(1,15)
List=[1,2,3,4,5,6]
print(List)
List.append(108)                #we will add only one item at a time by using this append()
print(List)
b=[99,98,97]
List.extend(b)                  #list will add another list
print(List)
List.insert(0,0)    #adding 0 at 0index
print(List)

#removing methods pop(),del,clear()
List.pop()
print(List)
List.pop(4)
print(List)             #giving index value to delete other wise it will take out from last
del List[3]             #deleting the element which is present in the index
print(List)
List.clear()
print(List)


#loops in list
List=[]
for i in range(1,10):
    List.append(i)
print(List)
a=[15,12,14,15,12,13,16]
[print(x) for x in a]               #the two lines are having same meaning
for i in a:
    print(i)


#sorting the list
b=[21,105,14,13,16,19,18,17]
b.sort()
print(b)
b.sort(reverse=True)
print(b)
c=["sai","EHFIWUE","KERHO"]
c.sort(key=str.lower)
print(c)


#adding two lists by using +,append,extend
a.extend(b)
print(a)
d=[80,81,82]
for i in d:
    a.append(i)
    a.sort()
print(a)
print(a.count(18))
print(a.index(105))
