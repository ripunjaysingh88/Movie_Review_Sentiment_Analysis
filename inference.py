import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import tokenizer_from_json
import json
import requests

url = "http://34.93.157.158:8501/v1/models/lstm:predict"

with open('tokenizer.json', 'r', encoding='utf-8') as f: 
    data = json.load(f)
    tokenizer = tokenizer_from_json(data)
    


def get_prediction(sentence):

    x_sample_encoded = tokenizer.texts_to_sequences(sentence)
    x_sample_padded = pad_sequences(x_sample_encoded, maxlen=100, padding='pre', truncating='pre')

    data = json.dumps({"instances": x_sample_padded.tolist()})
    headers = {"content-type": "application/json"} 
    json_response = requests.post(url, data=data, headers=headers)
    prediction = json.loads(json_response.text)['predictions']
    result = prediction[0][0]
    result = round(result,2)
    return result

