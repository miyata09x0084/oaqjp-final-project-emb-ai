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
    url = ('https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict')
    
    # Prepare request payload
    myobj = {
        "raw_document": {
            "text": text_to_analyse
        }
    }
    
    # Set required headers for API request
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Send POST request and get response
    response = requests.post(url, json=myobj, headers=header)
    
    if response.status_code == 400:
        print("Error: Invalid input text.")
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    
    # Parse response as JSON and convert to dictionary
    formatted_response = json.loads(response.text)
    
    # Print response content for debugging
    print("API Response:")
    print(formatted_response)
    
    try:
        # Extract emotion scores
        emotions = formatted_response['emotionPredictions'][0]['emotion']
        
        # Identify the dominant emotion
        dominant_emotion = max(emotions.items(), key=lambda x: x[1])[0]
        
        # Return results in required format
        result = {
            'anger': emotions['anger'],
            'disgust': emotions['disgust'],
            'fear': emotions['fear'],
            'joy': emotions['joy'],
            'sadness': emotions['sadness'],
            'dominant_emotion': dominant_emotion
        }
        
        # Print results
        print('Emotion Scores:')
        print(f'Anger: {result["anger"]}')
        print(f'Disgust: {result["disgust"]}')
        print(f'Fear: {result["fear"]}')
        print(f'Joy: {result["joy"]}')
        print(f'Sadness: {result["sadness"]}')
        print(f'Dominant Emotion: {result["dominant_emotion"]}')
        
        return result
    except KeyError as e:
        print(f"Error accessing response data: {e}")
        return None