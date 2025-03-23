import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Adjust speed (100-200)
    engine.setProperty('volume', 1.0)  # Adjust volume (0.0 to 1.0)
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    speak("Hello bhagath! I am your AI assistant. How can I help you?")
