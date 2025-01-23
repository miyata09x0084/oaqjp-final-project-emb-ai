"""Flask application for emotion detection."""

from flask import Flask, request, jsonify, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def render_index_page():
    """Render the index page."""
    return render_template('index.html')

@app.route('/emotionDetector')
def detect_emotion():
    """Detect emotion from the provided text."""
    text_to_analyze = request.args.get('textToAnalyze')

    result = emotion_detector(text_to_analyze)
    if result['dominant_emotion'] is None:
        return jsonify({"error": "Invalid text! Please try again!"})

    response_text = (
        f"The system's response to the given text is: "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} "
        f"and 'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )
    return jsonify({"response": response_text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
