def analyze_log(log):

    if 'failed' in log:
        return{
            'threat':'Possible brute-force attempt',
            'severity':'medium',
            'confidence': 68,
            "risk_level": "amber"
        }
    elif 'virus' in log:
        return{
            'threat':'Possible virus detected',
            'severity':'high',
            'confidence': 85,
            "risk_level": "red"
        }
    elif 'unauthorized' in log:
        return{
            'threat':'Unauthorized intrusion detected',
            'severity':'low',
            'confidence': 57,
            "risk_level": "amber"
        }
    elif 'malware' in log:
        return{
            'threat':'Malware detected',
            'severity':'medium',
            'confidence': 65,
            "risk_level": "red"
        }
    elif 'suspicious' in log:
        return{
            'threat':'Suspiscious activity detected',
            'severity':'low',
            'confidence': 56,
            "risk_level": "amber"
        }
    elif 'attack' in log:
        return{
            'threat':'Direct attack detected',
            'severity':'high',
            'confidence': 88,
            "risk_level": "red"
        }
    elif 'ransom' in log:
        return{
            'threat':'Ransomware detected',
            'severity':'high',
            'confidence': 90,
            "risk_level": "red"
        }
    elif 'phishing' in log:
        return{
            'threat':'Phishing detected',
            'severity':'medium',
            'confidence': 72,
            "risk_level": "amber"
        }
    elif 'ddos' in log:
        return{
            'threat':'ddos detected',
            'severity':'medium',
            'confidence': 76,
            "risk_level": "red"
        }
    elif 'attack' in log:
        return{
            'threat':'suspicious traffic detected',
            'severity':'medium',
            'confidence': 67,
            "risk_level": "amber"
        }
    else:
        return{
        'threat':'No threat detected',
        'severity':'low',
        'confidence': 50,
        "risk_level": "green"
        }
