from flask import Flask,request
from app.modules.analyzer import analyze_log

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to SentinelAI"

@app.route('/analyze')
def analyze():
    log = request.args.get('log')
    result = analyze_log(log)

    return{
        'analysis':result,
    }

@app.route('/version')
def version():
    return 'SentinelAI version 1.0'

app.run(debug=True)