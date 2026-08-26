from flask import Flask, send_file, render_template
from pipeline import run_pipeline

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate')
def generate():
    run_pipeline()
    return send_file('study_guide.pdf')

if __name__ == '__main__':
    app.run(debug=True)