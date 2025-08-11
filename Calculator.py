#calculator
class calculate():
  def __init__(self,a,b):
    self.a=a
    self.b=b
  def add(self):
    return self.a+self.b
  def sub(self):
    return self.a-self.b
  def mul(self):
    return self.a*self.b
  def div(self):
    return self.a/self.b
  def fdiv(self):
    return self.a//self.b
  def mod(self):
    return self.a%self.b
a=int(input("enter the first number"))
b=int(input("enter the second number"))
obj=calculate(a,b)
print(obj.add())
print(obj.sub())
