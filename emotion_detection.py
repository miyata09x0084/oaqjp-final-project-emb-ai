import requests  # Import requests library for handling HTTP requests


def emotion_detector(text_to_analyse):
    """
    Analyze the sentiment of input text using Watson NLP API.
    
    Args:
        text_to_analyse (str): Text to be analyzed
        
    Returns:
        str: API response containing sentiment analysis results
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
    
    return response.text