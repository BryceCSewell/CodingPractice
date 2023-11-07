import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = myobj, headers = headers)
    formatted_response = json.loads(response.text)
    EP = formatted_response['emotionPredictions']
    convert = dict(enumerate(EP))
    anger = convert[0]['emotion']['anger']
    disgust = convert[0]['emotion']['disgust']
    fear = convert[0]['emotion']['fear']
    joy = convert[0]['emotion']['joy']
    sadness = convert[0]['emotion']['sadness']
    score = [anger, disgust, fear, joy, sadness]
    
    def emotion_predictor(score_input):
        dominant_emotion = ""
        anger = score_input[0]
        disgust = score_input[1]
        fear = score_input[2]
        joy = score_input[3]
        sadness = score_input[4]

        if anger > (disgust and fear and joy and sadness):
            dominant_emotion = "anger"
        elif disgust > (anger and fear and joy and sadness):
            dominant_emotion = "disgust"
        elif fear > (anger and disgust and joy and sadness):
            dominant_emotion = "fear"
        elif joy > (anger and disgust and fear and sadness):
            dominant_emotion = "joy"
        elif sadness > (anger and disgust and fear and joy):
            dominant_emotion = "sadness"

        emotions = {
            'anger': anger,
            'disgust': disgust,
            'fear': fear,
            'joy': joy,
            'sadness': sadness,
            'dominant_emotion': dominant_emotion,
        }

        return emotions

    emotionPredictorResult = emotion_predictor(score)
    emotion_predictor_string = str(emotionPredictorResult)
    return (emotion_predictor_string.replace(', ',', \n'))
