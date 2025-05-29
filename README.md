# 🤖 Marisa - Advanced AI Assistant

Marisa is an advanced voice-activated AI assistant powered by OpenAI and Hugging Face Transformers, built using Python. It can interact with users through voice, perform intelligent web searches, tell jokes, analyze sentiment, open apps, respond using GPT-3.5, and even access your webcam. Think of Marisa as your personal JARVIS, with a foundation ready to scale into something much bigger.

---

## 🔧 Features

- 🎤 **Speech Recognition** – Understands user speech using Google STT
- 🔊 **Text-to-Speech (TTS)** – Talks back using pyttsx3
- 🔍 **Web Search** – Searches Google and Wikipedia
- 📺 **YouTube Integration** – Plays YouTube videos using voice commands
- 🤣 **Entertainment** – Tells jokes via `pyjokes`
- ⏰ **Time Function** – Tells current time
- 🧠 **ChatGPT Integration** – Conversations via OpenAI GPT-3.5
- 💬 **Sentiment Analysis** – Understands emotional tone using Transformers
- 📷 **Webcam Access** – Opens camera with OpenCV
- 🖥️ **App Launcher** – Opens installed apps
- 🛑 **Voice Exit** – Stops execution on command

---

## 🛠️ Technologies Used

| Category         | Tools / Libraries                                       |
|------------------|---------------------------------------------------------|
| **Voice I/O**     | `speech_recognition`, `pyttsx3`                         |
| **Web Tasks**     | `pywhatkit`, `webbrowser`, `wikipedia`                 |
| **Fun Stuff**     | `pyjokes`                                               |
| **AI & NLP**      | `openai`, `transformers`, `pipeline(sentiment-analysis)` |
| **Vision**        | `cv2 (OpenCV)`, `numpy`                                 |
| **System Utils**  | `os`, `sys`, `datetime`                                 |

---

## 🧠 Architecture Flow

[User Voice]
↓
[Speech Recognition → Text]
↓
[Intent Detection (keywords & AI)]
↓
┌────────────┬──────────────┬───────────────┬──────────────┐
│ GPT-3.5 │ Sentiment AI │ Wikipedia │ YouTube │
│ (OpenAI) │ (Transformers)│ (wikipedia) │ (pywhatkit) │
└────────────┴──────────────┴───────────────┴──────────────┘
↓
[Text Response → pyttsx3 → Audio]

---

## ⚙️ Installation

### 1. Clone the Repo

```bash
git clone https://github.com/BHAGGY29/ADVANCED-AI-ASSITANT-.git
cd ADVANCED-AI-ASSITANT-

2. Install Dependencies
Make sure Python 3.7+ is installed.
pip install -r requirements.txt
If requirements.txt is missing, install manually:
pip install speechrecognition pyttsx3 pywhatkit wikipedia pyjokes openai transformers opencv-python numpy

3. Set OpenAI API Key
Create a .env file or add your key directly into openai.api_key.
openai.api_key = "YOUR_OPENAI_API_KEY"
For security: Use .env with python-dotenv.

🚀 Run the Assistant
python marisa.py
You’ll hear Marisa say:
“Hello! I am Marisa, your AI assistant. How can I assist you today?”

🧪 Sample Voice Commands
"Play Shape of You"

"What time is it?"

"Search artificial intelligence"

"Tell me a joke"

"Analyze I am feeling really sad today"

"Chat What do you know about black holes?"

"Open notepad"

"Camera"

"Exit"
