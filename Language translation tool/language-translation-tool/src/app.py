from flask import Flask, render_template, request, jsonify
from translation.google_translate import GoogleTranslate
from tts.text_to_speech import TextToSpeech

app = Flask(__name__)
translator = GoogleTranslate()
tts = TextToSpeech()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    data = request.json
    text = data.get('text')
    source_lang = data.get('source_lang')
    target_lang = data.get('target_lang')
    
    translated_text = translator.translate_text(text, source_lang, target_lang)
    return jsonify({'translated_text': translated_text})

@app.route('/speak', methods=['POST'])
def speak():
    data = request.json
    text = data.get('text')
    
    tts.speak(text)
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(debug=True)