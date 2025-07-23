# 🤖 Buddy - Your Personal AI Voice Assistant for Desktop

**Buddy** is a Python-based AI assistant that runs locally on your desktop. Inspired by J.A.R.V.I.S from Iron Man, it listens for voice commands, responds intelligently, and can control your system — all powered by modern AI like GPT-4o (via Groq API).

---

## ✨ Features

- 🎙️ **Real-time Speech Recognition**
- 🧠 **Chat with GPT-4o (Groq API Integration)**
- 🌐 **Multilingual Support (mtranslate)**
- 🖥️ **Reads On-screen Text Out Loud**
- 📂 **Open Files, Folders, Websites, and Applications**
- 🔐 **Secure Environment using `.env`**
- 🧩 **Modular Design – Easily Extend with New Features**

---

## 🛠️ Tech Stack

- Python 3.x
- `selenium` — voice capture via browser
- `mtranslate` — translation module
- `Groq GPT-4o` — AI response engine
- `dotenv` — API key management
- `tensorflow` (optional) — model optimization
- `TTS / STT` — text-to-speech and speech-to-text libraries

---

## 🚀 Getting Started

### 1. Clone the Repository

2. Install Requirements

bash
Copy
Edit
pip install -r requirements.txt

3. Add Environment Variables

Create a .env file in the root directory with:
ini
Copy
Edit
GroqAPIKey=your_groq_api_key_here
4. Run the Assistant

bash
Copy
Edit
python Backend/SpeechToText.py
or

bash
Copy
Edit
python main.py

📁 Project Structure
bash
Copy
Edit
Buddy/
├── Backend/
│   ├── SpeechToText.py
│   ├── GroqAPI.py
│   ├── ...
├── .env
├── requirements.txt
├── README.md
└── ...
🧠 How It Works
Listens for your voice command

Translates speech to text

Sends the query to Groq GPT-4o

Speaks the response aloud

Executes relevant commands (open apps, read screen, etc.)

