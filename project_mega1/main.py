import speech_recognition as sr
import webbrowser
import pyttsx3

# Initialize the recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(f"I will speak this text: {text}")
    engine.runAndWait()

if __name__ == "__main__":
    speak("Initializing Jarvizs...")

    while True:
        with sr.Microphone() as source:
            print("Say something!")
            audio = recognizer.listen(source)
            try:
                # Recognize speech using Sphinx (offline)
                text = recognizer.recognize_sphinx(audio)
                print("Sphinx thinks you said: " + text)
                speak(text)

                # Example: open Google if you say "open Google"
                if "open google" in text.lower():
                    webbrowser.open("https://www.google.com")
                    speak("Opening Google")

            except sr.UnknownValueError:
                print("Sphinx could not understand audio")
            except sr.RequestError as e:
                print(f"Sphinx error: {e}")
