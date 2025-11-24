import random
print(random.randint(1,100))
print(random.randrange(1,100))
print(random.choice([1,2,3,4,5,6,7,8,9]))
x=[1,5,2,6,8,100,32,3,9,8,2,]
print(random.choice(x))
print(random.shuffle(x))
print(x)
print(random.sample(x,3))
print(random.sample(x,1))
print(random.sample(x,5))