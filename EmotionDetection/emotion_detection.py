import json
import requests

def emotion_detector(text_to_analyze):
    url = ('https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict')
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    inputJson = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = inputJson, headers = header)
    formatted_response = json.loads(response.text)

    #declare a variable emotion_predictions to call in order to extract the required emotions
    emotion_predictions = formatted_response['emotionPredictions'][0]['emotion']
    emotion_predictor = {key: emotion_predictions[key] for key in emotion_predictions.keys()}
    #below is the code for dominant_emotion
    dominant_emotion = max(emotion_predictor, key = emotion_predictor.get)
    
    print(emotion_predictor)
    
    print(f"The dominant emotion is {dominant_emotion}")
    