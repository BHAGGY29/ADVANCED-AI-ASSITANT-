import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import pyjokes
import webbrowser
import datetime
import os
import sys

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 170)  # Speed of speech
engine.setProperty('volume', 1.0)  # Volume level

def speak(text):
    """Converts text to speech"""
    engine.say(text)
    engine.runAndWait()

def recognize_speech():
    """Listens to the user and converts speech to text"""
    recognizer = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=8)  # Adding timeout
            
        command = recognizer.recognize_google(audio).lower()
        print(f"You said: {command}")
        return command
    except sr.UnknownValueError:
        speak("Sorry, I couldn't understand. Please repeat.")
        return ""
    except sr.RequestError:
        speak("Speech service is down. Check your internet connection.")
        return ""
    except sr.WaitTimeoutError:
        speak("No input detected. Please say something.")
        return ""

def execute_command(command):
    """Executes tasks based on voice commands"""
    if 'play' in command:
        song = command.replace('play', '').strip()
        speak(f"Playing {song} on YouTube")
        pywhatkit.playonyt(song)
    
    elif 'time' in command:
        time_now = datetime.datetime.now().strftime('%I:%M %p')
        speak(f"The current time is {time_now}")
    
    elif 'search' in command:
        query = command.replace('search', '').strip()
        speak(f"Searching Google for {query}")
        webbrowser.open(f"https://www.google.com/search?q={query}")
    
    elif 'wikipedia' in command:
        query = command.replace('wikipedia', '').strip()
        speak(f"Searching Wikipedia for {query}")
        try:
            result = wikipedia.summary(query, sentences=2)
            speak(result)
        except wikipedia.exceptions.DisambiguationError as e:
            speak("The search term is too broad. Please be more specific.")
        except wikipedia.exceptions.PageError:
            speak("Sorry, I couldn't find anything on Wikipedia for that.")

    elif 'joke' in command:
        joke = pyjokes.get_joke()
        speak(joke)
    
    elif 'open' in command:
        app = command.replace('open', '').strip()
        speak(f"Opening {app}")
        try:
            if sys.platform.startswith('win'):
                os.system(f'start {app}')
            elif sys.platform.startswith('linux'):
                os.system(f'xdg-open {app}')
            elif sys.platform.startswith('darwin'):
                os.system(f'open {app}')
            else:
                speak("Sorry, I can't open applications on this system.")
        except Exception as e:
            speak("Error opening application.")

    elif 'exit' in command or 'stop' in command:
        speak("Goodbye!")
        sys.exit()
    
    else:
        speak("Sorry, I didn't understand that.")

# Main loop
if __name__ == "__main__":
    speak("Hello! I am your AI assistant. How can I help you?")
    while True:
        user_command = recognize_speech()
        if user_command:
            execute_command(user_command)

