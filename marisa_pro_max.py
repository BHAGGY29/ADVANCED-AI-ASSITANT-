# marisa_pro_max.py

import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import pyjokes
import webbrowser
import datetime
import os
import sys
import openai
import numpy as np
from dotenv import load_dotenv
from transformers import pipeline

# Load environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Initialize Sentiment Analysis
sentiment_analyzer = pipeline("sentiment-analysis")

# Initialize Text-to-Speech Engine
engine = pyttsx3.init()
engine.setProperty('rate', 170)
engine.setProperty('volume', 1.0)

def speak(text):
    print(f"\U0001F5E3 MARISA: {text}")
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("\U0001F3A7 Listening...")
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

def ask_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]

def execute_command(command):
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

    elif 'analyze' in command:
        text = command.replace('analyze', '').strip()
        result = sentiment_analyzer(text)
        speak(f"The sentiment is {result[0]['label']} with a confidence of {result[0]['score']:.2f}")

    elif 'chat' in command:
        user_query = command.replace('chat', '').strip()
        reply = ask_gpt(user_query)
        speak(reply)

    elif 'exit' in command or 'stop' in command:
        speak("Goodbye! Try not to miss me too much.")
        sys.exit()

    else:
        reply = ask_gpt(command)
        speak(reply)

def run():
    speak("Hey boss. Marisa Pro Max online with GUI power. Let's slay this day.")
    while True:
        command = listen()
        if command:
            execute_command(command)

if __name__ == "__main__":
    run()
