guess=5
i=0
chance=4
while(i<5):
    user=int(input("enter your guess number"))
    if(guess==user):
        print("you win the game")
        break
    else:
        print("you have",chance,"chance")
        i+=1
        chance-=1