from transformers import pipeline
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    question = data['question']
    context = data['context']
    result = nlp(question=question, context=context)
    return jsonify(result)

import requests
url = 'http://localhost:5000/chat'
data = {'question': 'What is the capital of France?', 'context': 'France is a country in Eur>
response = requests.post(url, json=data).json()
print(response['answer'])

app = Flask(__name__)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
