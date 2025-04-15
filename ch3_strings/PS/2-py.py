from datetime import datetime


letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''

name=input("Please enter your name: ")
now = datetime.now()
dateT=now.strftime("%Y-%m-%d")
# dateT=now.strftime("%Y-%m-%d %H:%M:%S")
letter=letter.replace("<|Name|>", name).replace("<|Date|>", dateT)
 

print(letter)