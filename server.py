from flask import Flask, request, jsonify, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def render_index_page():
    return render_template('index.html')

@app.route('/emotionDetector')
def detect_emotion():
    text_to_analyze = request.args.get('textToAnalyze')
    
    if not text_to_analyze:
        return jsonify({"error": "No text provided for analysis"}), 400

    try:
        result = emotion_detector(text_to_analyze)
        response_text = (
            f"The system's response to the given text is: "
            f"'anger': {result['anger']}, "
            f"'disgust': {result['disgust']}, "
            f"'fear': {result['fear']}, "
            f"'joy': {result['joy']} "
            f"and 'sadness': {result['sadness']}. "
            f"The dominant emotion is {result['dominant_emotion']}."
        )
        return jsonify({"message": response_text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

#     @app.route("/sentimentAnalyzer")
# def sent_analyzer():
#     # リクエスト引数から分析するテキストを取得
#     text_to_analyze = request.args.get('textToAnalyze')

#     # テキストをsentiment_analyzer関数に渡し、応答を保存
#     response = sentiment_analyzer(text_to_analyze)

#     # 応答からラベルとスコアを抽出
#     label = response['label']
#     score = response['score']

#     # 感情ラベルとスコアを含むフォーマットされた文字列を返す
#     return "与えられたテキストは{}として識別され、スコアは{}です。".format(label.split('_')[1], score)