from flask import Flask,request

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to SentinelAI"

@app.route('/analyze')
def analyse():
    log = request.args.get('log')

    if 'failed' in log:
        result = 'Possible brute-force attempt'
    elif 'virus' in log:
        result = 'Possible malware detected'
    else:
        result = 'No threat detected'

    return {
        'log':log,
        'analysis':result
    }

@app.route('/version')
def version():
    return 'SentinelAI version 1.0'

app.run(debug=True)