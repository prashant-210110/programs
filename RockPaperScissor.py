#playing rock paper scissor with computer
print("ALL THE BEST FOR THIS GAME")
import random
x=int(input("enter any one number '0','1','2'"))
if x>2:
    print("enter valied number")
else:
    if x==0:
        print("your/'s choice is rock")
    elif x==1:
        print("your/'s choice is paper")
    else:
        print("your/'s choice is scissor")
    y=random.randint(0,2)
    if y==0:
        print("machine/'s choice is rock")
    elif y==1:
        print("machine/'s choice is paper")
    else:
        print("machine/'s choice is scissor")
    def rps(x,y):
        if x==y:
            print("match is draw")
        elif y == 0 and x == 2:
            print("you loos")
        elif x==0 and y==2:
            print("you win")
        elif y>x:
            print("you loos")
        elif x>y:
            print("you win")
        elif y==0 and x==2:
            print("you loos")
        else:
            pass
    rps(x,y)

print("thankyou for playing")