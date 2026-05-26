from flask import Flask,request
from app.modules.scanner import scan_log
from app.modules.utils import generate_timestamp,save_scan_results

app = Flask(__name__)
timestamp = generate_timestamp()

@app.route('/')
def home():
    return "Welcome to SentinelAI"

@app.route('/health')
def health():
    return {
        'application': 'healthy'
    }

@app.route('/status')
def status():
    return {
        'application': 'Ready to scan!'
    }

@app.route('/version')
def version():
    return {
        'application': 'SentinelAI',
        'version': '1.0'
    }

@app.route('/analyze')
def analyze():
    log = request.args.get('log')
    result = scan_log(log)
    save_scan_results(result)
    return{
        'timestamp':timestamp,
        'log': log,
        'result': result
    }

app.run(debug=True)