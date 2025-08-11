#caser cipher
alp=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def encryption(plain_text,shift_key):
  ciper_text=""
  for i in plain_text:
    if i in alp:
      p=alp.index(i)
      new=p+shift_key%26
      ciper_text+=alp[new]
    else:
      ciper_text+=i
  print(ciper_text)
def decryption(ciper_text,shift_key):
  plain_text=""
  for i in ciper_text:
    if i in alp:
      p=alp.index(i)
      new=p-shift_key%26
      plain_text+=alp[new]
    else:
      plain_text+=i
  print(plain_text)
end=False
while not end:
  do=input("type encrypt or decrypt")
  text=input("enter the text")
  shift=int(input("enter the shift"))
  if do =="encrypt":
    encryption(text,shift)
  elif do=="decrypt":
    decryption(text,shift)
  else:
    print("invalid input")
  play_again=input("type yes if you want to play again")
  if play_again=="yes":
    end=False
  else:
    end=True