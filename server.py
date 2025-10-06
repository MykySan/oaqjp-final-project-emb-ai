from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector  # ваш модуль

app = Flask(__name__)

@app.route("/emotionDetector", methods=["GET", "POST"])
def emotionDetector():
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    if response.get('dominant_emotion') is None:
        return 'Invalid text! Please try again!'

    return (
        f"For the given statement, the system response is "
        f"'anger': {response.get('anger', 0.0)}, 'disgust': {response.get('disgust', 0.0)}, "
        f"'fear': {response.get('fear', 0.0)}, 'joy': {response.get('joy', 0.0)} and "
        f"'sadness': {response.get('sadness', 0.0)}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )


@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
