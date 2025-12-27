from flask import Flask, request, render_template
from youtube_downloader import download_video
from question_generator import generate_questions
from chatbot import ask_chatbot

app = Flask(__name__)
video_context = ""

@app.route("/", methods=["GET", "POST"])
def index():
    global video_context
    answer = ""
    questions = []

    if request.method == "POST":
        if "video_url" in request.form:
            video_url = request.form["video_url"]
            video_path = download_video(video_url)
        if "student_question" in request.form:
            question = request.form["student_question"]
            answer = ask_chatbot(question, video_context)
        if "generate_questions" in request.form:
            questions = generate_questions(video_context)

    return render_template("index.html", answer=answer, questions=questions)

if __name__ == "__main__":
    app.run(debug=True)