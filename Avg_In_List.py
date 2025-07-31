#average height from a list of heights no using of sum() and len() use input()output will be whole number
heights=input("enter the heights:")
height=heights.split()
count=0
for r in height:
  count=count+1
print(count)
for i in range(count):
    height[i] = int(height[i])
sum=0
for i in height:
  sum=sum+i
print("the sum of the list is:",sum)
average=sum/count
print("the average pf the list is :",round(average))