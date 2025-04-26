

a = int(input("Enter your age : "))

if(a>=18):
    print("You are above the age of consent")
    print("Good for you")
elif(a<0):
    print("you are entering a invalid age ( negative age )")
elif(a==0):
    print("0 is not a valid age")
else:
    print("You are below the age of consent")