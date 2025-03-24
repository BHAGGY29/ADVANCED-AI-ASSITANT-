import openai
import pyttsx3
import speech_recognition as sr

# 🔑 Set up OpenAI API Key
openai.api_key = ""

# 🎤 Function to recognize speech
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎙️ Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("⏳ Recognizing...")
        text = recognizer.recognize_google(audio)
        print(f"👤 You: {text}")
        return text
    except sr.UnknownValueError:
        print("😕 Could not understand")
        return ""
    except sr.RequestError:
        print("🚨 Speech service error")
        return ""

# 🧠 Function to get AI response
def get_ai_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]

# 🗣️ Function to make AI speak
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# 🤖 AI Assistant Loop
while True:
    user_input = recognize_speech()
    if user_input.lower() in ["exit", "quit", "stop"]:
        print("👋 Shutting down...")
        speak("Goodbye!")
        break

    ai_response = get_ai_response(user_input)
    print(f"🤖 AI: {ai_response}")
    speak(ai_response)
