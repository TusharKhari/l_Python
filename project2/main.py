

import random

n=random.randint(1,100)
a=-1
guesses=0
# print(f"rnd no. {n}")
while(a!=n):
    
    a=int(input("Guess a number: "))
    if(a>n):
        print("lower number please")
        guesses+=1
    elif(a<n):
        print("Higher number please")
        guesses+=1
    # else:
    #     print(f"you have guessed the number in {guesses} guesses")
    #     break


print(f"you have guessed the number in {guesses} guesses")
