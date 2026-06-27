import requests

WEBHOOK_URL = "https://hook.eu1.make.com/qk6oitngoatbwwwmrvdqgqcja3r1s45s"

def send_to_make(filename, transcript, summary):

    data = {
        "filename": filename,
        "transcript": transcript,
        "summary": summary
    }

    response = requests.post(WEBHOOK_URL, json=data)

    print(response.status_code)
    print(response.text)