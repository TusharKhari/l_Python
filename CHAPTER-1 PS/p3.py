import pyttsx3


engine = pyttsx3.init()
rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
engine.setProperty('rate', 175)
engine.say("I am good.")
engine.runAndWait()