from flask import Flask, render_template
import json
import os

wer = Flask(__name__)

def load_clinics():
    try:
        filepath = os.path.join('data', 'clinics.json')
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
            clinics = data.get('clinics', [])
            return clinics
    except:
        return []

@wer.route('/')
def home():
    return render_template('index.html')

@wer.route('/research')
def isled():
    return render_template('research.html')

@wer.route('/safety')
def bezopas():
    return render_template('safety.html')

@wer.route('/clinics')
def clinics():
    clinics_data = load_clinics()
    return render_template('clinics.html', clinics=clinics_data)

@wer.route('/care')
def yxod():
    return render_template('care.html')

if __name__ == '__main__':
    wer.run(debug=True)
