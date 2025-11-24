#gussing game
import random
a=random.randint(0,9)
print(a)
chance=5
for i in range(chance):
  b=int(input("guess your number between 0 to 9:"))
  if len(str(b))==1:
    if b==a:
      print("your correct")
      print("you won the game")
      if chance-i-1==4:
        print("you are correct in first attempt")
      if chance-i-1==3:
        print("you are correct in second attempt")
      if chance-i-1==2:
        print("you are correct in third attempt")
      if chance-i-1==1:
        print("you are correct in fourth attempt")
      break
    else:
      print(f"incorrect.... please try again you have {chance-i-1} attempts ")
      if chance-i-1==0:
        print("your loss")
  else:
    print("enter the correct one digit number")
  i=i-1
