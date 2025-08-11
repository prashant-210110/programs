#counting the vowels in the given string
def vowel():
  a=input("enter the string:")
  c=a.lower()
  count=0
  b="aeiou"
  for i in c:
    if i in b:
      count+=1
  print(count)
vowel()