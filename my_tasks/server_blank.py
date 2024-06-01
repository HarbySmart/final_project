#import the Flask library and other libraries needed for this application
from flask import Flask, request, render_template

#import the emotion_detector function from the package
from EmotionDetection.emotion_detection import emotion_detector

# Initialize the flask app
app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def emo_detector():
    text_to_analyse = request.args.get('textToAnalyze')
    dominant_emotion = emotion_detector(text_to_analyse)

    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    else:
        return f"The input text has been identified as {dominant_emotion}"

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000)
    