''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector", methods=["GET", "POST"])
def emotion_detector_func():
    ''' This code receives the text from the HTML interface and 
        runs emotion detection over it using emotion_detector()
        function. The output returned shows the label and its confidence 
        score for the provided text.
    '''
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
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
