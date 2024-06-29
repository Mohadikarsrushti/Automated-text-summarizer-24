from flask import Flask, request, jsonify
from flask_cors import CORS
from model_training import load_model, summarize_text

app = Flask(_name_)
CORS(app)

model, tokenizer = load_model()

@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.json
    text = data['text']
    summary = summarize_text(model, tokenizer, text)
    return jsonify({'summary': summary})

if _name_ == '_main_':
    app.run(debug=True)