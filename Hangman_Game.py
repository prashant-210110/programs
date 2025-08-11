#HANGMAN GAME WITH OUT THAT PICS
import random
lives=6
word=['apple','mango','banana']
rand_word=random.choice(word)
print(rand_word)
display=[]
b=len(rand_word)
for i in range(b):
  display+='_'
print(display)
game_over=False
while not game_over:
  user_guess=input("enter your guessed letter").lower()
  for i in range(len(rand_word)):
    l=rand_word[i]
    if l==user_guess:
      display[i]=l
  print(display)
  if user_guess not in rand_word:
    lives-=1
    if lives==0:
      game_over=True
      print("game over")
      print("you lost")
  if '_' not in display:
    game_over=True
    print("you win")