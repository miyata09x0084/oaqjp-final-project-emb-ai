import requests  # Import requests library for handling HTTP requests
import json  # Add json library to process JSON data


def emotion_detector(text_to_analyse):
    """
    Analyze the sentiment of input text using Watson NLP API.
    
    Args:
        text_to_analyse (str): Text to be analyzed
        
    Returns:
        dict: API response containing sentiment analysis results
    """
    # API endpoint for sentiment analysis
    url = ('https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime'
           '.nlp.v1/NlpService/SentimentPredict')
    
    # Prepare request payload
    myobj = {
        "raw_document": {
            "text": text_to_analyse
        }
    }
    
    # Set required headers for API request
    header = {
        "grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"
    }
    
    # Send POST request and get response
    response = requests.post(url, json=myobj, headers=header)
    
    # Parse response as JSON and convert to dictionary
    formatted_response = json.loads(response.text)
    
    # Extract emotion scores
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    
    # Identify the dominant emotion
    dominant_emotion = max(emotions.items(), key=lambda x: x[1])[0]
    
    # Return results in required format
    return {
        'anger': emotions['anger'],
        'disgust': emotions['disgust'],
        'fear': emotions['fear'],
        'joy': emotions['joy'],
        'sadness': emotions['sadness'],
        'dominant_emotion': dominant_emotion
    }