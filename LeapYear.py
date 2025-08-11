#chechk the given year is leap year not
#9603526342
x=int(input("enter the year"))
b=len(str(x))
if b==4:
    if x%4==0:
        if x%100==0:
            if x%400==0:
                print("leap year")
            else:
                print("not a leap year")
        else:
            print("leap year")
    else:
        print("not a leap year")
else:
    print("enter the 4 digit year")




def Leapyear(x):
  if x%4==0:
    if x%100==0:
      if x%400==0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False
Leapyear(2028)