# 🎙️ AI Voice Assistant

## 📌 Overview

AI Voice Assistant is an intelligent web application that converts speech into text using OpenAI Whisper, generates AI-powered summaries with Groq LLM, translates transcripts into multiple languages, answers questions based on the transcript, and stores the results in a SQLite database. The application also integrates with Make.com to automatically send transcript data to Google Sheets for easy record management.

---

# 🚀 Features

* 🎤 Upload audio files (.mp3, .wav, .ogg)
* 📝 Speech-to-Text using OpenAI Whisper
* 🤖 AI-generated summaries using Groq LLM
* 💬 AI-powered Question & Answer system
* 🌍 Multi-language Translation

  * English
  * Tamil
  * Hindi
* 💾 SQLite Database for transcript history
* 📜 View uploaded transcript history
* 🔍 Search previous transcripts
* 🗑 Delete transcript history
* 📄 Download transcript
* 📄 Download summary
* 🔗 Make.com Webhook Integration
* 📊 Automatic Google Sheets synchronization
* 🎨 Responsive web interface using HTML and CSS

---

# 🛠️ Tech Stack

## Backend

* Python
* Flask

## AI Models

* OpenAI Whisper
* Groq LLM

## Database

* SQLite

## Frontend

* HTML5
* CSS3

## Automation

* Make.com
* Google Sheets

---

# 📂 Project Structure

```text
AI-Voice-Assistant/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── services/
│   ├── whisper_service.py
│   ├── groq_service.py
│   └── make_service.py
│
├── templates/
│   ├── index.html
│   ├── result.html
│   ├── history.html
│   └── translate.html
│
├── static/
│   └── style.css
│
├── uploads/
├── downloads/
└── database.db
```

---

# ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/abulT/AI-Voice-Assistant.git
```

### Navigate to the project folder

```bash
cd AI-Voice-Assistant
```

### Create a virtual environment

```bash
python -m venv venv
```

### Activate the virtual environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### Install required packages

```bash
pip install -r requirements.txt
```

### Create a `.env` file

```env
GROQ_API_KEY=your_groq_api_key
MAKE_WEBHOOK_URL=your_make_webhook_url
```

### Run the application

```bash
python app.py
```

Open your browser:

```
http://127.0.0.1:5000
```

---

# 🔄 Workflow

```text
User Uploads Audio
          │
          ▼
OpenAI Whisper
(Speech-to-Text)
          │
          ▼
Transcript Generated
          │
          ▼
Groq LLM
   │
   ├── AI Summary
   ├── Translation
   └── Question Answering
          │
          ▼
SQLite Database
          │
          ▼
Make.com Webhook
          │
          ▼
Google Sheets
```

---

# 📸 Screenshots

### Home Page

*Add screenshot here*

### Upload & Transcript

*Add screenshot here*

### AI Summary

*Add screenshot here*

### Translation

*Add screenshot here*

### History Page

*Add screenshot here*

### Google Sheets Integration

*Add screenshot here*

### Make.com Workflow

*Add screenshot here*

---

# 🎯 Future Enhancements

* 🎙️ Live voice recording
* 🔊 Text-to-Speech output
* 👥 Speaker identification
* 😀 Emotion detection from speech
* 📄 PDF export
* ☁️ Cloud deployment
* 🔐 User authentication
* 📱 Mobile responsive design improvements

---

# 💡 Applications

* Meeting transcription and summarization
* Lecture note generation
* Interview analysis
* Voice documentation
* Customer support analysis
* AI-powered personal assistant

---

# 👩‍💻 Author

** Mohamed Abul Faizal T **

Computer Science Student

* Java Full Stack Developer
* Python Developer
* AI & Machine Learning Enthusiast
* Data Science Learner

GitHub: https://github.com/abulT

---

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.

Thank you for visiting this repository!
