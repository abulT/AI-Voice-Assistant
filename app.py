from services.make_service import send_to_make
import sqlite3
from flask import Flask, render_template, request, send_file, redirect
import os

from services.whisper_service import transcribe_audio
from services.groq_service import generate_summary, ask_question, translate_text

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "uploads"

transcript_text = ""


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():

    global transcript_text

    audio = request.files["audio"]

    if audio.filename == "":
        return "No file selected"

    filepath = os.path.join(app.config["UPLOAD_FOLDER"], audio.filename)

    audio.save(filepath)
    print(filepath)
    print(os.path.getsize(filepath))

    transcript_text = transcribe_audio(filepath)

    with open("downloads/transcript.txt", "w", encoding="utf-8") as file:
        file.write(transcript_text)

        summary = generate_summary(transcript_text)

    with open("downloads/summary.txt", "w", encoding="utf-8") as file:
        file.write(summary)
        
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO history(filename, transcript, summary)
        VALUES (?, ?, ?)
        """,
        (audio.filename, transcript_text, summary)
    )

    conn.commit()
    conn.close()

    send_to_make(
    audio.filename,
    transcript_text,
    summary
)

    return render_template(
    "result.html",
    transcript=transcript_text,
    summary=summary
)


@app.route("/chat", methods=["POST"])
def chat():

    global transcript_text

    question = request.form["question"]

    answer = ask_question(transcript_text, question)

    return f"""
    <h2>AI Answer</h2>

    <p>{answer}</p>

    <br>

    <a href="/">Go Home</a>
    """
@app.route("/translate", methods=["POST"])
def translate():

    global transcript_text

    language = request.form["language"]

    translated = translate_text(transcript_text, language)

    return f"""
    <h2>Translated Text ({language})</h2>

    <p>{translated}</p>

    <br>

    <a href="/">Home</a>
    """

@app.route("/history")
def history():

    search = request.args.get("search")

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    if search:

        cursor.execute("""
        SELECT * FROM history
        WHERE filename LIKE ?
        OR transcript LIKE ?
        OR summary LIKE ?
        """,
        (f"%{search}%", f"%{search}%", f"%{search}%"))

    else:

        cursor.execute("SELECT * FROM history ORDER BY id DESC")

    rows = cursor.fetchall()

    conn.close()

    return render_template("history.html", rows=rows)

@app.route("/delete/<int:id>")
def delete(id):

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM history WHERE id=?", (id,))

    conn.commit()
    conn.close()

    return redirect("/history")


if __name__ == "__main__":
    app.run(debug=True)