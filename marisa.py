import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import pyjokes
import webbrowser
import datetime
import os
import sys
import cv2
import numpy as np
import openai
from transformers import pipeline

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 170)  # Speed of speech
engine.setProperty('volume', 1.0)  # Volume level

# Initialize OpenAI API (Replace with your API key)
openai.api_key = "YOUR_OPENAI_API_KEY"

# NLP Sentiment Analysis
sentiment_analyzer = pipeline("sentiment-analysis")

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
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=8)
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
        except wikipedia.exceptions.DisambiguationError:
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
        except Exception:
            speak("Error opening application.")
    
    elif 'exit' in command or 'stop' in command:
        speak("Goodbye!")
        sys.exit()
    
    elif 'analyze' in command:
        text = command.replace('analyze', '').strip()
        result = sentiment_analyzer(text)
        speak(f"The sentiment is {result[0]['label']} with a confidence of {result[0]['score']:.2f}")
    
    elif 'chat' in command:
        user_query = command.replace('chat', '').strip()
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_query}]
        )
        speak(response["choices"][0]["message"]["content"])
    
    elif 'camera' in command:
        speak("Opening camera...")
        cam = cv2.VideoCapture(0)
        while True:
            ret, frame = cam.read()
            cv2.imshow("Camera", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cam.release()
        cv2.destroyAllWindows()
    
    else:
        speak("Sorry, I didn't understand that.")


# Main loop
if __name__ == "__main__":
    speak("Hello! I am Marisa, your AI assistant. How can I assist you today?")
    while True:
        user_command = recognize_speech()
        if user_command:
            execute_command(user_command)


