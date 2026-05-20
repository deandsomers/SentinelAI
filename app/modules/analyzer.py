def analyze_log(log):

    if 'failed' in log:
        result = 'Possible brute-force attempt'
        severity = 'medium'
    elif 'virus' in log:
        result = 'Possible malware detected'
        severity = 'high'
    elif 'unauthorized' in log:
        result = 'Unauthorized intrusion detected' 
        severity = 'low'   
    elif 'malware' in log:
        result = 'Malware detected'
        severity = 'medium'
    elif 'suspicious' in log:
        result = 'Suspiscious activity detected' 
        severity = 'low'
    elif 'attack' in log:
        result = 'Direct attack detected'
        severity = 'high'
    else:
        result = 'No threat detected'
        severity = 'low'

    return {
        'log':log,
        'analysis':result,
        'severity':severity
    }