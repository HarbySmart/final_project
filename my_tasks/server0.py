#import the Flask library and other libraries needed for this application
from flask import Flask, request, render_template

#import the emotion_detector function from the package
from EmotionDetection.emotion_detection import emotion_detector

# Initialize the flask app
app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def emo_detector():
    text_to_analyse = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyse)
    emotion = response['emotionPredictions'][0]['emotion']
    dominant_emotion = max(emotion.items(), key=lambda x: x[1])

    return "For the given statement, the system response is {emotion}. The dominant emotion is {dominant_emotion}"

@app.route("/")
def render_index_page():
    return render_template('index.html')
    