
from flask import Flask, render_template, request, jsonify
from utils.text_extractor import extract_text_from_pdf
from utils.ai_helper import simplify_text, answer_question
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    f = request.files.get('file')
    if not f:
        return jsonify({'error': 'no file uploaded'}), 400
    filename = os.path.join('sample_docs', f.filename)
    f.save(filename)
    text = extract_text_from_pdf(filename)
    # Call Vertex AI / GenAI to simplify (this will call out to your configured GCP project)
    summary = simplify_text(text)
    return jsonify({'summary': summary})

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json or {}
    doc_text = data.get('doc_text', '')
    question = data.get('question', '')
    if not question:
        return jsonify({'error':'no question provided'}), 400
    answer = answer_question(doc_text, question)
    return jsonify({'answer': answer})

if __name__ == '__main__':
    app.run(debug=True)
