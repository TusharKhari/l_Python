
import random

'''
1 for snake
-1 for water 
0 for gun
'''


computer = random.choice([-1,0,1])
# computer = -1
youStr = (input("Eneter your choice: "))
youDict = {"s":1, "w":-1, "g":0}
revDict = {1:"snake", -1:"water", 0:"gun"}
you = youDict[youStr]

print(f"computer chose {revDict[computer]}   || you chose {revDict[you]}")

if(computer==you):
    print("Its a draw")
else:
    if(computer==-1 and you==1):
        print("you win")
    elif(computer==-1 and you==0):
        print("You Lose!")
    elif(computer==1 and you==-1):
        print("You Lose!")
    elif(computer==1 and you==0):
        print("You Win!")
    elif(computer==0 and you==-1):
        print("You loose!")
    elif(computer==0 and you==1):
        print("You Loose!")
    else:
        print("Something went wrong")


# or 

if(computer==you):
    print("Its a draw")
elif((computer-you)==-1 or (computer-you)==2 ):
    print("You lose")
else : 
    print("you win")
