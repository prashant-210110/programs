import random
def dice():
  a=0
  for i in range(10):
    d1=random.randint(1,6)
    d2=random.randint(1,6)
    print(d1,d2)
    sum=d1+d2
    if sum==7:
      a+=1
    else:
      pass
  print(a)
dice()