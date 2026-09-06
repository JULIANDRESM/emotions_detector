"""
This module contains the emotion detector function
that interacts with the Watson NLP API to predict emotions.
"""
import json
import requests

def emotion_detector(text_to_analyze):
    """
    Analyzes text to detect emotions using Watson NLP.
    Returns a dictionary of emotion scores and the dominant emotion.
    """
    # Check for blank input (Task 7 requirement)
    if not text_to_analyze or text_to_analyze.strip() == "":
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    url = (
        'https://sn-watson-emotion.labs.skills.network/v1/'
        'watson.runtime.nlp.v1/NlpService/EmotionPredict'
    )
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }

    try:
        response = requests.post(url, json=myobj, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException:
        # If API returns error (like 400), return dictionary with None values
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    # If the response is successful (status 200)
    formatted_response = json.loads(response.text)

    # Extract the emotions dictionary
    emotions = formatted_response['emotionPredictions'][0]['emotion']

    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    joy_score = emotions['joy']
    sadness_score = emotions['sadness']

    # Determine the dominant emotion
    dominant_emotion = max(emotions, key=emotions.get)

    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }
