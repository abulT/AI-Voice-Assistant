from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_summary(transcript):

    prompt = f"""
    Summarize the following transcript into short bullet points.

    Transcript:
    {transcript}
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content


def ask_question(transcript, question):

    prompt = f"""
    Transcript:
    {transcript}

    Question:
    {question}

    Answer only using the transcript.
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content

def translate_text(text, language):

    prompt = f"""
    Translate the following text into {language}.

    Text:
    {text}

    Only return the translated text.
    """

    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return completion.choices[0].message.content