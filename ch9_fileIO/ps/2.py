

import random



def game():
    print("You are playing the game...")
    score = random.randint(1,62)
    
    with open("myfile.txt",'r') as f:
        hiScore=f.read()
        if(hiScore!=""):
            hiScore=int(hiScore)
        else:
            hiScore=0
    print(f"your score : {score}")
    
    
    
    if(score>int(hiScore) or hiScore==""):
        with open("myfile.txt", "w") as f:
            f.write(str(score))
        
    return score

game()










