from flask import Flask, send_file
from pipeline import run_pipeline

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Canvas AI Agent</h1> <a href="/generate"> <button>Generate my study guide </button> </a>'

@app.route('/generate')
def generate():
    run_pipeline()
    return send_file('study_guide.pdf')

if __name__ == '__main__':
    app.run(debug=True)